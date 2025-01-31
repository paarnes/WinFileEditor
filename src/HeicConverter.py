import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(input_path, output_path=None):
    """
    Convert a single HEIC file or all HEIC files in a folder to JPG.

    :param input_path: Path to a single HEIC file or a folder containing HEIC files.
    :param output_path: Path to save the converted JPG files. If None, saves in 'converted' folder.
    """
    # Register HEIF format with Pillow
    pillow_heif.register_heif_opener()

    # Check if input is a folder or a single file
    if os.path.isdir(input_path):  # Batch conversion
        if not output_path:
            output_path = os.path.join(input_path, "converted")
        os.makedirs(output_path, exist_ok=True)

        for filename in os.listdir(input_path):
            if filename.lower().endswith(".heic"):
                heic_file = os.path.join(input_path, filename)
                jpg_file = os.path.join(output_path, os.path.splitext(filename)[0] + ".jpg")

                try:
                    image = Image.open(heic_file)
                    image.save(jpg_file, "JPEG", quality=100)
                    print(f"Converted: {heic_file} -> {jpg_file}")
                except Exception as e:
                    print(f"Failed to convert {heic_file}: {e}")

        print("All files converted!")
        return True

    else:  # Single file conversion
        if not input_path.lower().endswith(".heic"):
            print("Error: The selected file is not a HEIC file.")
            return False

        if not output_path:
            output_path = os.path.splitext(input_path)[0] + ".jpg"

        try:
            image = Image.open(input_path)
            image.save(output_path, "JPEG", quality=100)
            print(f"Converted: {input_path} -> {output_path}")
            return True
        except Exception as e:
            print(f"Failed to convert {input_path}: {e}")
            return False
