import subprocess
import os

chrome = r"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("spillburg corporate services/source_template/index.html")
master_pdf = os.path.abspath("spillburg corporate services/Company Profile - 2026.pdf")
user_data = os.path.abspath("scratch/chrome_tmp_corp2")

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

print("Executing cmd:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
print("Exit code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
print("Exists:", os.path.exists(master_pdf))
