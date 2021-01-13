#first idea / Only for Lebensmittel
# Website https://www.supermarktcheck.de/lebensmittel/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver import chrome

PATH = "/Users/maxbl/OneDrive/Desktop/Coding/chromedriver.exe"

driver = webdriver.Chrome(PATH)


driver.get(r"https://www.supermarktcheck.de/lebensmittel/")
time.sleep(10)
acceptframe = driver.find_element_by_id("sp_message_iframe_233610")
driver.switch_to_frame(acceptframe)
driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/button").click()
time.sleep(10)
driver.quit()


#driver.find_element_by_class_name("message-component").click()

def pick_a_product():
    print("Hello, which product would you like to choose ? ")
    print("")
    #Wie machen wir es bzgl. Tippfehlern bei der Produkt suche ? 
    #und wie machen wir es bzgl. Cola => Coca Cola, Pepsi Cola etc
    choosen_product = input()
    print("You choose ", choosen_product)
    
    return choosen_product

#product= pick_a_product()

#def enter_website():
 #   driver.get(url)
 #   search_bar = driver.find_element_by_name("q")
 # search_bar.send_keys(product)
 #  search_bar.send_keys(Keys.RETURN)

#enter_website()


