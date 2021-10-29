from bs4 import BeautifulSoup
import requests
import random



html_text = requests.get('https://unsplash.com/s/photos/2d-dice-imagews').text
soup = BeautifulSoup(html_text, 'lxml')
profs = soup.find_all('img')
aa = 0
bb = random.randint(0,10000000000)
for x in profs:
    aa+=1
    # print(x)
    # print(bb)
    try:
        response = requests.get(x['src'])
        file = open(f"Wallpers/{aa+bb}.png", "wb")
        file. write(response.content) 
    except:
        print(f"Image of {bb + aa+1} not exists")


print("Downloaded Successfully")


