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
	sleep(1)
	driver.find_element_by_xpath("//div[@id='navbar-collapse']/ul[2]/li/div/a/span").click()
	sleep(1)
	driver.find_element_by_id("login").click()
	sleep(1)
	driver.find_element_by_id("login").clear()
	sleep(1)
	driver.find_element_by_id("login").send_keys("user2")
	sleep(1)
	driver.find_element_by_id("password").clear()
	sleep(1)
	driver.find_element_by_id("password").send_keys("user2")
	sleep(1)
	driver.find_element_by_id("submit").click()
	sleep(1)
	driver.find_element_by_link_text("Welcome").click()
	sleep(1)
	driver.find_element_by_link_text("This is a first topic").click()
	sleep(1)
	driver.find_element_by_id("content").click()
	sleep(1)
	driver.find_element_by_id("content").send_keys("Great! This is a reply")
	sleep(1)
	driver.find_element_by_id("submit").click()
	sleep(0.5)
	driver.close()

def test_clickable():
	prep_login_action()

	
