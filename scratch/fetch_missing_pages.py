import urllib.request
import ssl
import os
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_ignore = False
        self.texts = []
        self.imgs = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self.in_ignore = True
        attrs_dict = dict(attrs)
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
    return "\n".join(p.texts), p.imgs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}

def fetch_text(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
        return resp.read().decode('utf-8', errors='ignore')

log_urls = [
    'https://spillburglogistics1.com/',
    'https://spillburglogistics1.com/about-us/',
    'https://spillburglogistics1.com/services/',
    'https://spillburglogistics1.com/contact-us/',
    'https://spillburglogistics1.com/news-updates/',
    'https://spillburglogistics1.com/air-freight/',
    'https://spillburglogistics1.com/land-freight/',
    'https://spillburglogistics1.com/sea-freight/',
    'https://spillburglogistics1.com/warehousing/',
    'https://spillburglogistics1.com/?page_id=11',
]

log_all_text = []
log_all_imgs = set()
for u in log_urls:
    try:
        html = fetch_text(u)
        txt, imgs = parse_html(html)
        log_all_imgs.update(imgs)
        log_all_text.append(f"=== URL: {u} ===\n{txt}\n")
        print(f"Fetched {u} ({len(txt)} chars, {len(imgs)} imgs)")
    except Exception as e:
        print(f"Failed {u}: {e}")

with open("scratch/site_dumps/logistics_all_pages.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log_all_text))

print("All logistics images:", sorted(list(log_all_imgs)))

corp_extra_urls = [
    'https://www.spillburgcorporate.com/en/success-stories',
    'https://www.spillburgcorporate.com/en/services/payroll-and-hr',
    'https://www.spillburgcorporate.com/en/services/stock-market-listing',
    'https://www.spillburgcorporate.com/en/services/taxation',
]
corp_extra_text = []
for u in corp_extra_urls:
    try:
        html = fetch_text(u)
        txt, imgs = parse_html(html)
        corp_extra_text.append(f"=== URL: {u} ===\n{txt}\n")
        print(f"Fetched {u} ({len(txt)} chars)")
    except Exception as e:
        print(f"Failed {u}: {e}")

with open("scratch/site_dumps/corporate_extra_pages.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(corp_extra_text))

