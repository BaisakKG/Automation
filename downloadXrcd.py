#! python3
# Загружает все комиксы XKCD.com

import requests,os, bs4
proxies = {
    "http": "http://user:password@10.10.10.1:8080/",
    "https": "https://user:password@10.10.10.1:8080/"}

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True) # сохраняем комикс в папке ./xkcd

while not url.endswith('#'):
    # Загрузка страницы
    print('Загружается страница %s...' % url)
    res = requests.get(url, proxies=proxies)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    #Поиск URL-адреса изображения комикса
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалос найти изоброжение комикса.')
    else:
        comicUrl = 'http:'+str(comicElem[0].get('src'))
        # Загрузить изображение
        print('Загружается изоброжжение %s...' % (comicUrl))
        res = requests.get(comicUrl,proxies=proxies)
        res.raise_for_status()

    # Сохраниение изображения в папке ./xkcd
    imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close ()

    # Получение URL-адреса кнопки Prev.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')

print('Готово!')