from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.amazon.in')

searchBar = driver.find_element(By.ID, 'twotabsearchtextbox')
driver.implicitly_wait(5)
searchBar.send_keys('iphone')
searchBar.submit()



# remaining code




driver.close()
