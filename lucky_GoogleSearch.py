#! python3
# Открывает несколько результатов поиска с помощью Google
# Windows+R - lucky <текст поиска>

import requests, sys, webbrowser, bs4
proxies = {
    "http": "http://user:password@10.10.10.1:8080/",
    "https": "https://user:password@10.10.10.1:8080/"}

print('Гуглим...')
res = requests.get('https://www.google.com/search?q='+' '.join(sys.argv[1:]), proxies=proxies)
res.raise_for_status()
# извлечение первых несколькоих найденных ссылок
soup = bs4.BeautifulSoup(res.text,"html.parser")
# Открытие отдельной вкладки для каждого результата
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))

