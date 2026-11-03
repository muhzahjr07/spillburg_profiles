import subprocess
import os
import shutil

chrome = r"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe"
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

test_html = os.path.abspath("scratch/test.html")
test_pdf = os.path.abspath("scratch/test.pdf")
user_data = os.path.abspath("scratch/browser_profile")
os.makedirs(user_data, exist_ok=True)

# Try Edge first as it is system-installed and fast
cmd = [
    edge,
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data}",
    f"--print-to-pdf={test_pdf}",
    "--no-pdf-header-footer",
    test_html
]

print("Running Edge print...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
print("Returncode:", res.returncode)
print("PDF exists:", os.path.exists(test_pdf))
if os.path.exists(test_pdf):
    print("Size:", os.path.getsize(test_pdf))
    import fitz
    doc = fitz.open(test_pdf)
    print("Pages in PDF:", len(doc))
