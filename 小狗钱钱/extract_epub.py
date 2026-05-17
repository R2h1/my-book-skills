import zipfile, re, html, os, sys

# Set console encoding for Chinese
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dir_path = os.path.dirname(os.path.abspath(__file__))
for f in os.listdir(dir_path):
    if f.endswith('.epub'):
        epub_path = os.path.join(dir_path, f)
        print(f'Found EPUB: {f}', file=sys.stderr)
        break

epub = zipfile.ZipFile(epub_path, 'r')
texts = []
for n in epub.namelist():
    if n.endswith('.html') or n.endswith('.xhtml'):
        raw = epub.read(n).decode('utf-8', errors='replace')
        clean = html.unescape(re.sub('<[^>]+>', '', raw))
        clean = re.sub(r'\s+', ' ', clean).strip()
        if clean:
            texts.append(clean)

full_text = '\n\n'.join(texts)
print(f'Total chars: {len(full_text)}', file=sys.stderr)

out_path = os.path.join(dir_path, '小狗钱钱_自清.txt')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_text)
print(f'Saved to: {out_path}', file=sys.stderr)
print(full_text[:3000])
