# Задание 5: Построчное чтение с with open()
def read_line_by_line():
    """Читает и выводит файл построчно"""
    try:
        with open('task1.txt', 'r', encoding='utf-8') as file:
            print("Построчный вывод файла:")
            print("-" * 30)
            for line_num, line in enumerate(file, 1):
                print(f"Строка {line_num}: {line.strip()}")
            print("-" * 30)

    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    read_line_by_line()