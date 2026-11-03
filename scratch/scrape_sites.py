import urllib.request
import ssl
import re
from urllib.parse import urljoin, urlparse
import json
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

sites = {
    'destination': 'https://www.destinationconsultancy.com',
    'corporate': 'https://www.spillburgcorporate.com',
    'logistics': 'https://www.spillburglogistics1.com',
    'holdings': 'https://www.spillburg.com'
}

os.makedirs("scratch/site_dumps", exist_ok=True)

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
        return resp.read().decode('utf-8', errors='ignore')

for name, base_url in sites.items():
    print(f"=== Fetching {name}: {base_url} ===")
    try:
        html = fetch(base_url)
        with open(f"scratch/site_dumps/{name}_home.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        # Find internal links
        links = set(re.findall(r'href=["\']([^"\']+)["\']', html))
        imgs = set(re.findall(r'src=["\']([^"\']+)["\']', html))
        print(f"Found {len(links)} links, {len(imgs)} images on {name} home")
        
        internal_links = set()
        for l in links:
            full = urljoin(base_url, l)
            if urlparse(full).netloc == urlparse(base_url).netloc and not any(full.lower().endswith(ext) for ext in ['.css', '.js', '.png', '.jpg', '.jpeg', '.svg', '.ico', '.woff', '.woff2', '.ttf']):
                internal_links.add(full.split('#')[0])
        
        print(f"Internal pages for {name}: {internal_links}")
        for idx, page_url in enumerate(sorted(internal_links)[:20]):
            if page_url.rstrip('/') == base_url.rstrip('/'):
                continue
            try:
                p_html = fetch(page_url)
                slug = re.sub(r'[^a-zA-Z0-9]+', '_', urlparse(page_url).path.strip('/')) or f"sub_{idx}"
                with open(f"scratch/site_dumps/{name}_{slug}.html", "w", encoding="utf-8") as f:
                    f.write(p_html)
                p_imgs = set(re.findall(r'src=["\']([^"\']+)["\']', p_html))
                imgs.update(p_imgs)
                print(f"  Fetched {page_url} ({len(p_html)} bytes)")
            except Exception as e:
                print(f"  Failed {page_url}: {e}")
        
        with open(f"scratch/site_dumps/{name}_images.json", "w", encoding="utf-8") as f:
            json.dump(sorted(list(imgs)), f, indent=2)
    except Exception as e:
        print(f"Error on {name}: {e}")

