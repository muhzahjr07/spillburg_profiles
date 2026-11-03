from PIL import Image

im = Image.open(r"C:\Users\User\.gemini\antigravity-ide\brain\010c63f6-24c0-4578-88fa-3dc014f8f00b\scratch\holdings_pages\page_03.png")
w, h = im.size

# Let's crop with precision:
# Left box: x from ~165 to ~715, y from ~625 to ~1065
# Right box: x from ~1070 to ~1620, y from ~625 to ~1065
# Let's verify by testing exact slices
crop_hameez = im.crop((165, 625, 715, 1065))
crop_shaameel = im.crop((1070, 625, 1620, 1065))

crop_hameez.save("assets/director_hameez_clean.jpg", quality=95)
crop_shaameel.save("assets/director_shaameel_clean.jpg", quality=95)
print("Saved clean director portraits:", crop_hameez.size, crop_shaameel.size)
