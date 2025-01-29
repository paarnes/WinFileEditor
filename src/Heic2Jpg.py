import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(folder_path):
    # Register HEIF format with Pillow
    pillow_heif.register_heif_opener()

    # Create output folder
    output_folder = os.path.join(folder_path, "converted")
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if file is a HEIC file
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)
            try:
                # Open HEIC file using Pillow
                image = Image.open(heic_path)

                # Generate output JPG path
                output_path = os.path.join(
                    output_folder, os.path.splitext(filename)[0] + ".jpg"
                )

                # Save the image as JPG with maximum quality
                image.save(output_path, "JPEG", quality=100)

                print(f"Converted: {filename} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")




if __name__ == "__main__":
    folder_path = r"C:\Users\perhe\OneDrive\Documents\Python_skript\Heic2Jpg\heic\heic2"
    if os.path.exists(folder_path):
        convert_heic_to_jpg(folder_path)
    else:
        print("Invalid folder path. Please try again.")
