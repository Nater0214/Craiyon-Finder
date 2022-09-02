# save.py
# Saves the images to files


# Imports
from os.path import exists
from os import mkdir


# Methods
def save_images(images: list, dir_name: str) -> None:
    # Creates found directory if it does not exist
    if not exists(".\\found"):
        mkdir(".\\found")

    # Create directory and store it in a convinient variable
    save_dir = f".\\found\\{dir_name}"
    mkdir(save_dir)

    # Save all the images
    for i, image_content in enumerate(images, start=1):
        with open(f"{save_dir}\\img{i}.jpg", 'wb') as image_file:
            image_file.write(image_content)