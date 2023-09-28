from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import subprocess
import os

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
    c.drawImage(file_path, x, page_height - y - image_height,
                width=image_width, height=image_height)
    x += image_width + 0.6*28.35
    image_placed += 1


# Save the canvas as a PDF file
c.save()

print(f"PDF file '{pdf_filename}' has been created.")
# Compress the PDF using PyPDF2
subprocess.Popen(["xdg-open", pdf_filename])
