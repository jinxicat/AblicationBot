from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def signin(driver):
	dropdown = driver.find_element_by_id("navbarDropdown-10")
	dropdown.click()
	login = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/header/nav/div[2]/ul[2]/li[3]/div/a[1]')
	login.click()
	email = driver.find_element_by_id('email')
	email.send_keys('YOUR_EMAIL')
	psw = driver.find_element_by_id('password')
	psw.send_keys("YOUR_PASSWORD")
	signin = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/form/div[3]/div/button')
	signin.click()

def search_jobs(term, driver):
	driver.find_element_by_id('typeaheadInput').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
	driver.find_element_by_id('typeaheadInput').send_keys(term)
	driver.find_element_by_id('submitSearch-button').click()

def search_options(driver):
	driver.find_element_by_xpath("/html/body/dhi-js-dice-client/div/dhi-search-page-container/dhi-search-page/div/dhi-search-page-results/div/div[3]/div/dhi-filters-widget/div/section[2]/dhi-accordion[1]/div[2]/div/js-remote-options-filter/div/ul[1]/li[1]/span").click()
	driver.find_element_by_xpath("/html/body/dhi-js-dice-client/div/dhi-search-page-container/dhi-search-page/div/dhi-search-page-results/div/div[3]/div/dhi-filters-widget/div/section[2]/dhi-accordion[6]/div[2]/div/js-single-select-filter/div/div/span").click()

driver = webdriver.Firefox(executable_path='PATH_TO_GEKODRIVER')
driver.get("https://dice.com")
signin(driver)

while True:
	try:
		search_jobs("JOB_SEARCH_TERM", driver)
		break
	except Exception as e:
		print(e)
		time.sleep(1)

while True:
	try:
		search_options(driver)
		break
	except Exception as e:
		print(e)
		time.sleep(1)

# for search_card in driver.find_element_by_xpath("/html/body/dhi-js-dice-client/div/dhi-search-page-container/dhi-search-page/div/dhi-search-page-results/div/div[3]/js-search-display/div/div[3]/dhi-search-cards-widget/div")