from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://google.com/')
js_script = "window.alert('This is an alert..');"
driver.execute_script(js_script)
sleep(5)
driver.quit()