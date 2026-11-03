from PIL import Image

page3_path = r"C:\Users\User\.gemini\antigravity-ide\brain\010c63f6-24c0-4578-88fa-3dc014f8f00b\scratch\holdings_pages\page_03.png"
im = Image.open(page3_path)
w, h = im.size
print(f"Page 3 size: {w} x {h}")

# In page_03.png:
# Left photo (Hameez):
# x: ~80 to ~400, y: ~240 to ~415 (normalized to image coordinates)
# Let's inspect coordinates precisely:
# Let's find the golden box or crop accurately
# w is roughly 1200, h is roughly 1700
crop_left = im.crop((int(w * 0.08), int(h * 0.24), int(w * 0.40), int(h * 0.42)))
crop_right = im.crop((int(w * 0.58), int(h * 0.24), int(w * 0.90), int(h * 0.42)))

crop_left.save("assets/director_hameez_precise.jpg", quality=95)
crop_right.save("assets/director_shaameel_precise.jpg", quality=95)
print("Saved cropped director portraits.")
