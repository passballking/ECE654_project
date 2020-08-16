import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def prep_login_action():
	options = Options()
	#options.add_argument("--headless")
	chromeDriverPath = "/home/qt/Desktop/654_test/test_project/chromedriver_84"
	driver = webdriver.Chrome(chromeDriverPath, options=options)
	driver.get("http://localhost:5000")
	sleep(0.5)
	driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
	sleep(0.5)
	driver.find_element_by_link_text("Register").click()
	sleep(0.5)
	driver.find_element_by_id("username").click()
	sleep(0.5)
	driver.find_element_by_id("username").send_keys(Keys.ENTER)
	sleep(0.5)
	driver.find_element_by_id("email").click()
	sleep(0.5)
	driver.find_element_by_id("email").clear()
	sleep(0.5)
	driver.find_element_by_id("email").send_keys("english@qq.com")
	sleep(0.5)
	driver.find_element_by_id("password").clear()
	sleep(0.5)
	driver.find_element_by_id("password").send_keys("user456")
	sleep(0.5)
	driver.find_element_by_id("confirm_password").clear()
	sleep(0.5)
	driver.find_element_by_id("confirm_password").send_keys("user456")
	sleep(0.5)
	driver.find_element_by_id("accept_tos").click()
	sleep(0.5)
	driver.find_element_by_id("submit").click()
	sleep(0.5)
	driver.close()

def test_clickable():
	prep_login_action()

	
