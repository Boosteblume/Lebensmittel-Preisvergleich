from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


#launch the Browser and enter the webiste
#accept the cookies
PATH = "/Users/maxbl/OneDrive/Desktop/Coding/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(r"https://www.edeka.de/unsere-marken/suche-nach-edeka-produkten/suche-nach-edeka-produkten/sortimentkategorien.jsp")
time.sleep(5)
acceptframe = driver.find_element_by_id("popin_tc_privacy_button_2").click()


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
    driver.get(r"https://www.edeka.de/unsere-marken/suche-nach-edeka-produkten/suche-nach-edeka-produkten/sortimentkategorien.jsp")
    search_bar = driver.find_element_by_id("textsearchproduct")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)

enter_website()

#trying to store the Results in this variable
search_results = driver.page_source


#def choose_a_brand():
    #for brands in search_results:


time.sleep(5)
#driver.quit()