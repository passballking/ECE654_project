import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

user_name = ''
def test_forget_password():
	options = Options()
	options.add_argument("--headless")
	chromeDriverPath = "/home/qt/Desktop/654_test/test_project/chromedriver_84"
	driver = webdriver.Chrome(chromeDriverPath, options=options)
	driver.get("http://localhost:5000")
	try:
		login_button = driver.find_element_by_link_text('Login')
		login_button.click()
	except NoSuchElementException:
		pass
	sleep(1)
	url_1 = driver.current_url
	assert driver.current_url == 'http://localhost:5000/auth/login'
	sleep(0.5)
	login_not_a_member = driver.find_element_by_xpath('//form/div[5]/div/a[2]')
	login_not_a_member.click()
	sleep(1)
	url_2 = driver.current_url
	assert driver.current_url == 'http://localhost:5000/auth/reset-password'
	driver.close()

	
