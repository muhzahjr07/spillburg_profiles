import shutil
import os

base_dir = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"
dirs = [
    os.path.join(base_dir, "spillburg corporate services", "assets"),
    os.path.join(base_dir, "spillburg logistics", "assets"),
    os.path.join(base_dir, "destination consultancy", "assets")
]

src_h = os.path.join(base_dir, "assets", "director_hameez_clean.jpg")
src_s = os.path.join(base_dir, "assets", "director_shaameel_clean.jpg")

for d in dirs:
    shutil.copy(src_h, os.path.join(d, "director_hameez.jpg"))
    shutil.copy(src_s, os.path.join(d, "director_shaameel.jpg"))

print("Updated authentic director photos in all 3 companies!")
