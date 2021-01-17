import requests

url = r"https://www.real.de/item/search/?search_value=brot"
r = requests.get(url)
with open('real.txt', 'w') as file:
    file.write(r.text)
    print(file)



