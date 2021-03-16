from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# import pandas as pd
# import numpy as np
# import matplotlib as mlt
# import matplotlib.pyplot as plt

#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()
driver.get(r"https://www.rossmann.de/de/ernaehrung/c/olcat1_4")
time.sleep(2)
acceptframe = driver.find_element_by_id("onetrust-accept-btn-handler").click()


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
    driver.get(r"https://www.rossmann.de/de/ernaehrung/c/olcat1_4")
    search_bar = driver.find_element_by_class_name("rm-searchbar__field")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)


enter_website()

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/main/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/form/div[1]/div/ul").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/main/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/form/div[1]/div/ul/li[5]").click()
time.sleep(3)

price = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/main/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div[2]/div[3]/div[1]").get_attribute("content")
name = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/main/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div[2]/div[2]/a").get_attribute("data-product-name")

driver.quit()
print(price, name)