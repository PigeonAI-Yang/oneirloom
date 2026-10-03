from hashlib import sha256
import json
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright


PROOF = Path(__file__).resolve().parent
ROOT = PROOF.parents[2]
REFERENCE = ROOT / 'skills/oneirloom-style-design/templates/experimental-editorial-posters/06-swiss-sculpture/images/reference.png'
EDGE = Path('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
WIDTH = 1450
HEIGHT = 2040


def image_size(path):
    with Image.open(path) as image:
        return list(image.size)


def dark_ink_bbox(path, region, threshold=64):
    x0, y0, x1, y1 = region
    xs = []
    ys = []
    with Image.open(path) as image:
        for y in range(y0, y1):
            for x in range(x0, x1):
                pixel = image.getpixel((x, y))
                rgb = pixel[:3] if isinstance(pixel, tuple) else (pixel, pixel, pixel)
                if max(rgb) < threshold:
                    xs.append(x)
                    ys.append(y)
    if not xs:
        return None
    return {
        'x': min(xs),
        'y': min(ys),
        'width': max(xs) - min(xs) + 1,
        'height': max(ys) - min(ys) + 1,
        'threshold_max_rgb_lt': threshold,
    }


def union_boxes(boxes):
    valid = [box for box in boxes if box]
    if not valid:
        return None
    left = min(box['x'] for box in valid)
    top = min(box['y'] for box in valid)
    right = max(box['x'] + box['width'] for box in valid)
    bottom = max(box['y'] + box['height'] for box in valid)
    return {'x': left, 'y': top, 'width': right - left, 'height': bottom - top}


def element_box(locator):
    return locator.evaluate('(element) => { const b = element.getBBox(); return {x: b.x, y: b.y, width: b.width, height: b.height}; }')


def svg_geometry(page, path, screenshot):
    page.goto(path.as_uri(), wait_until='load')
    page.evaluate('document.fonts.ready')
    page.evaluate("document.documentElement.style.margin = '0'; document.documentElement.style.padding = '0'; document.documentElement.style.overflow = 'hidden';")
    root = page.locator('svg')
    dimensions = {
        'width': float(root.get_attribute('width')),
        'height': float(root.get_attribute('height')),
        'viewBox': root.get_attribute('viewBox'),
    }
    panel = element_box(page.locator('#blue-panel'))
    screenshot_target = page.locator('svg')
    screenshot_target.screenshot(path=str(screenshot), animations='disabled')
    return dimensions, panel


def main():
    if not EDGE.is_file():
        raise FileNotFoundError(EDGE)
    reference_hash_before = sha256(REFERENCE.read_bytes()).hexdigest()
    reference_dimensions = image_size(REFERENCE)
    page_errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, executable_path=str(EDGE))
        page = browser.new_page(viewport={'width': WIDTH, 'height': HEIGHT}, device_scale_factor=1)
        page.on('pageerror', lambda error: page_errors.append(str(error)))

        source_dimensions, source_panel = svg_geometry(page, PROOF / 'source-layout.svg', PROOF / 'source-layout.png')
        page.goto((PROOF / 'source-layout.svg').as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        source_line_boxes = page.locator('#source-title-placeholders rect').evaluate_all('(elements) => elements.map(element => { const b = element.getBBox(); return {x: b.x, y: b.y, width: b.width, height: b.height}; })')
        source_local_contour = element_box(page.locator('#source-left-local-contour'))
        source_footer_box = element_box(page.locator('#source-footer-placeholder'))
        adapted_dimensions, adapted_panel = svg_geometry(page, PROOF / 'adapted-layout.svg', PROOF / 'adapted-layout.png')
        adapted_clip_geometry = {
            'upper_local_contour': element_box(page.locator('#adapted-upper-local-contour')),
            'headline_crop_strip': element_box(page.locator('#adapted-headline-crop-strip')),
            'lower_local_contour': element_box(page.locator('#adapted-lower-local-contour')),
        }
        adapted_left_cue = page.locator('#left-local-cue').evaluate('(element) => ({cx: Number(element.getAttribute("cx")), cy: Number(element.getAttribute("cy")), rx: Number(element.getAttribute("rx")), ry: Number(element.getAttribute("ry"))})')
        adapted_text = page.locator('text').evaluate_all('(elements) => elements.map(element => ({id: element.id, text: element.textContent, fontFamily: getComputedStyle(element).fontFamily, fontSize: getComputedStyle(element).fontSize, box: (() => { const b = element.getBBox(); return {x: b.x, y: b.y, width: b.width, height: b.height}; })()}))')
        svg_dom_boxes_not_actual_ink = {entry['id']: entry['box'] for entry in adapted_text}
        title_values = {entry['id']: entry['text'] for entry in adapted_text}

        page.set_viewport_size({'width': 1920, 'height': 1120})
        preview = PROOF / 'preview.html'
        page.goto(preview.as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        image_states = page.locator('img').evaluate_all('(images) => Promise.all(images.map(async image => { try { await image.decode(); } catch (error) {} return {id: image.id, loaded: image.complete && image.naturalWidth > 0, naturalWidth: image.naturalWidth, naturalHeight: image.naturalHeight, currentSrc: image.currentSrc}; }))')
        labels = page.locator('figcaption').all_text_contents()
        preview_geometry = page.evaluate('({viewportWidth: innerWidth, documentWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth, documentHeight: document.documentElement.scrollHeight})')
        comparison_path = PROOF / 'comparison.png'
        page.screenshot(path=str(comparison_path), full_page=True, animations='disabled')
        browser.close()

    reference_hash_after = sha256(REFERENCE.read_bytes()).hexdigest()
    output_dimensions = {
        'source-layout.png': image_size(PROOF / 'source-layout.png'),
        'adapted-layout.png': image_size(PROOF / 'adapted-layout.png'),
        'comparison.png': image_size(comparison_path),
    }
    title_x0 = int(WIDTH * 0.05)
    title_x1 = int(WIDTH * 0.515)
    title_split_y = int(HEIGHT * 0.39)
    title_ink_boxes = {
        'dream': dark_ink_bbox(PROOF / 'adapted-layout.png', (title_x0, int(HEIGHT * 0.25), title_x1, title_split_y)),
        'weaver': dark_ink_bbox(PROOF / 'adapted-layout.png', (title_x0, title_split_y, title_x1, int(HEIGHT * 0.56))),
    }
    title_ink_overall = union_boxes(list(title_ink_boxes.values()))
    title_line_gap = None
    if title_ink_boxes['dream'] and title_ink_boxes['weaver']:
        title_line_gap = title_ink_boxes['weaver']['y'] - (title_ink_boxes['dream']['y'] + title_ink_boxes['dream']['height'])
    footer_ink_box = dark_ink_bbox(PROOF / 'adapted-layout.png', (title_x0, int(HEIGHT * 0.84), title_x1, int(HEIGHT * 0.95)))
    title_ink_metrics = {
        'measurement_source': 'rendered adapted-layout.png pixels read with PIL; SVG getBBox is reported separately as geometry only',
        'pixel_test': 'max(R,G,B) < 64',
        'search_region_fraction': {'x': [0.05, 0.515], 'y': [0.25, 0.56]},
        'line_split_y': title_split_y,
        'dream': title_ink_boxes['dream'],
        'weaver': title_ink_boxes['weaver'],
        'overall': title_ink_overall,
        'overall_top_fraction': title_ink_overall['y'] / HEIGHT if title_ink_overall else None,
        'overall_height_fraction': title_ink_overall['height'] / HEIGHT if title_ink_overall else None,
        'line_gap_pixels': title_line_gap,
        'line_gap_fraction': title_line_gap / HEIGHT if title_line_gap is not None else None,
        'footer': footer_ink_box,
        'footer_top_fraction': footer_ink_box['y'] / HEIGHT if footer_ink_box else None,
        'footer_bottom_margin_pixels': HEIGHT - (footer_ink_box['y'] + footer_ink_box['height']) if footer_ink_box else None,
    }
    expected_source_bars = [
        {'x': 101.5, 'y': 551, 'width': 391.5, 'height': 130},
        {'x': 101.5, 'y': 696, 'width': 638, 'height': 130},
        {'x': 101.5, 'y': 841, 'width': 246.5, 'height': 130},
        {'x': 101.5, 'y': 986, 'width': 551, 'height': 130},
    ]
    source_bars_match = len(source_line_boxes) == len(expected_source_bars) and all(
        all(abs(actual[key] - expected[key]) <= 0.01 for key in expected)
        for actual, expected in zip(source_line_boxes, expected_source_bars)
    )
    source_footer_matches = all(abs(source_footer_box[key] - expected) <= 0.01 for key, expected in {'x': 101.5, 'y': 1754.4, 'width': 335, 'height': 90}.items())
    adapted_strip = adapted_clip_geometry['headline_crop_strip']
    adapted_right_edge = adapted_strip['x'] + adapted_strip['width']
    source_right_border = WIDTH - source_panel['x'] - source_panel['width']
    adapted_right_border = WIDTH - adapted_panel['x'] - adapted_panel['width']
    assertions = {
        'source_canvas_1450x2040': source_dimensions == {'width': WIDTH, 'height': HEIGHT, 'viewBox': '0 0 1450 2040'},
        'adapted_canvas_1450x2040': adapted_dimensions == {'width': WIDTH, 'height': HEIGHT, 'viewBox': '0 0 1450 2040'},
        'source_and_adapted_aspect_145_204': abs(source_dimensions['width'] / source_dimensions['height'] - 145 / 204) < 1e-9 and abs(adapted_dimensions['width'] / adapted_dimensions['height'] - 145 / 204) < 1e-9,
        'source_blue_panel_geometry': source_panel == {'x': 826.5, 'y': 0, 'width': 507.5, 'height': 2040},
        'adapted_blue_panel_geometry': adapted_panel == {'x': 826.5, 'y': 0, 'width': 507.5, 'height': 2040},
        'source_and_adapted_right_border_116': source_right_border == 116 and adapted_right_border == 116,
        'source_left_contour_spans_0_04_to_0_73': source_local_contour['y'] <= 0.041 * HEIGHT and source_local_contour['y'] + source_local_contour['height'] >= 0.72 * HEIGHT and source_local_contour['x'] <= 0.19 * WIDTH and abs(source_local_contour['x'] + source_local_contour['width'] - 0.57 * WIDTH) <= 2,
        'source_title_bars_match_visual_estimates': source_bars_match,
        'source_footer_placeholder_at_0_86h': source_footer_matches,
        'adapted_upper_and_lower_local_contours_present': adapted_clip_geometry['upper_local_contour']['y'] <= 0.041 * HEIGHT and adapted_clip_geometry['upper_local_contour']['y'] + adapted_clip_geometry['upper_local_contour']['height'] >= 0.27 * HEIGHT and adapted_clip_geometry['lower_local_contour']['y'] <= 0.65 * HEIGHT and adapted_clip_geometry['lower_local_contour']['y'] + adapted_clip_geometry['lower_local_contour']['height'] >= 0.73 * HEIGHT,
        'adapted_headline_crop_strip_stays_at_x_0_52_to_0_57': adapted_strip['x'] >= 0.52 * WIDTH - 0.01 and adapted_right_edge <= 0.57 * WIDTH + 0.01 and abs(adapted_strip['y'] - 0.27 * HEIGHT) <= 1 and abs(adapted_strip['y'] + adapted_strip['height'] - 0.54 * HEIGHT) <= 1,
        'adapted_upper_direction_cue_at_0_43_0_18': abs(adapted_left_cue['cx'] - 0.43 * WIDTH) <= 1 and abs(adapted_left_cue['cy'] - 0.18 * HEIGHT) <= 1,
        'adapted_title_words_exact_once': title_values == {'title-dream': 'DREAM', 'title-weaver': 'WEAVER', 'adapted-footer': 'ONEIRLOOM'},
        'adapted_title_ink_top_near_0_27h': title_ink_overall is not None and abs(title_ink_metrics['overall_top_fraction'] - 0.27) <= 0.005,
        'adapted_title_ink_height_0_23_to_0_26h': title_ink_overall is not None and 0.23 <= title_ink_metrics['overall_height_fraction'] <= 0.26,
        'adapted_title_ink_line_gap_at_most_0_018h': title_line_gap is not None and 0 <= title_ink_metrics['line_gap_fraction'] <= 0.018,
        'adapted_title_actual_ink_stays_left_of_crop_strip': title_ink_overall is not None and title_ink_overall['x'] + title_ink_overall['width'] <= adapted_strip['x'],
        'adapted_footer_actual_ink_top_near_0_86h': footer_ink_box is not None and abs(title_ink_metrics['footer_top_fraction'] - 0.86) <= 0.005,
        'adapted_footer_has_0_10h_bottom_margin': footer_ink_box is not None and title_ink_metrics['footer_bottom_margin_pixels'] >= 0.1 * HEIGHT,
        'comparison_labels_exact': labels == ['06原图', '原图粗分区（目测）', '织梦兽版式骨架（待主体素材）'],
        'comparison_images_loaded': len(image_states) == 3 and all(entry['loaded'] for entry in image_states),
        'reference_is_original_and_unchanged': reference_dimensions == [145, 204] and reference_hash_before == reference_hash_after,
        'comparison_has_no_horizontal_overflow': preview_geometry['documentWidth'] <= preview_geometry['clientWidth'] == preview_geometry['viewportWidth'],
        'canvas_screenshot_dimensions_exact': output_dimensions['source-layout.png'] == [WIDTH, HEIGHT] and output_dimensions['adapted-layout.png'] == [WIDTH, HEIGHT],
        'page_errors_empty': not page_errors,
    }
    result = {
        'status': 'draft-only; pending Primary visual review',
        'source_faithfulness_approved': False,
        'generation_used': False,
        'rendering': {'browser': 'Microsoft Edge', 'executable': str(EDGE), 'playwright': 'installed Python Playwright', 'source_reference_path': REFERENCE.relative_to(ROOT).as_posix(), 'source_reference_dimensions': reference_dimensions, 'source_reference_sha256_before_and_after': reference_hash_before},
        'canvas': {'width': WIDTH, 'height': HEIGHT, 'aspect': '145:204', 'paper': '#F4F0E8', 'blue_panel': '#4164D8', 'blue_panel_x': 826.5, 'blue_panel_width': 507.5, 'right_paper_border': 116},
        'comparison_labels': labels,
        'source_layout_observations': {'title_bars': 4, 'title_bar_tops': [551, 696, 841, 986], 'title_bar_widths_visual_estimates': [391.5, 638, 246.5, 551], 'title_bar_height_visual_estimate': 130, 'title_bar_coordinates': 'manual visual estimates from the original 145x204 reference, not precise measurements', 'small_copy_bars': 3, 'footer_placeholder_top': 1754.4, 'left_view_shape': 'hand-authored coarse gray contour spanning about y=0.04-0.73h; schematic shape only, not human anatomy or finished subject artwork', 'local_fragment_model': 'five unequal horizontal gray pieces clipped to the local contour; their count is schematic and does not assert original cut count', 'source_coordinate_basis': 'manual visual estimate from the original 145x204 reference'},
        'adapted_layout_choices': {'title': ['DREAM', 'WEAVER'], 'title_change': 'four source title lines reduced to two complete words', 'title_font_size': 300, 'title_text_remains_editable': True, 'omitted_small_copy_areas': 'left blank', 'footer': 'ONEIRLOOM', 'gray_mass': 'schematic low-detail placeholder, not approved subject artwork', 'adapted_crop': 'upper local fur mass, a narrow x=0.52-0.57h strip beside the headline, and a lower x=0.52-0.57h contour near the splice; no full-body or limb depiction', 'layout_coordinates': 'draft choices for review'},
        'measurements': {'source_canvas': source_dimensions, 'adapted_canvas': adapted_dimensions, 'source_blue_panel': source_panel, 'adapted_blue_panel': adapted_panel, 'source_left_local_contour_svg_geometry': source_local_contour, 'source_title_placeholder_boxes': source_line_boxes, 'source_footer_placeholder_svg_geometry': source_footer_box, 'adapted_local_crop_svg_geometry': adapted_clip_geometry, 'adapted_left_direction_cue_center': {'x': adapted_left_cue['cx'], 'y': adapted_left_cue['cy']}, 'adapted_svg_dom_boxes_not_actual_ink': svg_dom_boxes_not_actual_ink, 'adapted_actual_ink_pixel_bounds': title_ink_metrics, 'preview': preview_geometry, 'image_loads': image_states, 'screenshot_dimensions': output_dimensions, 'page_errors': page_errors},
        'checks': assertions,
        'all_checks_passed': all(assertions.values()),
    }
    (PROOF / 'checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    if not result['all_checks_passed']:
        raise RuntimeError(json.dumps({'failed_checks': [name for name, passed in assertions.items() if not passed], 'measurements': result['measurements']}, ensure_ascii=False))
    print(json.dumps({'all_checks_passed': True, 'screenshots': output_dimensions, 'adapted_actual_ink': title_ink_metrics, 'checks': len(assertions)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
