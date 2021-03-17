
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

PATH = "/Users/sophia/Documents/Lebensmittel-Preisvergleich/chromedriver"

driver = webdriver.Chrome(PATH)

#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome(PATH)
driver.get(r"https://www.mueller.de/drogerie/lebensmittel/nahrung/")
time.sleep(2) 
acceptframe = driver.find_element_by_id("uc-btn-accept-banner").click()


#choose a product 
def pick_a_product():
    print("Hello, which product would you like to choose ? ")
    print("")
    #Wie machen wir es bzgl. Tippfehlern bei der Produkt suche ? 
    #und wie machen wir es bzgl. Cola => Coca Cola, Pepsi Cola etc

    chosen_product = input()

    print("You choose ", chosen_product)
    
    return chosen_product

product= pick_a_product()

#search that product on the website
def enter_website():
    driver.get(r" https://www.mueller.de/drogerie/lebensmittel/nahrung/ ")
    search_bar = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/header/div[2]/div/div/form/div/div/input[1]")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)


enter_website()
select_menu = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div[2]/div/div[2]/div/div/div/div/div[2]/div/ul/li[1]/div[2]/div/button[2]/span")
drop = Select(select_menu)
drop.select_by_index(2)

time.sleep(3)
price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[3]/div/div[1]/a[1]/div/div[5]/span[1]").get_attribute("mu-product-tile__price")
name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[3]/div/div[1]/a[1]/div/div[7]").get_attribute("mu-product-tile__name")

driver.quit()
print(price, name)
