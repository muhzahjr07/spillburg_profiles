import os
import shutil

base_dir = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"
corp_dir = os.path.join(base_dir, "spillburg corporate services")
log_dir = os.path.join(base_dir, "spillburg logistics")
dest_dir = os.path.join(base_dir, "destination consultancy")

for d in [corp_dir, log_dir, dest_dir]:
    os.makedirs(os.path.join(d, "assets"), exist_ok=True)
    os.makedirs(os.path.join(d, "individual_pages"), exist_ok=True)
    os.makedirs(os.path.join(d, "source_template"), exist_ok=True)

brain_dir = r"C:\Users\User\.gemini\antigravity-ide\brain\010c63f6-24c0-4578-88fa-3dc014f8f00b"

# Find generated images
img_corp_cover = os.path.join(brain_dir, "corporate_services_cover_1793172005086.jpg")
img_log_cover = os.path.join(brain_dir, "logistics_cover_1793172025073.jpg")
img_dest_cover = os.path.join(brain_dir, "destination_cover_1793172043222.jpg")
img_corp_board = os.path.join(brain_dir, "corporate_boardroom_1793172063221.jpg")
img_log_wh = os.path.join(brain_dir, "logistics_warehouse_fleet_1793172086535.jpg")

# Shared assets
dir_left = "assets/director_portrait_left.jpg"
dir_right = "assets/director_portrait_right.jpg"
logo_wide = "assets/spillburg_logo_wide.jpg"
logo_mark = "assets/spillburg_logo_mark.jpg"
cinnamon = "assets/cinnamon_lakeside.jpg"
qr_code = "assets/qr_code_general.jpg"
frame95 = "spillburg holdings/Stock/Frame_95_logos_cream_2x.png"

# Copy to Corp Services
shutil.copy(img_corp_cover, os.path.join(corp_dir, "assets", "cover_hero.jpg"))
shutil.copy(img_corp_board, os.path.join(corp_dir, "assets", "boardroom_hero.jpg"))
shutil.copy(dir_left, os.path.join(corp_dir, "assets", "director_hameez.jpg"))
shutil.copy(dir_right, os.path.join(corp_dir, "assets", "director_shaameel.jpg"))
shutil.copy(logo_wide, os.path.join(corp_dir, "assets", "logo_wide.jpg"))
shutil.copy(logo_mark, os.path.join(corp_dir, "assets", "logo_mark.jpg"))
shutil.copy(cinnamon, os.path.join(corp_dir, "assets", "cinnamon_lakeside.jpg"))
shutil.copy(qr_code, os.path.join(corp_dir, "assets", "qr_code.jpg"))
shutil.copy(frame95, os.path.join(corp_dir, "assets", "affiliations_grid.png"))

# Copy to Logistics
shutil.copy(img_log_cover, os.path.join(log_dir, "assets", "cover_hero.jpg"))
shutil.copy(img_log_wh, os.path.join(log_dir, "assets", "warehouse_hero.jpg"))
shutil.copy(dir_left, os.path.join(log_dir, "assets", "director_hameez.jpg"))
shutil.copy(dir_right, os.path.join(log_dir, "assets", "director_shaameel.jpg"))
shutil.copy(logo_wide, os.path.join(log_dir, "assets", "logo_wide.jpg"))
shutil.copy(logo_mark, os.path.join(log_dir, "assets", "logo_mark.jpg"))
shutil.copy(cinnamon, os.path.join(log_dir, "assets", "cinnamon_lakeside.jpg"))
shutil.copy(qr_code, os.path.join(log_dir, "assets", "qr_code.jpg"))
shutil.copy(frame95, os.path.join(log_dir, "assets", "affiliations_grid.png"))

# Copy to Destination
shutil.copy(img_dest_cover, os.path.join(dest_dir, "assets", "cover_hero.jpg"))
shutil.copy(dir_left, os.path.join(dest_dir, "assets", "director_hameez.jpg"))
shutil.copy(dir_right, os.path.join(dest_dir, "assets", "director_shaameel.jpg"))
shutil.copy(logo_wide, os.path.join(dest_dir, "assets", "logo_wide.jpg"))
shutil.copy(logo_mark, os.path.join(dest_dir, "assets", "logo_mark.jpg"))
shutil.copy(cinnamon, os.path.join(dest_dir, "assets", "cinnamon_lakeside.jpg"))
shutil.copy(qr_code, os.path.join(dest_dir, "assets", "qr_code.jpg"))
shutil.copy(frame95, os.path.join(dest_dir, "assets", "affiliations_grid.png"))

print("Assets populated across all companies successfully!")
