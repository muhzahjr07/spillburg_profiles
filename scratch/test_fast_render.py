import subprocess
import os

chrome = r"C:\Users\User\AppData\Local\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("spillburg corporate services/source_template/index.html")
master_pdf = os.path.abspath("spillburg corporate services/Company Profile - 2026.pdf")
user_data = os.path.abspath("scratch/chrome_tmp_corp3")

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

print("Launching process...")
p = subprocess.Popen(cmd)
# Wait up to 6 seconds, check if pdf exists
import time
for i in range(12):
    time.sleep(0.5)
    if os.path.exists(master_pdf) and os.path.getsize(master_pdf) > 10000:
        print(f"PDF generated in {(i+1)*0.5}s! Size: {os.path.getsize(master_pdf)}")
        break

p.kill()
print("Killed browser, final check:")
print("Exists:", os.path.exists(master_pdf), "Size:", os.path.getsize(master_pdf) if os.path.exists(master_pdf) else 0)
