from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from base import BasePage
from elements import RevisedAppElements
from selenium.webdriver.support.ui import Select
# from elements import LoginPageCommonElements, AdminHomepageElements, AllPageCommonEelements
from selenium.webdriver.common.action_chains import ActionChains

class Application(BasePage):
    def __init__(self, driver):
        super(Application, self).__init__(driver)
        self.com_elem = RevisedAppElements(self.driver)

    def application_page_load(self):
        self.app_page_load = False
        self.driver.get('http://stg.sie.qioprogram.panth.com/node/add/application-new')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.com_elem._app_page_title)))
            self.app_page_load = True
        except:
            print 'Error!'

        if self.app_page_load is True:
            print 'Application page loaded properly.'
        elif self.app_page_load is False:
            print 'Application page did not load.'

        print 'Application Page load checking completed on: ' + str(datetime.now())
        # return self.app_page_load

    def app_submit(self):
        self.driver.find_element_by_xpath(self.com_elem._submitter_name).clear()
        self.driver.find_element_by_xpath(self.com_elem._submitter_name).send_keys("Pantheon Test 3")

        self.driver.find_element_by_xpath(self.com_elem._submitter_org).clear()
        self.driver.find_element_by_xpath(self.com_elem._submitter_org).send_keys("Pantheon Test Org 3")

        self.driver.find_element_by_xpath(self.com_elem._submitter_email).clear()
        self.driver.find_element_by_xpath(self.com_elem._submitter_email).send_keys("three.testemail@gmail.com")

        self.driver.find_element_by_xpath(self.com_elem._submitter_phone).clear()
        self.driver.find_element_by_xpath(self.com_elem._submitter_phone).send_keys("09678997038")

        self.driver.find_element_by_xpath(self.com_elem._org_name_dev_test).clear()
        self.driver.find_element_by_xpath(self.com_elem._org_name_dev_test).send_keys("Pantheon Org")

        self.driver.find_element_by_xpath(self.com_elem._summary).clear()
        self.driver.find_element_by_xpath(self.com_elem._summary).send_keys("Pantheon Test Summary text.")

        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Acute")
        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Community")
        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Home Health")
        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Multiple settings")
        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Outpatient")
        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Post Acute")
        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Primary Care")
        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Other")

        Select(self.driver.find_element_by_xpath(self.com_elem._care_setting)).select_by_visible_text("Community")

        self.driver.find_element_by_xpath(self.com_elem._source).clear()
        self.driver.find_element_by_xpath(self.com_elem._source).send_keys("Pantheon Test source")

        self.driver.find_element_by_xpath(self.com_elem._source_phone).clear()
        self.driver.find_element_by_xpath(self.com_elem._source_phone).send_keys("09678997038")

        self.driver.find_element_by_xpath(self.com_elem._source_email).clear()
        self.driver.find_element_by_xpath(self.com_elem._source_email).send_keys("six.testemail@gmail.com")

        self.driver.find_element_by_xpath(self.com_elem._evidence).clear()
        self.driver.find_element_by_xpath(self.com_elem._evidence).send_keys("Pantheon Test evidence")

        self.driver.find_element_by_xpath(self.com_elem._save_btn).click()

        time.sleep(1)
        print "Application submit completed on: " + str(datetime.now())
        pass