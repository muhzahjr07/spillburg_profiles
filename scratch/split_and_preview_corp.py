import fitz
import os

pdf_path = "spillburg corporate services/Company Profile - 2026.pdf"
indiv_dir = "spillburg corporate services/individual_pages"
preview_dir = "scratch/corp_preview"
os.makedirs(indiv_dir, exist_ok=True)
os.makedirs(preview_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Processing {len(doc)} pages...")

for i, page in enumerate(doc):
    # Save individual page PDF
    single_doc = fitz.open()
    single_doc.insert_pdf(doc, from_page=i, to_page=i)
    pdf_out = os.path.join(indiv_dir, f"Page {i+1:02d}.pdf")
    single_doc.save(pdf_out)
    single_doc.close()
    
    # Save preview image
    pix = page.get_pixmap(dpi=150)
    png_out = os.path.join(preview_dir, f"corp_p{i+1:02d}.png")
    pix.save(png_out)
    print(f"Page {i+1} saved to {pdf_out} and preview {png_out}")

doc.close()
print("All individual pages and previews generated successfully!")
