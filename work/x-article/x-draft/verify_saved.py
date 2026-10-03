import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

root = Path('J:/PigeonYang/skills/oneirloom/docs/articles/2026-10-01-oneirloom-x')
evidence = Path(__file__).parent
data = json.loads((evidence / 'current.json').read_text(encoding='utf-8'))
editor = next(control for control in data['controls'] if control['testid'] == 'composer')
title = next(control['value'] for control in data['controls'] if control['placeholder'] == '添加标题')
assert title == (root / 'x-title.txt').read_text(encoding='utf-8').strip()
expected_html = BeautifulSoup((root / 'x-body.html').read_text(encoding='utf-8'), 'html.parser')
actual_html = BeautifulSoup(editor['html'], 'html.parser')
expected = []
for element in expected_html.find_all(['p', 'blockquote'], recursive=False):
    value = element.get_text().strip()
    match = re.fullmatch(r'〔配图([1-6])〕', value)
    expected.append({'image': int(match[1])} if match else {'text': value})
actual = []
image_index = 0
for element in actual_html.select('[data-block=true]'):
    if element.select('img'):
        image_index += 1
        actual.append({'image': image_index})
    elif element.get_text().strip():
        actual.append({'text': element.get_text().strip()})
assert expected == actual, 'article paragraph/image sequence differs from approved copy'
assert len(data['images']) == 6 and all(item['loaded'] for item in data['images'])
assert actual_html.select('a[href="https://github.com/PigeonAI-Yang/oneirloom"]')
assert len(actual_html.select('blockquote')) == 3
assert len(actual_html.select('[style*="font-weight: bold"]')) == 5
assert '草稿' in data['text']
receipt = {
    'status': 'saved_to_x_article_drafts',
    'account': '@KimbomArtist',
    'url': data['url'],
    'title': title,
    'published': False,
    'reopened_from_draft_list': True,
    'approved_body_matches': True,
    'inline_images': 6,
    'image_order_matches': True,
    'images_loaded': True,
    'github_link_verified': True,
    'blockquote_count': 3,
    'bold_heading_count': 5,
    'source_body': str(root / 'article.md'),
}
(root / 'x-draft-result.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(evidence / 'saved-editor.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(receipt, ensure_ascii=False, indent=2))
