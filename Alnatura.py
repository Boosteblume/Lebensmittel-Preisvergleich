from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

#launch the Browser and enter the webiste
#accept the cookies
driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/ChromeDriver/chromedriver')
driver.get(r"https://www.alnatura.de/de-de/")
time.sleep(5)
acceptframe = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[2]/a[3]").click()
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
    driver.get(r"https://www.alnatura.de/de-de/")
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
driver.back()
time.sleep(5)
driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div[2]/a/div[2]/img").click()
price2 = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div/div[1]/div[2]/dl/dd[6]").text
name2 = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div/div[1]/div[2]/dl/dd[1]").text
         
                  #price = np.array([1,1,1,1,1,1])
                #name = np.array([1,1,1,1,1])
                #i = 1
                #while i<6:
                # driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div[{0}]/a/div[2]/img".format(str(i))).click()
                    #price[i-1] = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div/div[1]/div[2]/dl/dd[6]").text  #get_attribute("product__usage")
                    #name[i-1] = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div/div[1]/div[2]/dl/dd[1]").text #get_attribute("product__storage")
                    #driver.back()
                    #time.sleep(5)
                    #i += 1
driver.quit()
                #array = np.array([price],[name])
                #for j in array:
                    #for x in j:
                        #print(j)
print(price, name, price2, name2)                        

with open ("test.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(price) 
#done with the webscraping 
#creating the dataframe
