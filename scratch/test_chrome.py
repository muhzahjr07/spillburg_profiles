import subprocess
import os

chrome = r"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe"
test_html = os.path.abspath("scratch/test.html")
test_pdf = os.path.abspath("scratch/test_chrome.pdf")
user_data = os.path.abspath("scratch/chrome_tmp")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={user_data}",
    f"--print-to-pdf={test_pdf}",
    "--no-pdf-header-footer",
    f"file:///{test_html.replace(os.sep, '/')}"
]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
try:
    stdout, stderr = p.communicate(timeout=10)
    print("Communication finished. Exit code:", p.returncode)
except subprocess.TimeoutExpired:
    p.kill()
    print("Timed out, killed process.")

print("PDF exists:", os.path.exists(test_pdf), "Size:", os.path.getsize(test_pdf) if os.path.exists(test_pdf) else 0)
