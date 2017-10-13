from   selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

profile = webdriver.FirefoxProfile(r'D:\PythonScript\Selenium')
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox()
browser.get("https://10.10.10.1:33/admin/")
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
submit = browser.find_element_by_id("loginButton")
username.send_keys("admin")
password.send_keys("user")
submit.click()

