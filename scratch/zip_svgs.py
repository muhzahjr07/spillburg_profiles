import shutil
import os

BASE_DIR = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"
for comp in ["destination consultancy", "spillburg corporate services", "spillburg logistics"]:
    svg_dir = os.path.join(BASE_DIR, comp, "figma_svg_pages")
    zip_dest = os.path.join(BASE_DIR, comp, "figma_svg_pages")
    if os.path.exists(svg_dir):
        shutil.make_archive(zip_dest, "zip", svg_dir)
        print(f"Created {zip_dest}.zip")

print("All figma_svg_pages zipped successfully.")
