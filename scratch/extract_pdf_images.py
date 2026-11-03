import fitz
import os

pdf_path = r"spillburg holdings/v3_final/Company Profile - 2026.pdf"
out_dir = r"scratch/extracted_assets"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print("Total pages:", len(doc))

img_count = 0
for pno in range(len(doc)):
    page = doc[pno]
    image_list = page.get_images(full=True)
    print(f"Page {pno+1} has {len(image_list)} images")
    for img_idx, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        filename = f"p{pno+1:02d}_img{img_idx:02d}_{xref}.{image_ext}"
        filepath = os.path.join(out_dir, filename)
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        img_count += 1

print(f"Extracted {img_count} images to {out_dir}")
