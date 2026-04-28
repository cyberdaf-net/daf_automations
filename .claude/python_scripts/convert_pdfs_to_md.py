import fitz
import pytesseract
from PIL import Image
import io
import os
import glob
from collections import Counter

def modal_font_size(page):
    sizes = []
    blocks = page.get_text('dict')['blocks']
    for block in blocks:
        if block['type'] == 0:
            for line in block.get('lines', []):
                for span in line.get('spans', []):
                    size = round(span['size'], 1)
                    sizes.append(size)
    if not sizes:
        return 12.0
    return Counter(sizes).most_common(1)[0][0]

def process_pdf(pdf_path):
    name = os.path.splitext(os.path.basename(pdf_path))[0]
    out_dir = os.path.join('outputs', name)
    attach_dir = os.path.join(out_dir, 'attachments')
    os.makedirs(out_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    md_lines = []
    fig_count = 0
    ocr_count = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        baseline = modal_font_size(page)
        blocks = page.get_text('dict')['blocks']
        blocks_sorted = sorted(blocks, key=lambda b: (round(b['bbox'][1], 1), round(b['bbox'][0], 1)))

        for block in blocks_sorted:
            if block['type'] == 0:  # text
                for line in block.get('lines', []):
                    line_text = ''
                    line_size = None
                    for span in line.get('spans', []):
                        text = span['text'].strip()
                        if text:
                            line_text += span['text']
                            if line_size is None:
                                line_size = span['size']
                    line_text = line_text.strip()
                    if not line_text:
                        continue
                    if line_size and line_size >= baseline * 1.4:
                        md_lines.append(f'## {line_text}')
                    elif line_size and line_size >= baseline * 1.15:
                        md_lines.append(f'### {line_text}')
                    else:
                        md_lines.append(line_text)

            elif block['type'] == 1:  # image
                bbox = block['bbox']
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]
                if w < 50 or h < 50:
                    continue

                fig_count += 1
                os.makedirs(attach_dir, exist_ok=True)
                fig_filename = f'{name}-figure-{fig_count}.png'
                fig_path = os.path.join(attach_dir, fig_filename)

                # Extract image via page clip
                clip = fitz.Rect(bbox)
                mat = fitz.Matrix(2, 2)
                pix = page.get_pixmap(matrix=mat, clip=clip)
                pix.save(fig_path)

                # OCR
                img = Image.open(fig_path)
                ocr_text = pytesseract.image_to_string(img).strip()
                if ocr_text:
                    ocr_count += 1

                md_lines.append(f'![[attachments/{fig_filename}]]')
                if ocr_text:
                    quoted = '\n'.join(f'> {line}' for line in ocr_text.splitlines())
                    md_lines.append(quoted)
                    # md_lines.append(ocr_text)

        md_lines.append('')  # page separator blank line

    md_path = os.path.join(out_dir, f'{name}.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))

    return fig_count, ocr_count

def main():
    pdfs = sorted(glob.glob('inputs/*.pdf'))
    if not pdfs:
        print('No PDFs found in inputs/')
        return

    total_processed = 0
    total_images = 0
    total_ocr = 0
    skipped = []

    for pdf_path in pdfs:
        try:
            imgs, ocrd = process_pdf(pdf_path)
            total_processed += 1
            total_images += imgs
            total_ocr += ocrd
        except Exception as e:
            skipped.append(f'{os.path.basename(pdf_path)}: {e}')
            print(f'ERROR skipping {pdf_path}: {e}')

    skip_str = ''
    if skipped:
        skip_str = ' (' + ', '.join(skipped) + ')'
    print(f'Processed: {total_processed} | Images: {total_images} | OCR\'d: {total_ocr} | Skipped: {len(skipped)}{skip_str}')

if __name__ == '__main__':
    main()
