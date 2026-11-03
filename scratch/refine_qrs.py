import urllib.request
import urllib.parse
import ssl
import os
from PIL import Image

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"

configs = [
    {
        "folder": "destination consultancy",
        "url": "https://www.destinationconsultancy.com",
        "fg_hex": "071E2B",
        "bg_hex": "FFFDF7",
        "fg": (7, 30, 43),
        "accent": (197, 155, 39),  # Gold #C59B27
    },
    {
        "folder": "spillburg corporate services",
        "url": "https://www.spillburgcorporate.com",
        "fg_hex": "00004D",
        "bg_hex": "F8FAFF",
        "fg": (0, 0, 77),
        "accent": (23, 61, 237),   # Cobalt #173DED
    },
    {
        "folder": "spillburg logistics",
        "url": "https://www.spillburglogistics1.com",
        "fg_hex": "0F172A",
        "bg_hex": "F8FAFC",
        "fg": (15, 23, 42),
        "accent": (2, 132, 199),   # Maritime Blue #0284C7
    }
]

for cfg in configs:
    out_path = os.path.join(base, cfg["folder"], "assets", "qr_website.png")
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={urllib.parse.quote(cfg['url'])}&color={cfg['fg_hex']}&bgcolor={cfg['bg_hex']}&margin=12&ecc=M"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
        data = r.read()
    with open(out_path, "wb") as f:
        f.write(data)

    qimg = Image.open(out_path).convert("RGBA")
    qw, qh = qimg.size
    qpix = qimg.load()
    min_x, min_y, max_x, max_y = qw, qh, 0, 0
    for y in range(qh):
        for x in range(qw):
            r, g, b, a = qpix[x, y]
            if r < 140 and g < 140:
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y

    # Find exact width of top-left finder outer top bar by scanning horizontally from (min_x, min_y) until a light pixel is hit!
    finder_w = 0
    for x in range(min_x, max_x + 1):
        r, g, b, a = qpix[x, min_y + 2]
        if r < 140 and g < 140:
            finder_w = x - min_x + 1
        else:
            break
    print(f"{cfg['folder']}: span={max_x - min_x + 1}, exact finder_w={finder_w}")

    for y in range(qh):
        for x in range(qw):
            r, g, b, a = qpix[x, y]
            if r < 140 and g < 140:
                in_tl = (x <= min_x + finder_w) and (y <= min_y + finder_w)
                in_tr = (x >= max_x - finder_w) and (y <= min_y + finder_w)
                in_bl = (x <= min_x + finder_w) and (y >= max_y - finder_w)
                if in_tl or in_tr or in_bl:
                    qpix[x, y] = cfg["accent"] + (255,)
                else:
                    qpix[x, y] = cfg["fg"] + (255,)
    qimg.save(out_path, "PNG")

