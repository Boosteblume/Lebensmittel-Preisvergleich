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
driver.get(r"https://metro.de/")
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
    driver.get(r"https://metro.de/")
    driver.find_element_by_xpath("/html/body/div[1]/header/div/div/div/div[1]/div/div/div/div/div/div[3]/div/a[2]").click()
    time.sleep(4)
    search_bar = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/nav/div/table/tbody/tr/td[2]/div/div/form/div/div/span/input")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)


enter_website()

#dann wieder ul mit lis / einfach 2 click befehle
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div/button").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div/ul/li[3]").click()

time.sleep(3)
price0 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/span[1]/div/div/div/div[3]/div/p[2]/span/span/span").get_attribute("innerHTML")
price1 = price0.split("&")
price = price1[0]
name = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/span[1]/div/div/div/div[2]/div[1]/a/h4").get_attribute("innerHTML")
#driver.quit()
print(price, name)