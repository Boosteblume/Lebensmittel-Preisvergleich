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
driver = webdriver.Safari()
driver.get(r"https://produkte.metro.de/shop")
time.sleep(3)

#problemhere
acceptframe = driver.find_element_by_class_name("field-accept-button-name").click()


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
    driver.get(r"https://produkte.metro.de/shop")
    search_bar = driver.find_element_by_class_name("form-control")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)


enter_website()
#select_menu = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/section/div[2]/div/div/select")
#drop = Select(select_menu)
#drop.select_by_index(1)

time.sleep(3)
#price = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/div[2]/div[1]").get_attribute("data-price")
#name = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/div[2]/div[1]").get_attribute("data-title")

#driver.quit()
#print(price, name)