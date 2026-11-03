import os
import pymupdf

BASE_DIR = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"
COMPANIES = [
    "destination consultancy",
    "spillburg corporate services",
    "spillburg logistics"
]

for company in COMPANIES:
    comp_dir = os.path.join(BASE_DIR, company)
    pdf_path = os.path.join(comp_dir, "Company Profile - 2026.pdf")
    svg_dir = os.path.join(comp_dir, "figma_svg_pages")
    os.makedirs(svg_dir, exist_ok=True)
    
    doc = pymupdf.open(pdf_path)
    for i, page in enumerate(doc):
        svg_filename = f"Page {i+1:02d}.svg"
        svg_path = os.path.join(svg_dir, svg_filename)
        svg_content = page.get_svg_image()
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
    print(f"Generated {len(doc)} SVG pages for {company} at {svg_dir}")

print("Done exporting all SVGs.")

