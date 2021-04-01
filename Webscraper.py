from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()

#Userinput for a given product
def pick_a_product():
    print("Hello, which product would you like to choose ? ")
    print("")

    choosen_product = input()

    print("You choose ", choosen_product)
    
    return choosen_product

#returns the choosen product
product = pick_a_product()

#writes the excel file
def writefile(shop, name, price):
    with open ("Results.csv", "a+") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([shop, name, price])  

#Webscraper for Real
def real(driver,product):
    #Uses Chromedriver to access shopsite, accept cookies and enter the product into the searchbar
    def enter_website():
        driver.get(r"https://www.real.de/")
        time.sleep(4)
        acceptframe = driver.find_element_by_xpath("/html/body/dialog/div/div[1]/button").click()
        time.sleep(3)
        search_bar = driver.find_element_by_class_name("rd-search__input")
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.RETURN)

    enter_website()

    #Selects filtering option; cheapest product
    time.sleep(3)
    select_menu = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div/section/div[2]/div/div/select")
    drop = Select(select_menu)
    drop.select_by_index(1)
    #Scrapes product price and name
    time.sleep(2)

    price = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/div[2]/div[1]").get_attribute("data-price")
    name = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/div[2]/div[1]").get_attribute("data-title")
    shop = "REAL"

    #Adds price and name of the corresponding shop to a csv file
    writefile(shop, name, price)

#Webscraper for Rossmann
def rossmann(driver, product):
    def enter_website():
        driver.get(r"https://www.rossmann.de/de/ernaehrung/c/olcat1_4")
        time.sleep(2)
        acceptframe = driver.find_element_by_id("onetrust-accept-btn-handler").click()
        time.sleep(2)
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
    shop = "Rossmann"
    
    writefile(shop, name, price)

#Webscraper for Müller
def mueller(driver, product):
    def enter_website():
        driver.get(r"https://www.mueller.de/drogerie/lebensmittel/nahrung/")
        time.sleep(2)
        acceptframe = driver.find_element_by_id("uc-btn-accept-banner").click()
        time.sleep(3)
        search_bar = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/header/div[3]/div/div/form/div/div/input[1]")
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.RETURN)

    enter_website()

    time.sleep(2)
    

    driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/select/option[3]").click()

    time.sleep(3)
    price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[3]/div/div[1]/a[1]/div/div[5]/span[1]").get_attribute("innerHTML")
    name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/div[2]/div[3]/div/div[1]/a[1]/div/div[7]").get_attribute("innerHTML")
    shop = "Müller"

    writefile(shop, name, price)

#Webscraper for Netto
def netto(driver, product):
    def enter_website():
        driver.get(r"https://www.netto-online.de/lebensmittel/")
        time.sleep(2)
        acceptframe = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[2]/a[3]").click()
        time.sleep(2)
        search_bar = driver.find_element_by_class_name("js-searchFormInput") 
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.RETURN)

    enter_website()
    time.sleep(2)
    select_menu = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/div[2]/section[2]/form/select")
    drop = Select(select_menu)
    drop.select_by_index(3)
    time.sleep(3)
    price = driver.find_element_by_xpath("/html/body/div[2]/main/div/div[3]/section/ul/li[1]/a/span/span[2]/span/ins/span").text
    price = price.replace("*", "€")
    name = driver.find_element_by_class_name("tc-product-name").text
    shop = "Netto"

    writefile(shop, name, price)
#Webscraper for Edeka24
def edeka24(driver, product):
    def enter_website():
        driver.get(r"https://www.edeka24.de/")
        time.sleep(2)
        acceptframe = driver.find_element_by_id("uc-btn-accept-banner").click()
        time.sleep(2)
        search_bar = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[7]/div/form/div/input[1]")
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.RETURN)


    enter_website()

    time.sleep(2)
    price = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/ul/li[1]/form/div/div/div[2]/div/a/h2").get_attribute("innerHTML")
    name = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/ul/li[1]/form/div/div/div[2]/div/div/div").get_attribute("innerHTML")
    shop = "Edeka24"

    writefile(shop, name, price)

#Webscraper for Alnatura
def alnatura(driver, product):
    def enter_website():
        driver.get(r"https://www.alnatura.de/de-de/")
        time.sleep(2)
        acceptframe = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[2]/a[3]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/header/div/div[3]/div/div[2]/ul/li[2]").click() #extraeingefügt
        search_bar = driver.find_element_by_xpath("/html/body/header/div/div[3]/div/div[2]/ul/div/div/div[3]/div[1]/input") #von Class zu xpath
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.RETURN)

    enter_website()
    time.sleep(5)
    #select_menu = driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/section/div[2]/div/div/select") #Kein Filter
    driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/div[2]/img").click() #Produkt muss auch ausgewählt werden, bevor Preis und Name sichtbar sind
    #drop = Select(select_menu)
    #drop.select_by_index(1)
    time.sleep(5)
    price = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div/div[1]/div[2]/dl/dd[6]").text
    name = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div/div[1]/div[2]/dl/dd[1]").text
    shop = "Alnatura"

    writefile(shop, name, price)

#Webscraper for Metro
def metro(driver, product):
    #load the page and accept the cookie
    driver.get(r"https://metro.de")
    driver.find_element_by_xpath("/html/body/div/footer/div/div/div[2]/div/div/div/div/div/div/div[2]/button").click()
    
    url = "https://produkte.metro.de/shop/search?q=" + product + "&sorting=price+asc"

    driver.get(url)
    time.sleep(4)

    name = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/span[1]/div/div/div/div[2]/div[1]/a/h4").get_attribute("innerHTML")

    price0 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/span[1]/div/div/div/div[3]/div/p[2]/span/span/span").get_attribute("innerHTML")
    price1 = price0.split("&")
    price = price1[0]
    shop = "METRO"

    writefile(shop, name, price)

#list of all shops
sites = [real, alnatura, rossmann, edeka24, metro, netto, mueller]


for site in sites:
    site(driver, product)


driver.quit()