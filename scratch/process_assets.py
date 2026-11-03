from PIL import Image, ImageDraw
import os

base = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"

# 1. Inspect 4-BOD.jpg dimensions and crop the 4 portraits cleanly
bod_path = os.path.join(base, "spillburg logistics", "assets", "4-BOD.jpg")
bod = Image.open(bod_path)
w, h = bod.size
print(f"4-BOD.jpg size: {w}x{h}")

# In 4-BOD.jpg (1000x1403):
# Let's find the exact bounding boxes of the 4 rounded-square blue-background portraits in the top row
# Looking at the image: y is roughly 14% to 29% of height, x is 4 columns across width
# Let's scan pixel rows/cols to find the exact portrait boxes or crop generously inside each portrait frame
# Portrait 1 (Hameez): x ~ 32..213, y ~ 205..406
# Portrait 2 (Shaameel): x ~ 286..467, y ~ 205..406
# Portrait 3 (Razik): x ~ 540..721, y ~ 205..406
# Portrait 4 (Mafaz): x ~ 787..968, y ~ 205..406
log_assets = os.path.join(base, "spillburg logistics", "assets")
corp_assets = os.path.join(base, "spillburg corporate services", "assets")

# Copy high-res Hameez and Shaameel from corporate to logistics, and also crop Razik and Mafaz from 4-BOD.jpg
import shutil
shutil.copyfile(os.path.join(corp_assets, "dir_hameez.jpg"), os.path.join(log_assets, "dir_hameez.jpg"))
shutil.copyfile(os.path.join(corp_assets, "dir_shaameel.jpg"), os.path.join(log_assets, "dir_shaameel.jpg"))

# Also copy Razik to corporate services in case we feature him on Corporate Services advisory board too!
razik_box = (int(w * 0.542), int(h * 0.148), int(w * 0.720), int(h * 0.288))
mafaz_box = (int(w * 0.789), int(h * 0.148), int(w * 0.967), int(h * 0.288))

razik_img = bod.crop(razik_box)
mafaz_img = bod.crop(mafaz_box)
razik_img.save(os.path.join(log_assets, "dir_razik.jpg"), quality=95)
mafaz_img.save(os.path.join(log_assets, "dir_mafaz.jpg"), quality=95)
razik_img.save(os.path.join(corp_assets, "dir_razik.jpg"), quality=95)
print("Cropped dir_razik.jpg and dir_mafaz.jpg")

# 2. Create white-wordmark versions of Corporate Services and Logistics logos for dark headers/covers
# Corporate Services logo: logo_corporate.png (2439x768)
corp_logo = Image.open(os.path.join(corp_assets, "logo_corporate.png")).convert("RGBA")
cw, ch = corp_logo.size
print(f"corp_logo size: {cw}x{ch}")
# In logo_corporate.png, left ~33% (x < cw*0.34) is the emblem (navy + medium blue), right ~66% (x >= cw*0.34) is the text "SPILLBURG CORPORATE SERVICES"
# For dark backgrounds, let's make a version where the dark navy pixels in the text (and dark spades) are lightened/whitened, while the medium cobalt/blue stays vibrant!
corp_white = corp_logo.copy()
pixels = corp_white.load()
for y in range(ch):
    for x in range(cw):
        r, g, b, a = pixels[x, y]
        if a > 20:
            # If it's on the text side (x > cw * 0.34): make "SPILLBURG" white and "CORPORATE SERVICES" ice-gold/silver
            if x > int(cw * 0.34):
                if y < int(ch * 0.62):
                    pixels[x, y] = (255, 255, 255, a)
                else:
                    pixels[x, y] = (212, 175, 55, a)  # Subtle champagne gold for "CORPORATE SERVICES"
            else:
                # In the emblem, if it's very dark navy (r < 20, g < 45, b < 85), turn it into crisp white so the 3-spade emblem pops on dark navy backgrounds!
                if b < 90 and r < 30:
                    pixels[x, y] = (255, 255, 255, a)
                else:
                    # Brighten the cobalt blue slightly for dark background contrast
                    pixels[x, y] = (min(255, r + 40), min(255, g + 65), min(255, b + 85), a)
corp_white.save(os.path.join(corp_assets, "logo_corporate_white.png"))
print("Saved logo_corporate_white.png")

# Logistics logo: logo_logistics_live.png (348x82)
log_logo = Image.open(os.path.join(log_assets, "logo_logistics_live.png")).convert("RGBA")
lw, lh = log_logo.size
print(f"log_logo size: {lw}x{lh}")
# Let's also crop just the ship icon (x < lw*0.24) as icon_logistics.png
icon_log = log_logo.crop((0, 0, int(lw * 0.24), lh))
icon_log.save(os.path.join(log_assets, "icon_logistics.png"))

# Create logo_logistics_white.png where the black text "SPILLBURG LOGISTICS 1" (x > lw*0.24 and dark pixels) becomes crisp white, and white background (if any) is transparent
log_white = log_logo.copy()
lpix = log_white.load()
for y in range(lh):
    for x in range(lw):
        r, g, b, a = lpix[x, y]
        if a > 20:
            if x > int(lw * 0.24):
                # If pixel is dark (the black text "SPILLBURG LOGISTICS 1")
                if r < 80 and g < 80 and b < 80:
                    lpix[x, y] = (255, 255, 255, a)
                elif b > 150 and r < 80:
                    # The blue "PRIVATE LIMITED" -> make it bright sky cyan so it pops on dark navy
                    lpix[x, y] = (56, 189, 248, a)
            else:
                # In the icon, if dark navy ship body, brighten slightly or keep crisp
                if r < 50 and g < 90 and b < 160 and a > 100:
                    lpix[x, y] = (186, 230, 253, a)
log_white.save(os.path.join(log_assets, "logo_logistics_white.png"))
print("Saved logo_logistics_white.png and icon_logistics.png")

# 3. Color-accent the 3 QR codes so the corner finder patterns feature the brand's secondary accent color!
qr_configs = [
    {
        "path": os.path.join(base, "destination consultancy", "assets", "qr_website.png"),
        "fg": (7, 30, 43),        # Deep Petrol #071E2B
        "accent": (184, 137, 42), # Warm Gold #B8892A
        "bg": (255, 253, 247),
    },
    {
        "path": os.path.join(base, "spillburg corporate services", "assets", "qr_website.png"),
        "fg": (0, 0, 77),         # Deep Royal Navy #00004D
        "accent": (23, 61, 237),  # Electric Cobalt #173DED
        "bg": (248, 250, 255),
    },
    {
        "path": os.path.join(base, "spillburg logistics", "assets", "qr_website.png"),
        "fg": (15, 23, 42),       # Midnight Navy #0F172A
        "accent": (2, 132, 199),  # Maritime Blue #0284C7
        "bg": (248, 250, 252),
    }
]

for qc in qr_configs:
    qimg = Image.open(qc["path"]).convert("RGBA")
    qw, qh = qimg.size
    qpix = qimg.load()
    # Find bounding box of dark modules
    min_x, min_y, max_x, max_y = qw, qh, 0, 0
    for y in range(qh):
        for x in range(qw):
            r, g, b, a = qpix[x, y]
            if r < 150 and g < 150:
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y
    span = max_x - min_x + 1
    # A standard QR code finder pattern is 7 modules wide out of ~29-33 modules (~24% of span)
    finder_size = int(span * 0.255)
    for y in range(qh):
        for x in range(qw):
            r, g, b, a = qpix[x, y]
            if r < 150 and g < 150:
                in_tl = (x <= min_x + finder_size) and (y <= min_y + finder_size)
                in_tr = (x >= max_x - finder_size) and (y <= min_y + finder_size)
                in_bl = (x <= min_x + finder_size) and (y >= max_y - finder_size)
                if in_tl or in_tr or in_bl:
                    qpix[x, y] = qc["accent"] + (255,)
                else:
                    qpix[x, y] = qc["fg"] + (255,)
    qimg.save(qc["path"], "PNG")
    print(f"Enhanced dual-tone branded QR code -> {qc['path']}")

