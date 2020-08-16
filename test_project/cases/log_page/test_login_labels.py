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
	label_list = []
	la_title = driver.find_element_by_xpath('.//div[@class="panel-heading page-head"]').text
	label_list.append(la_title)
	la_usernameOrEmail = driver.find_element_by_xpath('.//form/div[1]/label').text
	label_list.append(la_usernameOrEmail)
	la_password = driver.find_element_by_xpath('.//form/div[2]/label').text
	label_list.append(la_password)
	la_rememberme = driver.find_element_by_xpath('.//form/div[3]/div/div/label').text
	label_list.append(la_rememberme)
	la_not_a_member = driver.find_element_by_xpath('.//form//a[@href="/auth/register"]/small').text
	label_list.append(la_not_a_member)
	la_forgot_password = driver.find_element_by_xpath('.//form//a[@href="/auth/reset-password"]/small').text
	label_list.append(la_forgot_password)
	driver.close()
	return label_list

def test_login_labels():
	test_list = prep_login_action()
	true_list = ['Login', 'Username or Email address', 'Password', 'Remember me', 'Not a member yet?', 'Forgot your Password?']
	assert test_list == true_list

	
