from image_converter import ImageConverter
from display_manager import DisplayManager
import os
import shutil
import sys
import time
import threading

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PIC_PATH = os.path.join(SCRIPT_DIR, 'pic')
SD_MOUNT_BASE = "/media/enriquepi"  # Adjust this path as needed

display_manager = DisplayManager(image_folder=PIC_PATH)
print("Display manager created")


def process_and_display_images(sd_path):
    if os.path.exists(PIC_PATH):
        shutil.rmtree(PIC_PATH)
    os.makedirs(PIC_PATH)

    image_converter = ImageConverter(source_dir=sd_path, output_dir=PIC_PATH)
    print("Image converter created")

    # Process images from the SD card
    display_manager.display_message('start.jpg')
    try:
        print("Processing images, please wait...")
        image_converter.process_images()
    except Exception as e:
        print(f"Error during image processing: {e}")

    # Start displaying images
    try:
        display_manager.display_images()
    except Exception as e:
        print(f"Error during image display: {e}")


if __name__ == "__main__":
    sd_path = sys.argv[1]
    print(f"Frame manager received SD path: {sd_path}")
    process_and_display_images(sd_path)
