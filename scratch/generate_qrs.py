import os
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"

# Let's check if qrcode + PIL are available, otherwise use api.qrserver.com with custom hex colors and PIL post-processing
try:
    import qrcode
    from PIL import Image, ImageDraw
    HAS_QRCODE = True
except ImportError:
    HAS_QRCODE = False

print("HAS_QRCODE:", HAS_QRCODE)

configs = [
    {
        "folder": "destination consultancy",
        "url": "https://www.destinationconsultancy.com",
        "fg": "071E2B",      # Deep Petrol Teal
        "bg": "FFFDF7",      # Warm Ivory
        "accent": (184, 137, 42),  # Warm Gold #B8892A
        "fg_rgb": (7, 30, 43),
        "bg_rgb": (255, 253, 247),
    },
    {
        "folder": "spillburg corporate services",
        "url": "https://www.spillburgcorporate.com",
        "fg": "00004D",      # Deep Royal Navy
        "bg": "F8FAFF",      # Crisp Ice White
        "accent": (23, 61, 237),   # Electric Cobalt #173DED
        "fg_rgb": (0, 0, 77),
        "bg_rgb": (248, 250, 255),
    },
    {
        "folder": "spillburg logistics",
        "url": "https://www.spillburglogistics1.com",
        "fg": "0F172A",      # Midnight Navy
        "bg": "F8FAFC",      # Slate White
        "accent": (2, 132, 199),   # Maritime Cyan/Blue #0284C7
        "fg_rgb": (15, 23, 42),
        "bg_rgb": (248, 250, 252),
    }
]

for cfg in configs:
    out_path = os.path.join(base, cfg["folder"], "assets", "qr_website.png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if HAS_QRCODE:
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=14,
            border=2,
        )
        qr.add_data(cfg["url"])
        qr.make(fit=True)
        img = qr.make_image(fill_color=cfg["fg_rgb"], back_color=cfg["bg_rgb"]).convert("RGBA")
        # Color the 3 finder patterns with the accent color for a bespoke branded look
        matrix = qr.get_matrix()
        n = len(matrix)
        box = 14
        border = 2
        draw = ImageDraw.Draw(img)
        # Finder pattern coordinates in matrix (excluding border):
        # top-left: (0..6, 0..6), top-right: (0..6, n-7..n-1), bottom-left: (n-7..n-1, 0..6)
        finders = [(0, 0), (0, n - 7), (n - 7, 0)]
        for r0, c0 in finders:
            for dr in range(7):
                for dc in range(7):
                    if matrix[r0 + dr + border][c0 + dc + border]:
                        # Outer ring (dr in (0,6) or dc in (0,6)) -> fg_rgb, inner 3x3 (2..4, 2..4) -> accent
                        is_center = (2 <= dr <= 4) and (2 <= dc <= 4)
                        color = cfg["accent"] if is_center else cfg["fg_rgb"]
                        x0 = (c0 + dc + border) * box
                        y0 = (r0 + dr + border) * box
                        draw.rectangle([x0, y0, x0 + box - 1, y0 + box - 1], fill=color + (255,))
        img.save(out_path, "PNG")
        print(f"Generated custom QR with qrcode+PIL -> {out_path}")
    else:
        api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={ urllib.parse.quote(cfg['url']) }&color={cfg['fg']}&bgcolor={cfg['bg']}&margin=10&ecc=H"
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            data = r.read()
        with open(out_path, "wb") as f:
            f.write(data)
        try:
            from PIL import Image, ImageDraw
            img = Image.open(out_path).convert("RGBA")
            # Also save cleanly
            img.save(out_path, "PNG")
        except Exception as e:
            pass
        print(f"Generated custom QR via API -> {out_path}")

