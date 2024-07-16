FILE_NAME = 'phone_book.txt'
def read_file(file):
    try:
        with open(file, 'r', encoding = 'utf-8') as f: 
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)
    # try:
    #     with open(FILE_NAME, 'r', encoding = 'utf-8') as f: 
    #         lines = f.readlines()
    #         for line in lines:
    #             print(line)
    # except Exception as err:
    #     print('файла нет', 'error:', err)

def save_data(file):
    print('сохранение в файл')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronimyc = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding = 'utf-8') as f: 
        f.write(f'{first_name}, {last_name}, {patronimyc}, {phone_number}\n')
def search_data(contacts: list[str]):
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded 

def main():
    file_name = 'phone_book.txt'
    while True: 
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        answer = input('Выберите действие: ')
        if answer == '0':
            break
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)


if __name__ == '__main__':
    main()
