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
driver.get(r"https://www.interspar.at/")
time.sleep(2)
acceptframe = driver.find_element_by_id("cmpbntyestxt").click()
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
    driver.get(r"https://www.interspar.at/")
    search_bar = driver.find_element_by_class_name("metasearch-search-field search-input") 
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)

enter_website()

# ab hier bin ich noch unsicher. Wie wählt man das richtige infos daraus? muss man noch ein mal klicken um zum richtigen Preis zu kommen
select_menu = driver.find_element_by_xpath("...").click()
time.sleep(3)

price = driver.find_element_by_xpath("...").text
name = driver.find_element_by_class_name("...").text
driver.quit()
print(price, name)