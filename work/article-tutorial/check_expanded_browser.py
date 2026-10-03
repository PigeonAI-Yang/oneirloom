import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent


async def main():
    errors = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
            headless=True,
            args=['--disable-gpu'],
        )
        page = await browser.new_page(viewport={'width':1440, 'height':1100}, device_scale_factor=1)
        page.on('pageerror', lambda error: errors.append(str(error)))
        await page.goto((ROOT / '美女生图教程.html').as_uri(), wait_until='load')
        await page.add_style_tag(content='html{scroll-behavior:auto!important}')
        await page.evaluate('''async () => {
            const images = [...document.querySelectorAll('figure img')];
            images.forEach(img => img.loading = 'eager');
            await Promise.all(images.map(img => img.decode()));
        }''')
        desktop = await page.evaluate('''() => ({
            chapters:document.querySelectorAll('article h2').length,
            subsections:document.querySelectorAll('article h3').length,
            figures:document.querySelectorAll('figure').length,
            loadedImages:[...document.querySelectorAll('figure img')].filter(i=>i.complete&&i.naturalWidth>0).length,
            horizontalOverflow:document.documentElement.scrollWidth>innerWidth,
            copyButtons:document.querySelectorAll('.copy').length,
            everySubsectionIllustrated:[...document.querySelectorAll('article h3')].every(h=>{
                let next=h.nextElementSibling;
                while(next&&!['H2','H3'].includes(next.tagName)){
                    if(next.tagName==='FIGURE')return true;
                    next=next.nextElementSibling;
                }
                return false;
            })
        })''')
        await page.screenshot(path=str(ROOT / 'evidence/expanded-desktop-top.png'))
        for token, label in [('坐在椅子前沿和靠着椅背', 'pose'), ('叠穿时', 'layers'), ('也可以让近处的花', 'focus')]:
            locator = page.locator('h3').filter(has_text=token)
            await locator.evaluate('(e)=>e.scrollIntoView({block:"start"})')
            await page.wait_for_timeout(350)
            await page.screenshot(path=str(ROOT / f'evidence/expanded-desktop-{label}.png'))
        img = page.locator('figure img').nth(0)
        await img.click()
        desktop['lightboxOpens'] = await page.locator('dialog').evaluate('(d)=>d.open')
        await page.locator('dialog button').click()
        button = page.locator('.copy').first
        await button.click()
        await page.wait_for_timeout(150)
        desktop['copyButtonFeedback'] = await button.inner_text()
        await page.set_viewport_size({'width':390, 'height':844})
        await page.evaluate('window.scrollTo(0,0)')
        await page.wait_for_timeout(300)
        await page.screenshot(path=str(ROOT / 'evidence/expanded-mobile-top.png'))
        mobile = await page.evaluate('''() => ({
            viewport:innerWidth,
            scrollWidth:document.documentElement.scrollWidth,
            horizontalOverflow:document.documentElement.scrollWidth>innerWidth,
            mobileTocVisible:getComputedStyle(document.querySelector('.mobile-toc')).display!=='none'
        })''')
        await page.locator('h3').filter(has_text='拿杯子或搭扶手').evaluate('(e)=>e.scrollIntoView({block:"start"})')
        await page.wait_for_timeout(300)
        await page.screenshot(path=str(ROOT / 'evidence/expanded-mobile-contact.png'))
        report = {'desktop':desktop, 'mobile':mobile, 'pageErrors':errors}
        (ROOT / 'evidence/browser-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
        print(json.dumps(report,ensure_ascii=False))
        assert desktop['chapters'] == 16 and desktop['subsections'] == 37
        assert desktop['figures'] == desktop['loadedImages'] == 39
        assert desktop['everySubsectionIllustrated'] and desktop['lightboxOpens']
        assert desktop['copyButtonFeedback'] == '已复制'
        assert not desktop['horizontalOverflow'] and not mobile['horizontalOverflow'] and not errors
        await browser.close()


asyncio.run(main())
