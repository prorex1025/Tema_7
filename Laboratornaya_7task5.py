# Задание 6: Добавление новой строки в файл
def add_line_to_file():
    """Добавляет новую строку в файл и выводит содержимое"""
    try:
        # Добавляем новую строку
        with open('task1.txt', 'a', encoding='utf-8') as file:
            file.write("\nНовая добавленная строка.")

        # Читаем и выводим обновленный файл
        with open('task1.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        print("Обновленное содержимое файла:")
        print("-" * 40)
        print(content)
        print("-" * 40)
        print("Изменения сохранены в файле!")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    add_line_to_file()