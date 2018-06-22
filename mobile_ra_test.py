from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('https://vk.com/')

a = driver.find_element_by_id('index_email')
a.click()
#a = time.sleep(10)
a.send_keys('katzxa@mail.ru')


b = driver.find_element_by_id('index_pass')
b.click()
b.send_keys('rfnz27011990')

c = driver.find_element_by_id('index_login_button')
c.click()
