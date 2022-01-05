from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from os import listdir
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome()
url1 = 'https://www.google.co.kr/imghp?hl=ko'
driver.get(url1)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('python')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')

i = 1
for image in images:
    image.click()
    time.sleep(2)
    img = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')
    urllib.request.urlretrieve(img, str(i) + '.jpg')
    i = i + 1

# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(2)
# driver.get('https://teachablemachine.withgoogle.com/train/image')
