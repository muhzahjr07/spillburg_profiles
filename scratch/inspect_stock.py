import os
from PIL import Image

stock_dir = r"spillburg holdings/Stock"
files = sorted([f for f in os.listdir(stock_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
print(f"Total files in {stock_dir}: {len(files)}")
for f in files:
    path = os.path.join(stock_dir, f)
    try:
        im = Image.open(path)
        print(f"{f:50s} | {str(im.size):15s} | {im.format:5s} | {os.path.getsize(path)/1024:.1f} KB")
    except Exception as e:
        print(f"{f:50s} | Error: {e}")
