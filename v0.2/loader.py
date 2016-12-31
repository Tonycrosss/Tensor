import urllib.request, re
from bs4 import BeautifulSoup

def parse_link(link):
    # TODO нужно title еще прикрутить
    dirty_link = urllib.request.urlopen('{}'.format(link)).read()
    soup = BeautifulSoup(dirty_link, "lxml")
    text_title = soup.findAll('title') # Вытаскиваем заголовок
    text_news = soup.findAll('p') # вытаскиваем текст статьи
    dirty_text = str(text_title) + '\n' + str(text_news) # соединяем
    return dirty_text


def cleaner(dirty_text):
    # TODO Написать регулярку, которая будет очищать все и сразу

    clean_text = re.sub(r'(\<(/?[^>]+)>)', '', str(dirty_text)) # Убираем теги
    clean_text2 = re.sub(r'\.,', '\n', str(clean_text)) # Меняем точку с запятой на отступ
    clean_text3 = re.sub(r'\[', ' ', str(clean_text2)) # Убираем скобки лишние
    clean_text4 = re.sub(r'\]', '', str(clean_text3))
    return clean_text4

def text_writer(clean_text):
    # TODO Имя файла должно быть как ссылка
    # TODO попробовать объеденить с форматтером
    file = open('lenta.txt', 'w')
    file.write(clean_text)

def formatter():
    file = open('lenta.txt', 'r')
    text = file.readlines()
    for line in text:
        spl_text = line.split(' ')
        row = []
        result = []
        for word in spl_text:
            if len(' '.join(row)) <= 80:
                row.append(word)
            else:
                result.append(row)
                row = []
                row.append(word)
        result.append(row)  # Цепляем последние слова, потому что до else не доходит
        file = open('newnew', 'a', encoding='utf-8')
        for row in result:
            file.write(str(' '.join(row) + '\n'))




first_link = parse_link('https://lenta.ru/news/2016/12/30/otkaz/')
first_clear_text = cleaner(first_link)
text_writer(first_clear_text)
formatter()

# TODO Удаление скаченного не формаченного файла в конце сеанса
# в либреофис странно читается, в остальном везде гуд



