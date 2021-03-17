import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()
driver.get(r"https://www.netto-online.de/lebensmittel/")
time.sleep(2)
acceptframe = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[2]/a[3]").click()
#choose a product 
def pick_a_product():
    print("Hello, which product would you like to choose ? ")
    print("")
    #Wie machen wir es bzgl. Tippfehlern bei der Produkt suche ? 
    #und wie machen wir es bzgl. Cola => Coca Cola, Pepsi Cola etc
    choosen_product = input()
    print("You choose ", choosen_product)
    
    return choosen_product
product= pick_a_product()
#search that product on the website
def enter_website():
    driver.get(r"https://www.netto-online.de/lebensmittel/")
    search_bar = driver.find_element_by_class_name("js-searchFormInput") 
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)
enter_website()
select_menu = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/div[1]/section[2]/form/select")
drop = Select(select_menu)
drop.select_by_index(3)
time.sleep(3)
price = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/section/ul/li[1]/a/span/span[2]/span/ins/span").text
price = price.replace("*", "€")
name = driver.find_element_by_class_name("tc-product-name").text
driver.quit()
print(price, name)

with open ("test.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(price) 
#done with the webscraping 
#creating the dataframe

comparison_df = pd.DataFrame(columns=["Produkt Name", "Produkt Preis", "Supermarkt"])
comparison_df["Produkt Name"] = name
comparison_df["Produkt Preis"] = price 
