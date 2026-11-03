import subprocess
import os
import time
import fitz

chrome = r"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("spillburg logistics/source_template/index.html")
master_pdf = os.path.abspath("spillburg logistics/Company Profile - 2026.pdf")
indiv_dir = os.path.abspath("spillburg logistics/individual_pages")
preview_dir = os.path.abspath("scratch/logistics_preview")
os.makedirs(indiv_dir, exist_ok=True)
os.makedirs(preview_dir, exist_ok=True)

if os.path.exists(master_pdf):
    os.remove(master_pdf)

user_data = os.path.abspath(f"scratch/chrome_log_{int(time.time()*1000)}")

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

print("Rendering Logistics PDF...")
p = subprocess.Popen(cmd)
start_time = time.time()
while time.time() - start_time < 15:
    time.sleep(0.5)
    if os.path.exists(master_pdf) and os.path.getsize(master_pdf) > 10000:
        time.sleep(1.0)
        break

p.kill()
print("PDF created! Size:", os.path.getsize(master_pdf))

doc = fitz.open(master_pdf)
print(f"Total pages rendered: {len(doc)}")
for i, page in enumerate(doc):
    single_doc = fitz.open()
    single_doc.insert_pdf(doc, from_page=i, to_page=i)
    pdf_out = os.path.join(indiv_dir, f"Page {i+1:02d}.pdf")
    single_doc.save(pdf_out)
    single_doc.close()
    
    pix = page.get_pixmap(dpi=150)
    png_out = os.path.join(preview_dir, f"log_p{i+1:02d}.png")
    pix.save(png_out)
    print(f"Page {i+1} saved to {pdf_out}")

doc.close()
print("Logistics profile rendering complete!")
