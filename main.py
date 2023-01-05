from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.amazon.in')

searchBar = driver.find_element(By.ID, 'twotabsearchtextbox')
driver.implicitly_wait(5)
searchBar.send_keys('iphone')
searchBar.submit()


product_name = []
product_asin = []
product_price = []
product_ratings = []
product_ratings_num = []
product_link = []

items = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
print(items)


driver.implicitly_wait(5)
driver.close()