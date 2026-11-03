import subprocess
import os
import time
import fitz

chrome = r"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("spillburg corporate services/source_template/index.html")
master_pdf = os.path.abspath("spillburg corporate services/Company Profile - 2026.pdf")
indiv_dir = os.path.abspath("spillburg corporate services/individual_pages")
preview_dir = os.path.abspath("scratch/corp_preview")
os.makedirs(indiv_dir, exist_ok=True)
os.makedirs(preview_dir, exist_ok=True)

# Delete existing master pdf first!
if os.path.exists(master_pdf):
    os.remove(master_pdf)

user_data = os.path.abspath(f"scratch/chrome_fresh_{int(time.time()*1000)}")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-background-networking",
    "--disable-default-apps",
    "--disable-extensions",
    "--disable-sync",
    f"--user-data-dir={user_data}",
    f"--print-to-pdf={master_pdf}",
    "--no-pdf-header-footer",
    f"file:///{html_file.replace(os.sep, '/')}"
]

print("Launching Chrome to render freshly...")
p = subprocess.Popen(cmd)
start_time = time.time()
while time.time() - start_time < 15:
    time.sleep(0.5)
    if os.path.exists(master_pdf) and os.path.getsize(master_pdf) > 10000:
        time.sleep(1.0) # ensure file write flushed
        break

p.kill()
print("PDF created! Size:", os.path.getsize(master_pdf))

doc = fitz.open(master_pdf)
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    single_doc = fitz.open()
    single_doc.insert_pdf(doc, from_page=i, to_page=i)
    pdf_out = os.path.join(indiv_dir, f"Page {i+1:02d}.pdf")
    single_doc.save(pdf_out)
    single_doc.close()
    
    pix = page.get_pixmap(dpi=150)
    png_out = os.path.join(preview_dir, f"corp_p{i+1:02d}.png")
    pix.save(png_out)

doc.close()
print("Updated all pages and previews successfully!")
