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


class NewPost(BasePage):
    def __init__(self, driver):
        super(NewPost, self).__init__(driver)
        self.com_elem = NewPostEelements(self.driver)
        self.test_post_title = "Pantheon Test Post"

    def add_new_post(self):
        # Go to add new post page
        post_hover_content = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.com_elem._menu_posts))
        post_hover_content.perform()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._add_new_post)))
        except:
            print 'Driver did not recognize add new post link.'

        self.driver.find_element_by_xpath(self.com_elem._add_new_post).click()

        # Insert new post title
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._title_field)))
        except:
            print 'Driver did not recognize new post title field'

        self.driver.find_element_by_xpath(self.com_elem._title_field).send_keys(self.test_post_title)

        # Insert new post body content
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._content_body)))
        except:
            print 'Driver did not recognize new post body field.'
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
            print 'Driver did not recognize add media button'

        self.driver.find_element_by_xpath(self.com_elem._add_media_button).click()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._upload_file)))
        except:
            print 'Driver did not recognize upload file button'
        self.driver.find_element_by_xpath(self.com_elem._upload_file).click()

        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'panth-test.jpg')
        self.driver.find_element_by_xpath(self.com_elem._input_file).send_keys(self.file_path)
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._test_file)))
        except:
            print 'Driver did not recognize panth-test.jpg file.'
        # Click on the Insert Into Post button
        self.driver.find_element_by_xpath(self.com_elem._insert_into_post).click()

        # Click on the Edit link for Visibility option
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._edit_visibility)))
        except:
            pass
        self.driver.find_element_by_xpath(self.com_elem._edit_visibility).click()
        self.driver.find_element_by_xpath(self.com_elem._visibility_private).click()
        self.driver.find_element_by_xpath(self.com_elem._visibility_ok_button).click()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._uncategorized)))
        except:
            print 'Driver did not recognize Uncategorized checkbox.'
        self.driver.find_element_by_xpath(self.com_elem._uncategorized).click()

        # Click Publish/Update button
        self.driver.find_element_by_xpath(self.com_elem._publish_button).click()

        # View the newly created post
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._view_post)))
        except:
            print 'Driver did not recognize View post link.'
        self.driver.find_element_by_xpath(self.com_elem._view_post).click()

        # Verify new page
        try:
            self.driver.find_element_by_xpath(self.com_elem._new_post_title)
        except:
            print 'Error! New Post title did not found.'

        try:
            self.driver.find_element_by_xpath(self.com_elem._new_post_body)
            print 'New post created successfully!'
        except:
            print 'Error! New Post body did not found.'

        try:
            self.driver.find_element_by_xpath(self.com_elem._new_post_image)
        except:
            print 'Error! New Post Image did not found.'

        time.sleep(3)

    def clean_up_test_post(self):
        # Go to admin Dashboard
        admin_menu_hover = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.com_elem._admin_top_menu))
        admin_menu_hover.perform()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._dashboard_menu)))
        except:
            print 'Driver did not recognize Dashboard menu link.'
        self.driver.find_element_by_xpath(self.com_elem._dashboard_menu).click()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._dashboard_page_title)))
        except:
            print 'Driver did not recognize Dashboard Page title.'

        # Go to All post page
        post_hover_content = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.com_elem._menu_posts))
        post_hover_content.perform()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._all_post)))
        except:
            print 'Driver did not recognize add All post link.'

        self.driver.find_element_by_xpath(self.com_elem._all_post).click()
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._test_post_title)))
        except:
            print 'Driver did not recognize Test Post link.'
        self.driver.find_element_by_xpath(self.com_elem._test_post_title).click()

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._move_to_trash)))
        except:
            print 'Driver did not recognize Move to trash link.'
        self.driver.find_element_by_xpath(self.com_elem._move_to_trash).click()

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, self.com_elem._delete_confirmation_msg)))
        except:
            print 'Driver did not recognize post delete confirmation message.'