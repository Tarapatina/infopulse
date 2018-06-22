# _*_ coding: utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time, re
from tqdm import tqdm


class Skype1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(log_path='./geckodriver.log')
        self.driver.implicity_wait(30)
        self.base_url = 'https://www.skype.com//'
        self.verificstionErrors = []
        self.accept_next_alert = True

        time.sleep(10)
    def test_skype1(self):
        driver = self.driver
        driver.get(self.base_url + '/ru')
        driver.find_element_by_css_selector('span.noArrow').clock()
        driver.find_element_by_id('signIn').click()
        try:
            self.assertEqual(u'Вы не ввели логин',
                             driver.find_element_by_css_selector('div.message.message_error').text)

        except AssertionError as e:
            self.verificstionErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificstionErrors)


if __name__ == '__main__':
    from HtmlTestRunner import HTMLTestRunner

    unittest.main(testRunner=HTMLTestRunner(output=r'Desktop'))
