import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from base import BasePage
from elements import AllPageCommonEelements
from elements import LoginPageCommonElements
from elements import WpVersionCheckElements
# from elements import LoginPageCommonElements, AdminHomepageElements, AllPageCommonEelements
from selenium.webdriver.common.action_chains import ActionChains

class SiteUp(BasePage):
    def __init__(self, driver):
        super(SiteUp, self).__init__(driver)

    def site_up(self):
        site_name = 'Rethinkhealth'
        wp_url = "http://rth.dev.lin.panth.coms/"

        # Site is UP checking
        status = "Unknown"
        try:
            req = requests.get(wp_url)
            status = req.status_code, req.reason
            site_status = str(status)
            if site_status == "(200, 'OK')":
                wp_site_status = True
                print "Rethinkhealth site status: %s" % site_status
            else:
                print "Rethinkhealth site status: %s" % site_status
        except requests.exceptions.ConnectionError as e:
            print "%s site has the following error:\n%s" %(site_name, e)

class SiteOk(BasePage):
    def __init__(self, driver):
        super(SiteOk, self).__init__(driver)
        self.com_elem = AllPageCommonEelements(self.driver)

    def site_check(self):
        site_is_up = False
        # print 'starting test now...\n'

        # Check site page element
        try:
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.com_elem._page)))
            site_is_up = True
        except:
            site_is_up = False
            print "Error! Site did not load."

        # Check site logo
        try:
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.com_elem._site_logo)))
            site_is_up = True
        except:
            site_is_up = False
            print "Error! Site Logo did not load."

        # Check Site Navigation
        try:
            WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.com_elem._navbar)))
            site_is_up = True
        except:
            site_is_up = False
            print "Error! Site Navigation did not load."

        print 'Site checking completed.'+str(datetime.now())

        if site_is_up is True:
            print 'The site is up and running.'
        elif site_is_up is False:
            print 'The site did not load properly.'
        # return site_is_up

class Login(BasePage):
    def __init__(self, driver):
        super(Login, self).__init__(driver)
        self.com_elem = LoginPageCommonElements(self.driver)

    def login_as_admin(self):
        self.driver.get("http://rth.dev.lin.panth.com/wp-admin")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.com_elem._login_email_field)))
        except:
            print 'Error! Username or Email field does not load.'

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.com_elem._login_pass_field)))
        except:
            print 'Error! Password field does not load.'

        self.driver.find_element_by_id(self.com_elem._login_email_field).clear()
        self.driver.find_element_by_id(self.com_elem._login_email_field).send_keys(self.com_elem.username)
        self.driver.find_element_by_id(self.com_elem._login_pass_field).clear()
        self.driver.find_element_by_id(self.com_elem._login_pass_field).send_keys(self.com_elem.password)
        self.driver.find_element_by_id(self.com_elem._login_button).click()

        # Verify admin login

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.com_elem._wp_admin_bar)))
        print 'Successfully logged in as Admin.'

        # print 'Login as Admin failed.'

        # print 'Login as Admin successfully.'

class WpVersionCheck(BasePage):
    def __init__(self, driver):
        super(WpVersionCheck, self).__init__(driver)
        self.com_elem = WpVersionCheckElements(self.driver)

    def wp_version_check(self):
        self.driver.get("http://rth.dev.lin.panth.com/wp-admin")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.com_elem._dashboard)))
        except:
            print 'Error! WordPress Dashboard did not load.'

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.com_elem._wp_version)))
            wp_version = self.driver.find_element_by_id(self.com_elem._wp_version).text
            # print "Rethinkhealth Current WordPress Version is: " + wp_version + "."
            # print "Current WordPress Version is: "+wp_version+"."
            if wp_version == "":
                self.driver.find_element_by_xpath(self.com_elem._at_glance_expand).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.com_elem._wp_version)))
                wp_version = self.driver.find_element_by_id(self.com_elem._wp_version).text
                wp_version_message = "Rethinkhealth Current WordPress Version is: " + wp_version + "."

            print "Rethinkhealth Current WordPress Version is: " + wp_version + "."
        except:
            print 'Error! WP version message did not found.'
