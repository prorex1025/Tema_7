# Задание 3: Статистика текстового файла
def text_statistics():
    """Анализирует текст и выводит статистику"""
    try:
        with open('input_task3.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        letter_count = 0
        word_count = 0
        line_count = len(lines)

        for line in lines:
            # Подсчет букв латинского алфавита
            for char in line:
                if char.isalpha() and char.isascii():
                    letter_count += 1

            # Подсчет слов
            words = line.split()
            word_count += len(words)

        print("Input file contains:")
        print(f"{letter_count} letters")
        print(f"{word_count} words")
        print(f"{line_count} lines")

    except FileNotFoundError:
        print("Ошибка: Файл 'input_task3.txt' не найден")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


if __name__ == "__main__":
    text_statistics()