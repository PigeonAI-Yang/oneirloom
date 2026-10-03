import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright, expect

BASE = Path(__file__).resolve().parent
DRAFT = 'https://x.com/compose/articles/edit/2104389078770917376'


async def main():
    figures = json.loads((BASE / 'x-draft/manifest.json').read_text(encoding='utf-8'))['figures']
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://127.0.0.1:9334')
        page = next(q for q in browser.contexts[0].pages if q.url == DRAFT)
        editor = page.locator('[data-testid="composer"]')
        await page.get_by_text('正在上传媒体...', exact=True).wait_for(state='hidden', timeout=120000)
        count = await editor.locator('img').count()
        print(f'Existing figures: {count}', flush=True)
        assert count == 9, count
        for figure in figures[9:]:
            assert page.url == DRAFT
            marker = editor.get_by_text(figure['marker'], exact=True)
            await marker.scroll_into_view_if_needed()
            block_key = await marker.evaluate("e=>e.closest('[data-block]').getAttribute('data-offset-key')")
            await marker.click()
            await page.keyboard.press('Home')
            await page.keyboard.press('Shift+End')
            assert await page.evaluate('window.getSelection().toString()') == figure['marker']
            async with page.expect_response(lambda r: 'ArticleEntityUpdateContent' in r.url, timeout=120000) as deleted:
                await page.keyboard.press('Backspace')
            deletion_response = await deleted.value
            assert deletion_response.status == 200, deletion_response.status
            await deletion_response.finished()
            await expect(marker).to_have_count(0)
            await page.wait_for_timeout(1500)
            await expect(marker).to_have_count(0)
            empty = editor.locator(f'[data-block][data-offset-key="{block_key}"]')
            await expect(empty).to_have_text('')
            await empty.click(position={'x': 4, 'y': 8})
            await page.get_by_role('button', name='添加媒体内容', exact=True).click()
            await page.get_by_role('menuitem', name='媒体', exact=True).click()
            await page.locator('input[type=file][multiple]').set_input_files(figure['path'])
            await page.get_by_text('正在上传媒体...', exact=True).wait_for(state='visible', timeout=15000)
            await page.get_by_text('正在上传媒体...', exact=True).wait_for(state='hidden', timeout=120000)
            await page.wait_for_timeout(1000)
            count += 1
            await expect(editor.locator('img')).to_have_count(count, timeout=120000)
            caption = editor.get_by_text(figure['caption'], exact=True)
            assert await caption.evaluate('''e => !!e.closest('[data-block]').parentElement.previousElementSibling?.querySelector('section img')'''), figure['caption']
            await caption.click(click_count=3)
            assert (await page.evaluate('window.getSelection().toString()')).strip() == figure['caption']
            async with page.expect_response(lambda r: 'ArticleEntityUpdateContent' in r.url, timeout=120000) as saved:
                await page.keyboard.press('Control+i')
            response = await saved.value
            assert response.status == 200, response.status
            await response.finished()
            await page.wait_for_timeout(500)
            print(f'Inserted {count}: {figure["caption"]}', flush=True)
        result = await editor.locator('[data-block=true]').evaluate_all('''es => es.filter(e => e.querySelector('img')).map(e => ({
            after: e.parentElement.nextElementSibling?.innerText,
            src: e.querySelector('img').src,
            width: e.querySelector('img').naturalWidth,
            height: e.querySelector('img').naturalHeight
        }))''')
        (BASE / 'evidence/x-figures-inserted.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'Finished: {count} figures; remaining markers: {(await editor.inner_text()).count("〔教程配图")}', flush=True)


asyncio.run(main())
