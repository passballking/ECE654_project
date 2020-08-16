import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

user_name = ''
def prep_login_action():
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
	login_name = driver.find_element_by_name('login')
	login_name.send_keys('qt')
	sleep(1)
	login_pass = driver.find_element_by_name('password')
	login_pass.send_keys('aaa')
	sleep(1)
	login_submit = driver.find_element_by_name('submit')
	login_submit.click()
	sleep(1)
	assert driver.current_url == 'http://localhost:5000/auth/login'
	warning = driver.find_element_by_xpath('.//div[@id="flashed-messages"]/div')
	warning_class = warning.get_attribute('class')
	warning_text = warning.text
	driver.close()
	return [warning_class, warning_text]

def test_login_fail():
	test_list = prep_login_action()
	assert test_list == ['alert alert-danger', 'x\nWrong username or password.']

	
