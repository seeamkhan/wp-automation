from selenium import webdriver
from time import sleep
import unittest
from __builtin__ import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create new Chrome session
        cls.driver = webdriver.Chrome()
        # cls.driver = webdriver.PhantomJS()
        # cls.driver.maximize_window()

        # Navigate to site homepage
        # site_url = 'http://rth.dev.lin.panth.com/'
        # cls.driver.get(site_url)
        # print "Testing: "+site_url+" site."

    def verify(self, elem, time):
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, elem)))
            print "%s element found." % elem
        except:
            print "Driver did not recognize '%s' element." % elem

    def test_010(self):
        self.site_url = 'http://rth.dev.lin.panth.com/'
        self._logo = "//img[@alt = 'ReThink Health logo']"
        self.driver.get(self.site_url)

        # try:
        #     WebDriverWait(self.driver, 5).until(
        #         EC.presence_of_element_located((By.XPATH, self._logo)))
        #     print 'Logo found.'
        # except:
        #     print "Driver did not recognize logo."

        self.verify(self._logo, 5)



    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()