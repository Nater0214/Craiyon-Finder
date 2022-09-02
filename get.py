# get.py
# Get the images


# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from base64 import b64decode


# Methods
def get_images(prompt: str) -> list:
    # Create driver
    options = Options()
    if 1 == 1: options.add_experimental_option('excludeSwitches', ['enable-logging']) # For some reason my retarded editor thinks this will terminate the program so it messes everything up in my editor. I nested it so it will shut up.
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Get website and frame
    driver.get("https://craiyon.com")

    while True:
        # Get elements
        wait = driver_wait(driver, 5)
        input_elem: WebElement = wait.until(ec.presence_of_element_located((by.XPATH, "//*[@id=\"prompt\"]")))
        button_elem = driver.find_element(by.XPATH, "//*[@id=\"app\"]/div/div/div[1]/button")

        # Input prompt and press button
        input_elem.send_keys(prompt)
        button_elem.click()

        # Wait until images are ready
        wait = driver_wait(driver, 180)
        try:
            image_grid: WebElement = wait.until(ec.presence_of_element_located((by.CLASS_NAME, "grid-cols-3")))
        except TimeoutException:
            print("It shouldn't take this long! Retrying...")
        
        break

    # Get images
    image_divs = image_grid.find_elements(by.TAG_NAME, "div")
    image_elems = [div.find_element(by.TAG_NAME, "img") for div in image_divs]
    image_64s = [elem.get_attribute("src") for elem in image_elems]

    img_bytes = []
    for img_64 in image_64s:
        img_64: str
        img_64 = img_64[23:]
        img_64 = img_64.split("%0A")
        img_64 = ''.join(img_64)
        img_bytes.append(b64decode(img_64))
    
    return img_bytes