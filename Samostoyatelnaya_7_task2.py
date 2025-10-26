# Задание 3: Чтение всех строк в массив с open()/close()
def read_all_lines():
    """Читает все строки файла в массив"""
    file = None
    try:
        file = open('task1.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        print("Все строки файла в массиве:")
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line.strip()}")
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if file:
            file.close()

if __name__ == "__main__":
    read_all_lines()