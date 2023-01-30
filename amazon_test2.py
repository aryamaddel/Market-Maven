import pandas as pd
from amazon_test import search_product, get_products_on_page, make_driver


driver = make_driver()
search_product(driver=driver, product='pens')
products = get_products_on_page(driver=driver)

df_products = pd.DataFrame(data=products, columns=[
                                 'product_name', 'product asin', 'product_price', 'product_rating', 'product_ratings_num', 'product_link'])
print(df_products)