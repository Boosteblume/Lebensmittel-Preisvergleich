import requests
#Lisa sagt hallo
url = r"https://www.lidl.de/de/cimarosa/b1201"
r = requests.get(url)
with open('lidl.txt', 'w') as file:
    file.write(r.text)



