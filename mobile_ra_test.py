from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://vk.com/app3696901_71147356')

a = driver.find_element_by_id('quick_email')
time.sleep(10)
a.send_keys('katzxa@mail.ru')



b = driver.find_element_by_name('pass')
b.click()
b.send_keys('rfnz27011990')

driver.implicitly_wait(10)

c = driver.find_element_by_id('quick_login_button')
c.click()

driver.implicitly_wait(15)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
elem = driver.find_element_by_class_name("progress-bar-number-value ng-binding")
elem.click()