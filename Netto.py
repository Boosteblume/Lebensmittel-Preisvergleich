import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()

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
drop.select_by_index(4)
time.sleep(3)

price = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/section/ul/li[1]/a/span/span[2]/span/ins/span").get_attribute("product__current-price--digits-before-comma js-productile-price")
name = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/section/ul/li[1]/a/span/span[1]/em[2]").get_attribute("product__title tc-product-name")
driver.quit()
