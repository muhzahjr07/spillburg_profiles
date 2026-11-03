import fitz

doc = fitz.open("spillburg holdings/v3_final/Company Profile - 2026.pdf")
page3 = doc[2]

for info in page3.get_image_info():
    print("Image info keys:", info.keys())
    print("bbox:", info.get("bbox"), "number:", info.get("number"))

print("\nHameez positions:")
for r in page3.search_for("Hameez"):
    print(r)

print("\nShaameel positions:")
for r in page3.search_for("Shaameel"):
    print(r)
