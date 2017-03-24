from selenium.webdriver.support.ui import WebDriverWait
from basetestcase import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Conf_Reader
import os, time
from base import BasePage

class AllPageCommonEelements(BasePage):
    def __init__(self, driver):
        super(AllPageCommonEelements, self).__init__(driver)

        # Page elements
        self._page = "//div[@id='page']"
        self._site_logo = ".//div[@class='branding']"
        # self._top_logo = "//*[@class='logo']"
        self._navbar = ".//*[@class='navbar']"
        # # self._contextual_menu = ".//*[@id='block-menu-block-4']"
        # self._slider = "//div[@id='slider']"


class LoginPageCommonElements(BasePage):
    def __init__(self, driver):
        super(LoginPageCommonElements, self).__init__(driver)
        # Get username and password from the credential file
        credentials_file = os.path.join(os.path.dirname(__file__), 'login.credentials')
        self.username = Conf_Reader.get_value(credentials_file, 'LOGIN_USER')
        self.password = Conf_Reader.get_value(credentials_file, 'LOGIN_PASSWORD')

        # Page elements
        self._login_email_field = 'user_login'
        self._login_pass_field = 'user_pass'
        self._login_button = 'wp-submit'
        self._wp_admin_bar = "wpadminbar"

class WpVersionCheckElements(BasePage):
    def __init__(self, driver):
        super(WpVersionCheckElements, self).__init__(driver)

        # Page elements
        self._dashboard = "//h1[contains(text(), 'Dashboard')]"
        # self._dashboard = ".//*[@id='wpbody-content']/div[3]/h1"
        self._wp_version = "wp-version"
        self._at_glance_expand = ".//*[@id='dashboard_right_now']/button[@type='button']"

class NewPostEelements(BasePage):
    def __init__(self, driver):
        super(NewPostEelements, self).__init__(driver)

        # Page Elements
        self._menu_posts = "//li[@id='menu-posts']//div[contains(text(), 'Posts')]"
        self._add_new_post = "//a[@href='post-new.php']"
        self._add_new_post_title = "//h1[contains(text(), 'Add New Post')]"
        self._title_field = "//input[@name='post_title']"
        self._add_media_button = "//button[@id='insert-media-button']"
        self._edit_visibility = "//div[@id='visibility']//a[@class='edit-visibility hide-if-no-js']"
        self._visibility_private = "//input[@value='private']"
        self._visibility_ok_button = "//a[@class='save-post-visibility hide-if-no-js button']"
        self._uncategorized = "//label[contains(text(), 'Uncategorized')]//input[@type='checkbox']"  # Applicable for RTH
        self._publish_button = "//input[@id='publish']"
        self._content_body = "//div[@id='wp-content-editor-container']//iframe"

        self._upload_file = "//a[contains(text(), 'Upload Files')]"
        self._select_file = "//a[contains(text(), 'Select Files')]"
        self._input_file = "//input[starts-with(@id,'html5_')]"
        self._test_file = "//div[@class='media-sidebar visible']//div[starts-with(text(), 'panth-test')]"
        self._insert_into_post = "//button[contains(text(), 'Insert into post')]"

        self._view_post = "//a[contains(text(), 'View post')]"

        self._new_post_title = "//h1[contains(text(), 'Private: Pantheon Test Post')]"
        self._new_post_body = "//div[@class='entry-content']"
        self._new_post_image = "//div[@class='entry-content']/p/img"
