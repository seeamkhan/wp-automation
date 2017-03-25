from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from time import sleep
from datetime import datetime
from base import BasePage
from elements import AllPageCommonEelements
from elements import NewPostEelements
from elements import WpVersionCheckElements
from selenium.webdriver.common.action_chains import ActionChains
from custom_methods import AllCustomMethods


class NewPost(BasePage):
    def __init__(self, driver):
        super(NewPost, self).__init__(driver)
        self.element = AllCustomMethods(self.driver)
        self.com_elem = NewPostEelements(self.driver)
        self.base_url = AllPageCommonEelements(self.driver).site_url
        self.test_post_title = "Pantheon Test Post"

    def add_new_post(self):
        # Go to add new post page
        add_new_post_url = "%s/wp-admin/post-new.php" % self.base_url
        self.driver.get(add_new_post_url)

        # Insert new post title
        self.element.verify(self.com_elem._title_field, 5)
        self.driver.find_element_by_xpath(self.com_elem._title_field).send_keys(self.test_post_title)

        # Insert new post body content
        self.element.verify(self.com_elem._content_body, 5)
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
        self.element.verify(self.com_elem._add_media_button, 5)
        self.driver.find_element_by_xpath(self.com_elem._add_media_button).click()
        self.element.verify(self.com_elem._upload_file, 5)
        self.driver.find_element_by_xpath(self.com_elem._upload_file).click()
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'panth-test.jpg')
        self.driver.find_element_by_xpath(self.com_elem._input_file).send_keys(self.file_path)
        self.element.verify(self.com_elem._test_file, 5)
        # Click on the Insert Into Post button
        self.element.verify(self.com_elem._insert_into_post)
        self.driver.find_element_by_xpath(self.com_elem._insert_into_post).click()
        sleep(5)
        if(self.driver.find_element_by_xpath(self.com_elem._insert_into_post).is_enabled()):
            # print "Modal is visible."
            self.driver.find_element_by_xpath(self.com_elem._insert_into_post).click()
            sleep(3)
        # if(self.driver.find_element_by_xpath(self.com_elem._edit_visibility).is_enabled()):
        #     print "Edit visibility enabled."
        #     self.driver.find_element_by_xpath(self.com_elem._insert_into_post).click()
        else:
            pass
            # print "Modal is not visible."
        # Click on the Edit link for Visibility option
        self.element.verify(self.com_elem._edit_visibility)
        sleep(5)
        self.driver.find_element_by_xpath(self.com_elem._edit_visibility).click()
        sleep(2)
        self.driver.find_element_by_xpath(self.com_elem._visibility_private).click()
        sleep(2)
        self.driver.find_element_by_xpath(self.com_elem._visibility_ok_button).click()
        self.element.verify(self.com_elem._uncategorized)
        sleep(5)
        self.driver.find_element_by_xpath(self.com_elem._uncategorized).click()

        # Click Publish/Update button
        self.driver.find_element_by_xpath(self.com_elem._publish_button).click()

        # View the newly created post
        self.element.verify(self.com_elem._view_post)
        self.driver.find_element_by_xpath(self.com_elem._view_post).click()

        # Verify new page
        self.element.verify(self.com_elem._new_post_title)
        self.element.verify(self.com_elem._new_post_body)
        self.element.verify(self.com_elem._new_post_image)
        self.driver.save_screenshot('new-post.png')
        print "New post created successfully."
        # sleep(3)

    def clean_up_test_post(self):
        # # Go to admin Dashboard
        # dashboard_url = "%s/wp-admin/index.php" % self.base_url
        # print "Dashboard URL is: %s" % dashboard_url
        # self.driver.get(dashboard_url)
        # self.element.verify(self.com_elem._dashboard_page_title)

        # Go to All post page
        all_post_page_url = "%s/wp-admin/edit.php" % self.base_url
        # print "All Post Page URL is: %s" % all_post_page_url
        self.driver.get(all_post_page_url)
        self.element.verify(self.com_elem._test_post_title)
        self.driver.find_element_by_xpath(self.com_elem._test_post_title).click()
        self.element.verify(self.com_elem._move_to_trash)
        self.driver.find_element_by_xpath(self.com_elem._move_to_trash).click()
        self.element.verify(self.com_elem._delete_confirmation_msg)
        print "Test post removed successfully"