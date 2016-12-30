# TODO Скачивание ссылки
# TODO Читаем библиотеку urllib
import urllib.request, re
from bs4 import BeautifulSoup

def parse_link(link):
    dirty_link = urllib.request.urlopen('{}'.format(link)).read()
    soup = BeautifulSoup(dirty_link, "lxml")
    text_title = soup.findAll('title')
    text_news = soup.findAll('p')
    dirty_text = str(text_title) + '\n' + '\n' + str(text_news)
    return dirty_text


def cleaner(dirty_text):
    clean_text = re.sub(r'(\<(/?[^>]+)>)', '', str(dirty_text))
    clean_text2 = re.sub(r'\.,', '\n\n', str(clean_text))
    clean_text3 = re.sub(r'\[', ' ', str(clean_text2))
    clean_text4 = re.sub(r'\]', '', str(clean_text3))
    print(clean_text4)
    return clean_text4

def text_writer(clean_text):
    #TODO Имя файла должно быть как ссылка
    file = open('lenta.txt', 'w')
    file.write(clean_text)





first_link = parse_link('https://lenta.ru/news/2016/12/30/otkaz/')
first_clear_text = cleaner(first_link)
text_writer(first_clear_text)

