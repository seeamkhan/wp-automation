import unittest, time
from basetestcase import BaseTestCase
from testcases import SiteOk
from testcases import Login
from testcases import WpVersionCheck
from testcases import SiteUp
from add_content import NewPost


class RunTestCases(BaseTestCase):
    def test010_site_up(self):
        SiteUp(self).site_up()

    def test020_site_check(self):
        SiteOk(self.driver).site_check()

    def test030_login(self):
        Login(self.driver).login_as_admin()

    def test040_wp_version_check(self):
        WpVersionCheck(self.driver).wp_version_check()

    def test050_add_post(self):
        NewPost(self.driver).add_new_post()

        time.sleep(1)
if __name__ == '__main__':
    unittest.main(verbosity=2)