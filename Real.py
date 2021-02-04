from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import json
from bs4 import BeautifulSoup
import requests


#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()
driver.get(r"https://www.real.de/")
time.sleep(5)
acceptframe = driver.find_element_by_id("consentSubmit").click()


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
    driver.get(r"https://www.real.de/")
    search_bar = driver.find_element_by_class_name("rd-header__search-field")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)

enter_website()



#to get one artikel
test = driver.find_element_by_css_selector("#rd-item-grid > div:nth-child(5)")
test.get_attribute("outerHTML")


#mulitple but keyword brote is shit
test2 = driver.find_elements_by_xpath('//*[contains(text(), "brot")]')
#test[].get_attribute("outerHTML")

#if u know the brand it starts at element 3 so vesta[2]
vesta = driver.find_elements_by_xpath('//*[contains(text(), "Vestakorn")]')

#driver.quit()
#trying to store the Results in this variable / should be a string
#search_results = driver.page_source

#DataTitle für Markenname und Produktname
#metacontent = Price


#new idea

url = driver.current_url
url_code = requests.get(url)
url_content = url_code.text
soup = BeautifulSoup(url_content)
#raw = soup.findAll()
