from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='PATH_TO_GEKODRIVER')
driver.get("https://www.dice.com/jobs?q=helpdesk&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.easyApply=true&filters.isRemote=true&language=en&eid=S2Q_,6Q_0")

while True:

	try:

		#find all company names
		containers = driver.find_elements_by_class_name("card-header")
		for container in containers:
			company_name = container.find_element_by_class_name("card-company").find_element_by_tag_name('a').text
			print(company_name)

		#find all job titles
		containers = driver.find_elements_by_class_name("card-header")
		for container in containers:
			job_title = container.find_element_by_class_name('card-title-link').text
			print(job_title)

		#find all job links
		containers = driver.find_elements_by_class_name("card-header")
		for container in containers:
			job_link = container.find_element_by_class_name('card-title-link').get_attribute('href')
			print(job_link)

		driver.find_element_by_xpath('/html/body/dhi-js-dice-client/div/dhi-search-page-container/dhi-search-page/div/dhi-search-page-results/div/div[3]/js-search-display/div/div[4]/div[1]/js-search-pagination-container/pagination/ul/li[7]/a').click()

		time.sleep(10)

	except Exception as e:
		print(e)
		break