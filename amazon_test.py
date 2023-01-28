from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

NUMBER_OF_PRODUCTS = 0
product_name = []
product_asin = []
product_price = []
product_ratings = []
product_ratings_num = []
product_link = []


def get_product_name(item):
    try:
        name = item.find_element(
            By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]').text
        return name
    except NoSuchElementException:
        exit("No name found")


def get_product_asin(item):
    try:
        asin = item.get_attribute('data-asin')
        return asin
    except NoSuchElementException:
        exit("No asin found")


def get_price(item):
    try:
        price = item.find_element(
            By.XPATH, './/span[@class="a-price-whole"]').text
        return price
    except NoSuchElementException:
        exit("No price found")


def get_ratings(item):
    try:
        ratings = item.find_element(
            By.XPATH, './/div[@class="a-row a-size-small"]/span[1]'
        ).get_attribute('aria-label')
        return ratings
    except NoSuchElementException:
        return "No ratings found"


def get_ratings_num(item):
    try:
        ratings_num = item.find_element(
            By.XPATH, './/div[@class="a-row a-size-small"]/span[2]'
        ).get_attribute('aria-label')
        return ratings_num
    except NoSuchElementException:
        return "No ratings Number found"


def get_link(item):
    try:
        link = item.find_element(
            By.XPATH, './/h2/a').get_attribute('href')
        return link
    except NoSuchElementException:
        exit("No link found")


driver = webdriver.Chrome()
driver.get('https://www.amazon.in')

searchBar = driver.find_element(By.ID, 'twotabsearchtextbox')
driver.implicitly_wait(5)
item_to_be_searched = input("Enter product you want to search: ")
searchBar.send_keys(item_to_be_searched)
searchBar.submit()


items = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH, '//div[@data-component-type="s-search-result"]'
        )
    )
)

for item in items:
    product_name.append(get_product_name(item))

    product_asin.append(get_product_name(item))

    product_price.append(get_price(item))

    product_ratings.append(get_ratings(item))
    
    product_ratings_num.append(get_ratings_num(item))

    product_link.append(get_link(item))
