import urllib.request, re, os
from bs4 import BeautifulSoup


class TensLinker():
    def __init__(self, user_link):
        self.user_link = user_link

    def parse_link(self):
        print('Начинаем парсить Вашу страницу... \n')
        dirty_link = urllib.request.urlopen(
            '{}'.format(self.user_link)).read()  # Читаем ссылку
        soup = BeautifulSoup(dirty_link, "lxml")  # используя *суп* парсим
        text_title = soup.findAll('title')  # Вытаскиваем заголовок
        text_news = soup.findAll('p')  # вытаскиваем текст статьи
        dirty_text = str(text_title) + '\n' + str(
            text_news)  # соединяем заголовок и текст
        print('Парсинг страницы завершен! \n')
        print('Начинаем чистить страницу от ненужных символов... \n')
        clean_text = re.sub(r'(\<(/?[^>]+)>)', '',
                            str(dirty_text))  # Убираем теги
        clean_text2 = re.sub(r'\.,', '\n', str(
            clean_text))  # Меняем точку с запятой на отступ
        clean_text3 = re.sub(r'\[', ' ',
                             str(clean_text2))  # Убираем скобки лишние
        clean_text4 = re.sub(r'\]', '', str(clean_text3))
        print('Текст Чист! \n')
        return (clean_text4)

    def text_writer(self, clean_text):
        # TODO проверка на существование папки и не выдавать ошибку
        print('Создаем папки для хранения чистого текста... \n')
        try:
            os.makedirs(re.sub(r'http\S?://(www.)?', '',
                               self.user_link))  # Создаем нужные папки
        except:
            FileExistsError
            print('Папки уже существуют! Продолжаем...')
        os.chdir(re.sub(r'http\S?://(www.)?', '',
                        self.user_link))  # Переходим в новую директорию
        file = open('temp.txt', 'w')  # создаем временный текстовый файл
        file.write(clean_text)
        file = open('temp.txt', 'r')
        print('Записываем чистый текст в ./index.txt \n')
        text = file.readlines()
        for line in text:  # разбиваем статью по 80 символов, перенос по словам
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
            result.append(
                row)  # Цепляем последние слова, потому что до else не доходит
            file = open('index.txt', 'a', encoding='utf-8')
            for row in result:
                file.write(str(' '.join(row) + '\n'))
        os.remove('temp.txt')  # удаляем временный файл
