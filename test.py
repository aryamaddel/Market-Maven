from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from os import system as sys

driver = webdriver.Chrome()

driver.get('https://www.amazon.in')

searchBar = driver.find_element(By.ID, 'twotabsearchtextbox')
driver.implicitly_wait(5)

sys('clear')
item_to_be_searched = input("Enter product you want to search: ")
searchBar.send_keys(item_to_be_searched)
searchBar.submit()


product_name = []
product_asin = []
product_price = []
product_ratings = []
product_ratings_num = []
product_link = []

sys('clear')
print("Finding all elements\n")
items = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH, '//div[@data-component-type="s-search-result"]'
        )
    )
)
sys('clear')
print("Found all elements\n")

sys('clear')
print("Getting product details\n")
for item in items:
    product_name.append(item.find_element(
        By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]').text)
    product_asin.append(item.get_attribute('data-asin'))
    product_price.append(item.find_element(
        By.XPATH, './/a//span//span//span[@class="a-price-whole"]').text)

    ratings_box = item.find_elements(
        By.XPATH, './/div[@class="a-row a-size-small"]/span')

    if ratings_box != []:
        ratings = ratings_box[0].get_attribute('aria-label')
        ratings_num = ratings_box[1].get_attribute('aria-label')
    else:
        ratings, ratings_num = 0, 0

    product_ratings.append(ratings)
    product_ratings_num.append(str(ratings_num))

    product_link.append(item.find_element(
        By.XPATH, './/a').get_attribute('href')
    )
sys('clear')
print("Got product details\n")

sys('clear')
print("searching for your product\n")
items_selected = []
for itemNo, name in enumerate(product_name):
    if item_to_be_searched.lower() in name.lower():
        info = []
        info.append(product_name[itemNo])
        info.append(product_price[itemNo])
        info.append(product_ratings[itemNo])
        info.append(product_ratings_num[itemNo])
        info.append(product_link[itemNo])
        items_selected.append(info)
sys('clear')
print("Found your products\n")


driver.implicitly_wait(5)
driver.close()
