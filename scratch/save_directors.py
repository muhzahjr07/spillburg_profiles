import os
import shutil

assets_dir = r"assets"
os.makedirs(assets_dir, exist_ok=True)

# p03_img01_1715.jpeg and p03_img02_1719.jpeg
# Let's inspect which file corresponds to which xref
# In check_directors:
# image 9 was bbox 52..390 (left: Hameez)
# image 7 was bbox 400..890 (right: Shaameel)

# Let's copy both to assets directory
shutil.copy("scratch/extracted_assets/p03_img01_1715.jpeg", os.path.join(assets_dir, "director_portrait_left.jpg"))
shutil.copy("scratch/extracted_assets/p03_img02_1719.jpeg", os.path.join(assets_dir, "director_portrait_right.jpg"))

print("Copied director portraits to assets.")
