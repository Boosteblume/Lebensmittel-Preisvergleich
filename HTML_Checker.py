import requests

url = r"https://www.rewe.de/"
r = requests.get(url).content()
# with open('real.txt', 'w') as file:
#     file.write(r.text)
#     print(file)
print(r)


