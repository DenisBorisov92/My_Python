def delete_str(file):

    print(f'Введите часть данных сотрудника(чтоб его инициализировать) которого хотим удалить из БД')
    name = input()
    lines = []
    
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if not name in line: lines += line

    with open(file, 'w', encoding="utf-8") as data:
            data.writelines(lines)
        
    print('Удаление произведено...')

