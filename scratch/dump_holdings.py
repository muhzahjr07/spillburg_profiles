import fitz

doc = fitz.open("spillburg holdings/v3_final/Company Profile - 2026.pdf")
with open("scratch/holdings_text.txt", "w", encoding="utf-8") as out:
    for idx, page in enumerate(doc):
        out.write(f"=== PAGE {idx+1} ===\n")
        out.write(page.get_text() + "\n\n")

print("Saved holdings text.")
