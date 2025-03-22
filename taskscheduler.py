diary = []

def add_task(task):
    diary.append({'task':task, 'check_mark':'[ ]'})
    print(f'Задача "{task}" успешно добавлена!')

def complete_task(index):
    diary[index]['check_mark'] = '[x]'
    print(f'Задача "{diary[index]["task"]}" выполнена!')

def delete_task(index):
    print(f'Задача "{diary[index]['task']}" успешно удалена!')
    diary.pop(index)   

def view_task():
    for i, tas in enumerate(diary):
        print(f'[{i}] {tas['check_mark']} {tas['task']}')

while True:
    vvod = input()
    if vvod == 'exit':
        print('До свидания!')
        break

    try:
        parts = vvod.split(maxsplit=1)
        command = parts[0]
        value = parts[1] if len(parts) > 1 else None

        if command == 'add' and value:
            add_task(value)
        elif command == 'complete' and value:
            complete_task(int(value))
        elif command == 'delete' and value:
            delete_task(int(value))
        elif command == 'view':
            view_task()
        else:
            print('Ошибка: Неверная команда или отсутствует значение!')
    except ValueError:
        print('Ошибка: Некорректное значение для команды!')
    except IndexError:
        print('Ошибка: Неверный индекс задачи!')

        #123


    