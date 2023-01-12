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
    print("Getting product name")
    product_name.append(item.find_element(
        By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]').text)

    print("Getting product asin")
    product_asin.append(item.get_attribute('data-asin'))

    print("Getting product price")
    product_price.append(item.find_element(
        By.XPATH, './/span[@class="a-price-whole"]').text)

    print("Getting product ratings")
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
        By.XPATH, './/h2/a').get_attribute('href')
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

for prod_no, item in enumerate(items_selected):
    print(f"Number: {prod_no+1}")
    print(f"Name: {item[0]}")
    print(f"Price: {item[1]}")
    print(f"Ratings: {item[2]}")
    print(f"Number of Ratings: {item[3]}")
    print(f"Link: {item[4]}")
    print("\n\n")


prod_no = int(input("Enter the number of the product you want to buy: "))
sys('clear')
print("Opening the product link\n")
driver.get(items_selected[prod_no-1][4])
sys('clear')
print("Opened the product link\n")


# driver.implicitly_wait(5)
# driver.close()

# STILL MINOR ERRORS ARE THERE