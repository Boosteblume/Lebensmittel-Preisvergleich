from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()
driver.get(r"https://www.edeka24.de/")

time.sleep(4)

acceptframe = driver.find_element_by_id("uc-btn-accept-banner").click()
time.sleep(2)

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
    driver.get(r"https://www.edeka24.de/")
    search_bar = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[7]/div/form/div/input[1]")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)


enter_website()

time.sleep(3)
price = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/ul/li[1]/form/div/div/div[2]/div/a/h2").get_attribute("innerHTML")
name = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/ul/li[1]/form/div/div/div[2]/div/div/div").get_attribute("innerHTML")

driver.quit()
print(price, name)
