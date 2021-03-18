from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()
driver.get(r"https://www.mueller.de/drogerie/lebensmittel/nahrung/")
time.sleep(2) 
acceptframe = driver.find_element_by_id("uc-btn-accept-banner").click()


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
    driver.get(r" https://www.mueller.de/drogerie/lebensmittel/nahrung/ ")
    search_bar = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/header/div[2]/div/div/form/div/div/input[1]")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)


enter_website()

driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/select/option[3]").click()

time.sleep(3)
price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[3]/div/div[1]/a[1]/div/div[5]/span[1]").get_attribute("innerHTML")
name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[3]/div/div[1]/a[1]/div/div[7]").get_attribute("innerHTML")

driver.quit()
print(price, name)
