import urllib.request
import ssl
import re
import json
import os
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_ignore = False
        self.texts = []
        self.links = []
        self.imgs = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self.in_ignore = True
        attrs_dict = dict(attrs)
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append(attrs_dict['href'])
        if tag == 'img' and 'src' in attrs_dict:
            self.imgs.append(attrs_dict['src'])
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript'):
            self.in_ignore = False
    def handle_data(self, data):
        if not self.in_ignore:
            s = data.strip()
            if s:
                self.texts.append(s)

def parse_html(html_str):
    p = TextExtractor()
    p.feed(html_str)
    return "\n".join(p.texts), p.links, p.imgs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def fetch_bytes(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
        return resp.read()

# 1. Fetch Destination Consultancy JS bundle & CSS
print("=== 1. DESTINATION CONSULTANCY JS BUNDLE ===")
dest_js = fetch_bytes("https://www.destinationconsultancy.com/assets/index-DifLhCmz.js").decode('utf-8', errors='ignore')
with open("scratch/site_dumps/destination_bundle.js", "w", encoding="utf-8") as f:
    f.write(dest_js)

dest_css = fetch_bytes("https://www.destinationconsultancy.com/assets/index-CaYHktaR.css").decode('utf-8', errors='ignore')
with open("scratch/site_dumps/destination_bundle.css", "w", encoding="utf-8") as f:
    f.write(dest_css)

dest_assets = re.findall(r'["\']([^"\']+\.(?:png|jpg|jpeg|svg|webp|avif|ico|pdf))["\']', dest_js)
print("Destination asset paths:", set(dest_assets))

# Extract strings from dest_js
strings = re.findall(r'["\']([^"\']{8,600})["\']', dest_js)
filtered_strings = [s for s in strings if not s.startswith(('http://www.w3.org', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M0', 'flex ', 'grid ', 'relative ', 'absolute ', 'bg-', 'text-', 'border-', 'rounded-', 'px-', 'py-', 'transition'))]
with open("scratch/site_dumps/destination_extracted.txt", "w", encoding="utf-8") as f:
    for s in filtered_strings:
        f.write(s + "\n")
print(f"Saved {len(filtered_strings)} strings from destination_bundle.js")

# 2. Parse Corporate Services HTML files
print("\n=== 2. SPILLBURG CORPORATE SERVICES ===")
corp_texts = []
corp_all_imgs = set()
for fn in sorted(os.listdir("scratch/site_dumps")):
    if fn.startswith("corporate_") and fn.endswith(".html"):
        with open(os.path.join("scratch/site_dumps", fn), "r", encoding="utf-8") as f:
            txt, links, imgs = parse_html(f.read())
            corp_all_imgs.update(imgs)
            corp_texts.append(f"--- FILE: {fn} ---\n{txt}\n")

print("Corporate Services images:", sorted(list(corp_all_imgs)))
with open("scratch/site_dumps/corporate_extracted.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(corp_texts))
print("Saved corporate_extracted.txt")

# 3. Parse Logistics HTML file
print("\n=== 3. SPILLBURG LOGISTICS 1 (LIVE SITE) ===")
with open("scratch/site_dumps/logistics_home.html", "r", encoding="utf-8") as f:
    txt, log_links, log_imgs = parse_html(f.read())
    print("Logistics live links:", sorted(list(set(log_links))))
    print("Logistics live imgs:", sorted(list(set(log_imgs))))
    with open("scratch/site_dumps/logistics_extracted.txt", "w", encoding="utf-8") as out:
        out.write(txt)

# 4. Parse Holdings HTML files
print("\n=== 4. SPILLBURG HOLDINGS (LIVE SITE) ===")
hold_texts = []
for fn in sorted(os.listdir("scratch/site_dumps")):
    if fn.startswith("holdings_") and fn.endswith(".html"):
        with open(os.path.join("scratch/site_dumps", fn), "r", encoding="utf-8") as f:
            txt, links, imgs = parse_html(f.read())
            hold_texts.append(f"--- FILE: {fn} ---\n{txt}\n")
with open("scratch/site_dumps/holdings_extracted.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(hold_texts))
print("Saved holdings_extracted.txt")
