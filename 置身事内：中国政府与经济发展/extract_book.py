#!/usr/bin/env python3
"""Extract text from the EPUB book."""
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import html2text
import sys
import os

book_path = os.path.join(os.path.dirname(__file__),
    '置身事内：中国政府与经济发展 (兰小欢) (z-library.sk, 1lib.sk, z-lib.sk).epub')
output_path = os.path.join(os.path.dirname(__file__), 'book_text.txt')

book = epub.read_epub(book_path)

converter = html2text.HTML2Text()
converter.ignore_links = True
converter.ignore_images = True
converter.ignore_emphasis = False

items = list(book.get_items())
print(f"Total items: {len(items)}")

text_content = []
for i, item in enumerate(items):
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        # Remove script and style
        for tag in soup(['script', 'style', 'nav']):
            tag.decompose()
        text = converter.handle(str(soup))
        if text.strip():
            text_content.append(text.strip())
            # Print progress
            title = soup.find('title')
            title_text = title.get_text() if title else f'chapter_{i}'
            print(f"  [{i}] Extracted: {title_text[:60]}... ({len(text)} chars)")

full_text = '\n\n---\n\n'.join(text_content)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

char_count = len(full_text)
print(f"\nDone! Total characters: {char_count}")
print(f"Output: {output_path}")
