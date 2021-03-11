from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()
driver.get(r"https://www.aldi-sued.de/de/homepage.html")
time.sleep(2)
#um cookies zu bestätigen gibt es keine ID zu suchen, sondern class. deswegen habe ich anstatt find_element_by_id - find_element_by_class_name. Ist es richtig?
acceptframe = driver.find_element_by_class_name("btn btn-primary btn-minwidth js-privacy-accept").click()
# oder als alternative direkt nach xpath suchen:
# acceptframe = driver.find_element_by_xpath(/html/body/div[2]/div/div/form/div[3]/div/div[2]/button).click()

#choose a product 
def pick_a_product():
    print("Hello, which product would you like to choose ? ")
    print("")

    choosen_product = input()

    print("You choose ", choosen_product)
    
    return choosen_product

product= pick_a_product()

#search that product on the website
def enter_website():
    driver.get(r"https://www.aldi-sued.de/de/homepage.html")
    search_bar = driver.find_element_by_class_name("form-control at-input-search_txt ui-autocomplete-input")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)


enter_website()
select_menu = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/section/div[2]/div/div/select")
drop = Select(select_menu)
drop.select_by_index(1)

time.sleep(3)
price = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/div[2]/div[1]").get_attribute("data-price")
name = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/div[2]/div[1]").get_attribute("data-title")

driver.quit()
print(price, name)

#done with the webscraping 
#creating the dataframe

comparison_df = pd.DataFrame(columns=["Produkt Name", "Produkt Preis", "Supermarkt"])
comparison_df["Produkt Name"] = name
comparison_df["Produkt Preis"] = price