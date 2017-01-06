from tclass import tenslinker










if __name__ == '__main__':
    user_link = input('Введите ссылку \n')
    print('Смотрим Вашу страницу... \n')
    tenslinker = tenslinker.TensLinker(user_link)
    clean_text = tenslinker.parse_link()
    tenslinker.text_writer(clean_text)
    print('Программа выполнена!')


