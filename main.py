# main.py
# Main file
# Craiyon Finder
# Interface for generating images using the Craiyon AI
# Developed solely by Nater0214
# Libraries not developed by me


# Imports
from get import get_images
from save import save_images
from spinner import Spinner


# Deffinitions
def main(prompt: str, spinner: bool = True) -> None:
    # Get images
    print(f"{prompt}: ")
    if spinner:
        with Spinner():
            images = get_images(prompt)
    
    else:
        images = get_images(prompt)

    # Save images
    save_images(images, prompt)
    print("Done!\n")


# Main
# Get prompt
# prompt = input("Prompt: ")
prompt = "Phoenix Sports Logo"

if prompt == 'LIST': # If list of prompts is requested do that
    # Get prompts
    prompts = []
    while not prompt == 'END':
        prompt = input("Prompt: ")
        if not prompt == 'END':
            prompts.append(prompt)
    
    for prompt in prompts:
        main(prompt)
    
else: # or don't.
    main(prompt)