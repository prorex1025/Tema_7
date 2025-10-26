# Задание 2: Чтение первой строки с open()/close()
def read_first_line():
    """Читает и выводит первую строку файла"""
    file = None
    try:
        file = open('task1.txt', 'r', encoding='utf-8')
        first_line = file.readline()
        print("Первая строка файла:")
        print(first_line.strip())
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if file:
            file.close()

if __name__ == "__main__":
    read_first_line()