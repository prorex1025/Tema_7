# Задание 4: Чтение всех строк с with open()
def read_with_context_manager():
    """Читает все строки файла используя with open()"""
    try:
        with open('task1.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        print("Все строки файла (with open):")
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line.strip()}")

    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    read_with_context_manager()