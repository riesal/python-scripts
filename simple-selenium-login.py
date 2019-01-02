# python + selenium for automated weblogin
# prerequisites:
# python 2.7 with Ubuntu 16.04
#   - apt-get install xvfb google-chrome
#   - cd /tmp && virtualenv tes
#   - source /tmp/tes/bin/activate
#   - pip install chromedriver-install chromedriver chromedriver-binary chrome-driver selenium pyvirtualdisplay

import time

from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys

display = Display(visible=0, size=(800, 600))
display.start()

user=""
pwd=""

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

options.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://member.dijaminmurah.com/clientarea.php')
elem=driver.find_element_by_id("inputEmail")
user="your@user.com"
elem.send_keys(user)
elem=driver.find_element_by_id("inputPassword")
pwd="your@password.com"
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
