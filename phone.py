def load_contacts():
    contacts = []
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            surname, name, patronymic, phone = line.strip().split(',')
            contacts.append({'surname': surname, 'name': name, 'patronymic': patronymic, 'phone': phone})
    return contacts

def save_contacts(contacts):
    with open('contacts.txt', 'w', encoding='utf-8') as file:
        for contact in contacts:
            line = ','.join([contact['surname'], contact['name'], contact['patronymic'], contact['phone']])
            file.write(line + '\n')

def print_contacts(contacts):
    for contact in contacts:
        print('Фамилия:', contact['surname'])
        print('Имя:', contact['name'])
        print('Отчество:', contact['patronymic'])
        print('Телефон:', contact['phone'])
        print('---')

def search_contacts(keyword, contacts):
    found_contacts = []
    for contact in contacts:
        if keyword.lower() in contact['surname'].lower() or keyword.lower() in contact['name'].lower():
            found_contacts.append(contact)
    return found_contacts

def search_by_phone(phone, contacts):
    found_contacts = []
    for contact in contacts:
        if phone == contact['phone']:
            found_contacts.append(contact)
    return found_contacts

def add_contact(contacts):
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    contacts.append({'surname': surname, 'name': name, 'patronymic': patronymic, 'phone': phone})
    print('Контакт успешно добавлен.')

def update_contact(surname, name, contacts):
    for contact in contacts:
        if contact['surname'] == surname and contact['name'] == name:
            print('Введите новые данные для контакта', contact['surname'], contact['name'])
            contact['surname'] = input('Фамилия: ')
            contact['name'] = input('Имя: ')
            contact['patronymic'] = input('Отчество: ')
            contact['phone'] = input('Номер телефона: ')
            print('Контакт успешно обновлен.')
            return
    print('Контакт не найден.')

def delete_contact(surname, name, contacts):
    for contact in contacts:
        if contact['surname'] == surname and contact['name'] == name:
            contacts.remove(contact)
            print('Контакт успешно удален.')
            return
    print('Контакт не найден.')

def main():
    contacts = load_contacts()
    while True:
        print('--- Телефонный справочник ---')
        print('1. Показать все контакты')
        print('2. Поиск контактов по фамилии или имени')
        print('3. Поиск контактов по номеру телефона')
        print('4. Изменить контакт')
        print('5. Удалить контакт')
        print('6. Добавить контакт')
        print('0. Выход')
        choice = input('Выберите операцию: ')
        if choice == '1':
            print('Список контактов:')
            print_contacts(contacts)
        elif choice == '2':
            keyword = input('Введите ключевое слово для поиска: ')
            found_contacts = search_contacts(keyword, contacts)
            if found_contacts:
                print('Найденные контакты:')
                print_contacts(found_contacts)
            else:
                print('Контакты не найдены.')
        elif choice == '3':
            phone = input('Введите номер телефона для поиска: ')
            found_contacts = search_by_phone(phone, contacts)
            if found_contacts:
                print('Найденные контакты:')
                print_contacts(found_contacts)
            else:
                print('Контакты не найдены.')
        elif choice == '4':
            surname = input('Введите фамилию контакта для изменения: ')
            name = input('Введите имя контакта для изменения: ')
            update_contact(surname, name, contacts)
        elif choice == '5':
            surname = input('Введите фамилию контакта для удаления: ')
            name = input('Введите имя контакта для удаления: ')
            delete_contact(surname, name, contacts)
        elif choice == '6':
            add_contact(contacts)
        elif choice == '0':
            break
        else:
            print('Некорректный выбор. Попробуйте ещё раз.')

    save_contacts(contacts)

if __name__ == '__main__':
    main()

