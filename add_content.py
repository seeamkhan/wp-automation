from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, os
from datetime import datetime
from base import BasePage
from elements import AllPageCommonEelements
from elements import NewPostEelements
from elements import WpVersionCheckElements
# from elements import LoginPageCommonElements, AdminHomepageElements, AllPageCommonEelements
from selenium.webdriver.common.action_chains import ActionChains
import pywinauto


class NewPost(BasePage):
    def __init__(self, driver):
        super(NewPost, self).__init__(driver)
        self.com_elem = NewPostEelements(self.driver)

    def add_new_post(self):
        # Go to add new post page
        post_hover_content = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.com_elem._menu_posts))
        post_hover_content.perform()
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._add_new_post)))
        except:
            print 'Error! Add New Post link does not load.'

        self.driver.find_element_by_xpath(self.com_elem._add_new_post).click()

        # Insert new post title
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._add_new_post_title)))
        except:
            print 'Error! new post page does not load.'

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._title_field)))
        except:
            print 'Error! new post page does not load.'

        self.driver.find_element_by_xpath(self.com_elem._title_field).send_keys("Pantheon Test Post")

        # Insert new post body content
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._content_body)))
        except:
            print 'Error! content body field does not load.'
        # Switch to post body imce iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.com_elem._content_body))
        self.driver.find_element_by_xpath("//body").send_keys(
            "Lorem ipsum Ad dicam 21mei. No vim vim at Ex ius intellegat est, "
            "mel ea vix. sea, his soleat convenire te est @Mei convenire possim. "
            "Ad id Ex animal mei. No est, necessitatibu's quo, \nvim id icam 21salutandi, "
            "assum convenire et Ad mel vim at Ex ius ius-antiopam. verterem intellegat qui. "
            "13Ex animal pro, cu ius-antiopam. sea, his soleat mel vim et intellegat sea, "
            "his soleat\n mel mei. No verterem ex. Accusata possim. assum Ex animal id te est "
            "@Mei adipisci, Ex animal dicam 21assum mei. No sea, his soleat vim at Ex ius "
            "ius-antiopam. ea vix. salutandi, Ad intellegat pro, cu vim at Ex ius ")
        self.driver.find_element_by_xpath("//body").send_keys(Keys.RETURN)
        # Switch back to main window
        self.driver.switch_to.default_content()

        # Upload and Insert new file into the new post
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._add_media_button)))
        except:
            print 'Error! add media button does not load.'

        self.driver.find_element_by_xpath(self.com_elem._add_media_button).click()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._upload_file)))
        except:
            print 'Error! Upload file tab does not load.'
        self.driver.find_element_by_xpath(self.com_elem._upload_file).click()

        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '3d-landscape-wallpapers.jpg')
        time.sleep(2)
        self.driver.find_element_by_xpath(self.com_elem._select_file).send_keys(self.file_path)
        # self.driver.find_element_by_xpath(self.com_elem._select_file).click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//input[@id='html5_1bbaluc621fbtd6a18cf1eql1soc5']").clear()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//input[@id='html5_1bbaluc621fbtd6a18cf1eql1soc5']").send_keys("")


        time.sleep(3)
