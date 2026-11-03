import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def download(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    with open(path, 'wb') as f:
        f.write(data)
    print(f"Downloaded {url} -> {path} ({len(data)} bytes)")

base = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"

# 1. Destination Consultancy assets
dest_assets = os.path.join(base, "destination consultancy", "assets")
download("https://www.destinationconsultancy.com/assets/logo-white-ClcGKSp3.png", os.path.join(dest_assets, "logo_white.png"))
download("https://www.destinationconsultancy.com/assets/icon-compass-CMUhVVg5.png", os.path.join(dest_assets, "icon_compass.png"))
download("https://www.destinationconsultancy.com/images/directors/shaameel-mohideen.jpg", os.path.join(dest_assets, "dir_shaameel.jpg"))
download("https://www.destinationconsultancy.com/images/directors/azad-hamdoon.jpg", os.path.join(dest_assets, "dir_azad.jpg"))
download("https://www.destinationconsultancy.com/images/directors/faazil-ibrahim.jpg", os.path.join(dest_assets, "dir_faazil.jpg"))
download("https://www.destinationconsultancy.com/images/directors/eardley-kern.jpg", os.path.join(dest_assets, "dir_eardley.jpg"))

# 2. Spillburg Corporate Services assets
corp_assets = os.path.join(base, "spillburg corporate services", "assets")
download("https://www.spillburgcorporate.com/spillburg-cs-logo.png", os.path.join(corp_assets, "logo_corporate.png"))
download("https://www.spillburgcorporate.com/icon.png", os.path.join(corp_assets, "icon_corporate.png"))
download("https://www.spillburgcorporate.com/team/m-h-k-m-hameez.jpg", os.path.join(corp_assets, "dir_hameez.jpg"))
download("https://www.spillburgcorporate.com/team/jp-shaameel-mohideen.jpg", os.path.join(corp_assets, "dir_shaameel.jpg"))
for partner in ["agoda", "balaji", "royalty", "amtrad", "umms"]:
    download(f"https://www.spillburgcorporate.com/partners/{partner}.png", os.path.join(corp_assets, f"partner_{partner}.png"))

# 3. Spillburg Logistics 1 assets
log_assets = os.path.join(base, "spillburg logistics", "assets")
download("https://spillburglogistics1.com/wp-content/uploads/2021/01/new-logo.png", os.path.join(log_assets, "logo_logistics_live.png"))
download("https://spillburglogistics1.com/wp-content/uploads/2021/01/bglogo.png", os.path.join(log_assets, "logo_logistics_bg.png"))
download("https://spillburglogistics1.com/wp-content/uploads/2021/03/4-BOD.jpg", os.path.join(log_assets, "4-BOD.jpg"))

