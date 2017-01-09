from tclass import tenslinker










if __name__ == '__main__':
    user_link = input('Введите ссылку \n')
    print('Смотрим Вашу страницу... \n')
    tenslinker = tenslinker.TensLinker(user_link)  # Парсим ссылку
    clean_text = tenslinker.parse_link()  # получаем чистый текст
    tenslinker.text_writer(clean_text)   # Создаем папки и вписываем текст
    print('Программа выполнена!')


