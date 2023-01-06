from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://www.amazon.in')

searchBar = driver.find_element(By.ID, 'twotabsearchtextbox')
driver.implicitly_wait(5)
searchBar.send_keys('ps5')
searchBar.submit()


product_name = []
product_asin = []
product_price = []
product_ratings = []
product_ratings_num = []
product_link = []

items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.XPATH, '//div[@data-component-type="s-search-result"]')))

for item in items:
    product_name.append(item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]').text)
    product_asin.append(item.get_attribute('data-asin'))
    product_price.append(item.find_element(By.XPATH, './/span[2]').text)
    product_ratings.append(item.find_element(By.XPATH, './/span[1]').text)
    product_ratings_num.append(item.find_element(By.XPATH, './/span[2]').text)
    product_link.append(item.find_element(By.XPATH, './/a').get_attribute('href'))

# FIX THIS PART ⬆️⬆️⬆️


print(product_name)
print(product_asin)
print(product_price)
print(product_ratings)
print(product_ratings_num)
print(product_link)

driver.implicitly_wait(5)
driver.close()
print("omg it worked")
