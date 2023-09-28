from PIL import Image
import os
import shutil

image_folder = "gambar"  # ganti dengan folder gambar
output_folder = image_folder+"-compressed"
os.makedirs(output_folder, exist_ok=True)
compression_quality = 50

# Open the original image
for filename in os.listdir(image_folder):
    path = os.path.join(image_folder, filename)
    output = os.path.join(output_folder, filename)
    with Image.open(path) as img:
        img.save(output, format="JPEG",
                 quality=compression_quality)

print("Image has been compressed and saved.")
