import csv
import pandas as pd 
import numpy


file = pd.read_excel(r"C:\Users\maxbl\WebscrapingResult.xlsx")

#file.set_index('Markt', inplace=True)

file.dropna(inplace = True)


def min_sum():
    shop_prices = file.groupby(by=["Markt"])["Preis"].sum()
    print("The cheapest store is ", shop_prices.idxmin(), shop_prices.min(), "€")
    print("There you need to buy: ")
    
    grp = file.groupby(by=["Markt"])
    print(grp.get_group(shop_prices.idxmin()))


#asks the user if he has a favorite and returns the price sum
def favorite_store():

    answer = input("Do you have a favorite store?: (yes/no) ")

    if answer == "yes":

        print(file["Markt"].unique())
        store = input("choose one: ")
        
        grp = file.groupby(by=["Markt"])

        if store in file["Markt"].unique():
            print(grp.get_group(store))
            print(grp.get_group(store)["Preis"].astype(float).sum(), "€")
        
        else:
            print("Unknown Shop")
    else:
        min_sum()


    

favorite_store()