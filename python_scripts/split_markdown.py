import os
import glob
import re

def sanitize_heading(text):
    return text.replace('/', '-').replace('\\', '-').strip()

def split_md(md_path):
    name = os.path.splitext(os.path.basename(md_path))[0]
    out_dir = os.path.join('outputs', name)
    os.makedirs(out_dir, exist_ok=True)

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Split into sections on ## headings
    sections = []  # list of (heading_text, lines)
    current_heading = None
    current_lines = []

    for line in lines:
        if line.startswith('## '):
            if current_heading is not None:
                sections.append((current_heading, current_lines))
            current_heading = line[3:].strip()
            current_lines = [line]
        else:
            if current_heading is not None:
                current_lines.append(line)
            # else: content before first ## — ignore per spec

    if current_heading is not None:
        sections.append((current_heading, current_lines))

    if not sections:
        # No ## headings — copy unchanged with warning
        import shutil
        dest = os.path.join(out_dir, os.path.basename(md_path))
        shutil.copy2(md_path, dest)
        print(f'WARNING: No ## headings found in {md_path!r} — copied unchanged.')
        return 0

    pad = 3 if len(sections) > 99 else 2
    name_prefix = name[:10]

    for i, (heading, sec_lines) in enumerate(sections, 1):
        counter = str(i).zfill(pad)
        safe_heading = sanitize_heading(heading)
        filename = f'{counter} {name_prefix} - {safe_heading}.md'
        out_path = os.path.join(out_dir, filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.writelines(sec_lines)

    return len(sections)

def main():
    mds = sorted(glob.glob('inputs/*.md'))
    if not mds:
        print('No .md files found in inputs/')
        return

    total_files = 0
    total_sections = 0
    for md_path in mds:
        try:
            n = split_md(md_path)
            total_files += 1
            total_sections += n
        except Exception as e:
            print(f'ERROR skipping {md_path}: {e}')

    print(f'Processed: {total_files} files | Sections written: {total_sections}')

if __name__ == '__main__':
    main()
