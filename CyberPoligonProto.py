import os

DB_FILE = "database.txt"

def load_database():
    if not os.path.exists(DB_FILE): # проверка на существование файла
        return []
    with open(DB_FILE, "r", encoding="utf-8") as file: # чтение файла
        return [line.strip() for line in file.readlines()] # удаление пробелов

def save_database(database):
    with open(DB_FILE, "w", encoding="utf-8") as file: # запись в файл
        for record in database:
            file.write(record + "\n")

def view_records(database):
    if not database:
        print("Записи отсутствуют.")
    else:
        for i, record in enumerate(database, 1): # нумерация
            print(f"{i}. {record}")

def add_record(database):
    record = input("Введите новую запись: ")
    database.append(record)
    save_database(database)
    print("Запись добавлена.")

def edit_record(database):
    view_records(database)
    try:
        record_num = int(input("Введите номер записи для редактирования: ")) - 1
        if 0 <= record_num < len(database):
            new_record = input("Введите новое значение записи: ")
            database[record_num] = new_record
            save_database(database)
            print("Запись изменена.")
        else:
            print("Неверный номер записи.")
    except ValueError:
        print("Введите корректный номер.")

def delete_record(database):
    view_records(database)
    try:
        record_num = int(input("Введите номер записи для удаления: ")) - 1
        if 0 <= record_num < len(database):
            deleted_record = database.pop(record_num)
            save_database(database)
            print(f"Запись '{deleted_record}' удалена.")
        else:
            print("Неверный номер записи.")
    except ValueError:
        print("Введите корректный номер.")

def main():
    database = load_database()
    while True:
        print("\n1. Просмотреть записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            view_records(database)
        elif choice == "2":
            add_record(database)
        elif choice == "3":
            edit_record(database)
        elif choice == "4":
            delete_record(database)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()