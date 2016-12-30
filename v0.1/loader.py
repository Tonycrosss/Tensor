# TODO Скачивание ссылки
# TODO Читаем библиотеку urllib
import urllib.request


class Downloader():
    def __init__(self):
        pass

    def download(self, link):
        response = urllib.request.urlopen('{}'.format(link))
        file = open('test.txt', 'w')
        file.write(str(response.read(), encoding='UTF-8'))


first_loader = Downloader()
first_loader.download('https://habrahabr.ru/post/134863/')