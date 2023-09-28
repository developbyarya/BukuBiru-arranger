from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import subprocess
import tempfile
import os
from PIL import Image


def exifCorrection(image_path: str):
    temp = "temp"
    os.makedirs(temp, exist_ok=True)
    # Check the Exif orientation and rotate/transpose the image if necessary
    with Image.open(image_path) as img:
        image = img
        if hasattr(image, "_getexif"):
            exif = image._getexif()
            if exif is not None:
                orientation = exif.get(0x0112)
                if orientation is not None:
                    if orientation == 1:
                        # Normal (no rotation needed)
                        pass
                    elif orientation == 2:
                        # Mirrored horizontally
                        image = image.transpose(Image.FLIP_LEFT_RIGHT)
                    elif orientation == 3:
                        # Upside down
                        image = image.rotate(180, expand=True)
                    elif orientation == 4:
                        # Mirrored vertically
                        image = image.transpose(Image.FLIP_TOP_BOTTOM)
                    elif orientation == 5:
                        # Rotated 90 degrees counterclockwise and mirrored horizontally
                        image = image.rotate(90, expand=True).transpose(
                            Image.FLIP_LEFT_RIGHT)
                    elif orientation == 6:
                        # Rotated 90 degrees counterclockwise
                        image = image.rotate(90, expand=True)
                    elif orientation == 7:
                        # Rotated 90 degrees clockwise and mirrored horizontally
                        image = image.rotate(-90,
                                             expand=True).transpose(Image.FLIP_LEFT_RIGHT)
                    elif orientation == 8:
                        # Rotated 90 degrees clockwise
                        image = image.rotate(-90, expand=True)
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_image:
            tmp_image_path = tmp_image.name
            image.save(tmp_image_path, "JPEG")
    return tmp_image_path


# Define the PDF filename
pdf_filename = "output.pdf"

# Define the A4 page size
page_width, page_height = A4

# Create a canvas for the PDF
c = canvas.Canvas(pdf_filename, pagesize=(page_width, page_height))

# Define the image path and dimensions
image_path = "gambar"  # Ganti dengan image path kalian

image_width = 3*28.35  # Replace with the desired width in points
image_height = 4*28.35  # Replace with therow = 1 desired height in points

# Define the position (X, Y) on the page where you want to place the image
x = 0  # Replace with the desired X coordinate in points
y = 0  # Replace with the desired Y coordinate in points

total_image = len(os.listdir(image_path))
max_image_a_page = 6*7
image_placed = 0

for filename in os.listdir(image_path):
    file_path = os.path.join(image_path, filename)
    if (image_placed > 0 and image_placed % max_image_a_page == 0):
        x = 0
        y = 0
        image_placed = 0
        c.showPage()

    if (image_placed > 0 and image_placed % 6 == 0):
        x = 0
        y += image_height+0.28333*28.35

    # Draw the image on the canvas
    image = exifCorrection(file_path)

    c.drawImage(image, x, page_height - y - image_height,
                width=image_width, height=image_height)
    x += image_width + 0.6*28.35
    image_placed += 1


# Save the canvas as a PDF file
c.save()

print(f"PDF file '{pdf_filename}' has been created.")
# Compress the PDF using PyPDF2
subprocess.Popen(["xdg-open", pdf_filename])
