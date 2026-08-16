# -*- coding: utf-8 -*-
"""抽取 epub 正文为纯文本（按 OPF spine 阅读顺序）。"""
import zipfile, re, html, os, sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dir_path = os.path.dirname(os.path.abspath(__file__))
epub_path = None
for f in os.listdir(dir_path):
    if f.endswith('.epub'):
        epub_path = os.path.join(dir_path, f)
        print(f'Found EPUB: {f}', file=sys.stderr)
        break
if not epub_path:
    sys.exit('No epub found')

epub = zipfile.ZipFile(epub_path, 'r')
names = epub.namelist()

def strip_html(raw):
    raw = re.sub(r'<script[^>]*>.*?</script>', '', raw, flags=re.S | re.I)
    raw = re.sub(r'<style[^>]*>.*?</style>', '', raw, flags=re.S | re.I)
    raw = re.sub(r'<br\s*/?>', '\n', raw, flags=re.I)
    raw = re.sub(r'</p>|</div>|</h[1-6]>|</li>', '\n', raw, flags=re.I)
    clean = html.unescape(re.sub('<[^>]+>', '', raw))
    clean = re.sub(r'[ \t\u3000]+', ' ', clean)
    clean = re.sub(r'\n\s*\n+', '\n\n', clean).strip()
    return clean

# 找 OPF
opf_name = None
for n in names:
    if n.endswith('.opf'):
        opf_name = n
        break
print(f'OPF: {opf_name}', file=sys.stderr)

order = []
if opf_name:
    opf = epub.read(opf_name).decode('utf-8', errors='replace')
    m = re.search(r'<manifest[^>]*>(.*?)</manifest>', opf, flags=re.S)
    id2href = {}
    if m:
        for idm in re.finditer(r'<item[^>]+>', m.group(1)):
            tag = idm.group(0)
            iid = re.search(r'id="([^"]+)"', tag)
            href = re.search(r'href="([^"]+)"', tag)
            media = re.search(r'media-type="([^"]+)"', tag)
            if iid and href and media and ('html' in media.group(1).lower()):
                id2href[iid.group(1)] = href.group(1)
    sm = re.search(r'<spine[^>]*>(.*?)</spine>', opf, flags=re.S)
    if sm:
        for it in re.finditer(r'<itemref[^>]+>', sm.group(1)):
            tag = it.group(0)
            ref = re.search(r'idref="([^"]+)"', tag)
            if ref and ref.group(1) in id2href:
                order.append(id2href[ref.group(1)])

# 回退: 按 zip 顺序取所有 html
if not order:
    order = [n for n in names if n.endswith(('.html', '.xhtml'))]

# 相对 opf 目录解析路径
base = os.path.dirname(opf_name) if opf_name else ''
seen = set()
parts = []
for href in order:
    full = os.path.normpath(os.path.join(base, href)).replace('\\', '/')
    if full in names:
        key = full
    else:
        # 尝试文件名匹配
        candidates = [n for n in names if n.endswith(href)]
        key = candidates[0] if candidates else None
    if key and key not in seen:
        seen.add(key)
        raw = epub.read(key).decode('utf-8', errors='replace')
        clean = strip_html(raw)
        if clean:
            parts.append(clean)

full_text = '\n\n'.join(parts)
print(f'Total chars: {len(full_text)}, parts: {len(parts)}', file=sys.stderr)

out_path = os.path.join(dir_path, 'full_text.txt')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_text)
print(f'Saved to: {out_path}', file=sys.stderr)
