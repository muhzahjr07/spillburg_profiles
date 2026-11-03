import os
import subprocess
import urllib.parse
import fitz

base = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"
preview_dir = os.path.join(base, "scratch", "previews_v2")
os.makedirs(preview_dir, exist_ok=True)

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
browser = next((p for p in chrome_paths if os.path.exists(p)), None)
print("Using browser:", browser)

profiles = [
    ("destination consultancy", "dest"),
    ("spillburg corporate services", "corp"),
    ("spillburg logistics", "log"),
]

for folder, short in profiles:
    comp_dir = os.path.join(base, folder)
    html_path = os.path.join(comp_dir, "source_template", "index.html")
    out_pdf = os.path.join(comp_dir, "Company Profile - 2026.pdf")
    indiv_dir = os.path.join(comp_dir, "individual_pages")
    os.makedirs(indiv_dir, exist_ok=True)

    file_url = "file:///" + urllib.parse.quote(html_path.replace("\\", "/"), safe=":/")
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf=" + out_pdf,
        file_url
    ]
    subprocess.run(cmd, check=True)

    doc = fitz.open(out_pdf)
    print(f"[{folder}] Rendered {len(doc)} pages -> {out_pdf}")
    for i in range(len(doc)):
        single = fitz.open()
        single.insert_pdf(doc, from_page=i, to_page=i)
        page_pdf = os.path.join(indiv_dir, f"Page {i+1:02d}.pdf")
        single.save(page_pdf)
        single.close()

        pix = doc[i].get_pixmap(dpi=130)
        pix.save(os.path.join(preview_dir, f"{short}_p{i+1}.png"))
    doc.close()

