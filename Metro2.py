from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome()
driver.get(r"https://metro.de")
driver.find_element_by_xpath("/html/body/div/footer/div/div/div[2]/div/div/div/div/div/div/div[2]/button").click()

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

url = "https://produkte.metro.de/shop/search?q="+product+"&sorting=price+asc"

driver.get(url)
time.sleep(4)
name = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/span[1]/div/div/div/div[2]/div[1]/a/h4").get_attribute("innerHTML")

price0 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/span[1]/div/div/div/div[3]/div/p[2]/span/span/span").get_attribute("innerHTML")
price1 = price0.split("&")
price = price1[0]

print(name, price)
