import os
import pymupdf

BASE_DIR = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"
DOCS_IMG_DIR = os.path.join(BASE_DIR, "docs", "screenshots")
os.makedirs(DOCS_IMG_DIR, exist_ok=True)

PROFILES = {
    "holdings": os.path.join(BASE_DIR, "spillburg holdings", "v3", "Company Profile - 2026.pdf"),
    "destination": os.path.join(BASE_DIR, "destination consultancy", "Company Profile - 2026.pdf"),
    "corporate": os.path.join(BASE_DIR, "spillburg corporate services", "Company Profile - 2026.pdf"),
    "logistics": os.path.join(BASE_DIR, "spillburg logistics", "Company Profile - 2026.pdf"),
}

for prefix, pdf_path in PROFILES.items():
    if not os.path.exists(pdf_path):
        print(f"Skipping {prefix}: {pdf_path} not found")
        continue
    doc = pymupdf.open(pdf_path)
    # Render key pages: Page 1 (Cover), Page 3 (Leadership/About), and Page 6 or 8 (Services/Highlights)
    pages_to_render = [0, 2, 5, 7] # 0-indexed
    for page_num in pages_to_render:
        if page_num < len(doc):
            page = doc[page_num]
            pix = page.get_pixmap(dpi=120)
            out_name = f"{prefix}_page_{page_num+1:02d}.png"
            pix.save(os.path.join(DOCS_IMG_DIR, out_name))
            print(f"Saved {out_name}")

print("Screenshots prepared successfully in docs/screenshots/")
