import csv
import pandas as pd 
import numpy

#opens the file stored one of our pcs
file = pd.read_excel(r"C:\Users\maxbl\WebscrapingResult.xlsx")
file.dropna(inplace = True)

#is the function for the cheapest supermarket
def min_sum():
    #groups the entrys in the dataframe to Markt & Preis
    shop_prices = file.groupby(by=["Markt"])["Preis"].sum()

    #prints the cheapest store and the products you need to buy there
    print("The cheapest store is ", shop_prices.idxmin(), shop_prices.min(), "€")
    print("There you need to buy: ")
    grp = file.groupby(by=["Markt"])
    print(grp.get_group(shop_prices.idxmin()))


#asks the user if he has a favorite store and returns the price of it, else returns the cheapest store
def favorite_store():
    answer = input("Do you have a favorite store?: (yes/no) ")

    if answer == "yes":
        print(file["Markt"].unique())
        store = input("choose one: ")

        #groups the entries of the dataframe where the have a value Markt
        grp = file.groupby(by=["Markt"])

        #checks if the store the user entered is in the dataframe if it is 
        if store in file["Markt"].unique():
            print(grp.get_group(store))
            print(grp.get_group(store)["Preis"].astype(float).sum(), "€")
        
        else:
            print("Unknown Shop")
            
    else:
        min_sum()


    

favorite_store()