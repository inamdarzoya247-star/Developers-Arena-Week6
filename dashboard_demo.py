from PIL import Image
import os

# Screenshots folder
folder = "screenshots"

# Get all PNG files from screenshots folder
files = [
    os.path.join(folder, f)
    for f in os.listdir(folder)
    if f.lower().endswith(".png")
]

files.sort()

print("Screenshots found:", len(files))

images = []

for file in files:
    print("Adding:", file)
    images.append(Image.open(file).convert("RGB"))

if images:
    images[0].save(
        "dashboard_demo.gif",
        save_all=True,
        append_images=images[1:],
        duration=1500,
        loop=0
    )

    print("dashboard_demo.gif created successfully!")

else:
    print("No PNG screenshots found!")