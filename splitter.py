import os
from PIL import Image
import shutil

# Define the input folder containing your images and output folders
input_folder = 'fixed'
output_folder_1 = '34'
output_folder_2 = '12'
dump_folder = 'dump'

# Create the output folders if they don't exist
os.makedirs(output_folder_1, exist_ok=True)
os.makedirs(output_folder_2, exist_ok=True)
os.makedirs(dump_folder, exist_ok=True)

# Loop through each image in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    print(file_path)
    # Open the image using Pillow
    with Image.open(file_path) as img:
        # Get the aspect ratio by dividing width by height
        width, height = img.size
        aspect_ratio = width / height
        print(aspect_ratio)

        # Define the threshold for aspect ratio comparison
        threshold = .1

        # Determine which output folder to move the image to based on the aspect ratio
        if (aspect_ratio >= 0.7 and aspect_ratio < 0.8):  # 3:4 ratio (0.75 is 3/4)
            output_path = os.path.join(output_folder_1, filename)
        elif (aspect_ratio >= 0.5 and aspect_ratio <= 0.6):  # 1:2 ratio (0.5 is 1/2)
            output_path = os.path.join(output_folder_2, filename)
        else:
            output_path = os.path.join(dump_folder, filename)
            continue
        # break

        # Move the image to the appropriate output folder
        shutil.copy(file_path, output_path)

print("Images have been split into folders based on aspect ratio.")
