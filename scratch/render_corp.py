import subprocess
import os
import fitz

chrome = r"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("spillburg corporate services/source_template/index.html")
master_pdf = os.path.abspath("spillburg corporate services/Company Profile - 2026.pdf")
indiv_dir = os.path.abspath("spillburg corporate services/individual_pages")
os.makedirs(indiv_dir, exist_ok=True)
user_data = os.path.abspath("scratch/chrome_tmp_corp")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={user_data}",
    f"--print-to-pdf={master_pdf}",
    "--no-pdf-header-footer",
    f"file:///{html_file.replace(os.sep, '/')}"
]

print("Rendering master PDF...")
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
try:
    stdout, stderr = p.communicate(timeout=15)
except subprocess.TimeoutExpired:
    p.kill()

print("Master PDF exists:", os.path.exists(master_pdf))
if os.path.exists(master_pdf):
    doc = fitz.open(master_pdf)
    print(f"Total pages rendered: {len(doc)}")
    for i, page in enumerate(doc):
        # Extract individual page PDF
        single_doc = fitz.open()
        single_doc.insert_pdf(doc, from_page=i, to_page=i)
        single_pdf_path = os.path.join(indiv_dir, f"Page {i+1:02d}.pdf")
        single_doc.save(single_pdf_path)
        single_doc.close()
        print(f"Saved Page {i+1:02d}.pdf (rect: {page.rect})")
    doc.close()
