from base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class AllCustomMethods(BasePage):
    def __init__(self, driver):
        super(AllCustomMethods, self).__init__(driver)

    def verify(self, elem, time=5):
        elem_status = ''
        try:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, elem)))
            elem_status = "%s element found." % elem
        except:
            elem_status = "Driver did not recognize '%s' element." % elem
            print elem_status
        return elem_status

class Logger():
    def logger(self, *message):
        log = '\n'.join(message)
        return log

    def save_log(self, log):
        target = open("test-result-log", 'a')
        # target.truncate()
        target.write("\n\n%s" % log)
        target.close()