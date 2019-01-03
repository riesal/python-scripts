# python + selenium for simple screenshot
# prerequisites:
# simple use docker selenium OR
# python 2.7 with Ubuntu 16.04
#   - apt-get install xvfb google-chrome
#   - cd /tmp && virtualenv tes
#   - source /tmp/tes/bin/activate
#   - pip install chromedriver-install chromedriver chromedriver-binary chrome-driver selenium pyvirtualdisplay

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 800))
display.start()

user=""
pwd=""

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")

#options.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(3)
driver.get('https://your-website.com')
try:
    element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "main-body"))
    )
finally:
    elem=driver.find_element_by_css_selector("input.form-control")
    user="detikzzzzzz.com"
    elem.send_keys(user)
    elem=driver.find_element_by_css_selector("input.btn.search")
    elem.send_keys(Keys.RETURN)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.save_screenshot('skrinsut.png')
    driver.close()
    driver.quit()
