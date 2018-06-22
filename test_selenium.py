from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#driver = webdriver.Safari()
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('https://demo.oxwall.com/')


t = driver.find_element_by_class_name('ow_signin_label')
t.click()
s = driver.find_element_by_class_name('ow_positive')
s.click()
action= ActionChains(driver)
action.move_to_element(driver.find_element_by_class_name('ow_console_dropdown_hover'))
action.perform()
a = time.sleep(5)
#a = driver.find_element_by_class_name('ow_console_dropdown_cont')
#a.click()
# driver.find_element_by_name('password').click().send_keys('pass')
# driver.find_element_by_name('submit').click()
links = driver.find_element_by_link_text('Sign Out')
links.click()
t = time.sleep(5)

#print(len(links))
driver.quit()

