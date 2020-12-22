#first idea / Only for Lebensmittel
# Website https://www.supermarktcheck.de/lebensmittel/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Safari()

driver.implicitly_wait(10)

driver.get(r"https://www.supermarktcheck.de/lebensmittel/")
driver.find_element_by_class_name("message-component").click()

def pick_a_product():
    print("Hello, which product would you like to choose ? ")
    print("")
    #Wie machen wir es bzgl. Tippfehlern bei der Produkt suche ? 
    #und wie machen wir es bzgl. Cola => Coca Cola, Pepsi Cola etc
    choosen_product = input()
    print("You choose ", choosen_product)
    
    return choosen_product

product= pick_a_product()

#def enter_website():
 #   driver.get(url)
 #   search_bar = driver.find_element_by_name("q")
 # search_bar.send_keys(product)
 #  search_bar.send_keys(Keys.RETURN)

#enter_website()

time.sleep(5)
driver.quit()
