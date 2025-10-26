# Задание 9: Поиск самого длинного слова
def find_longest_word():
    """Находит самое длинное слово в файле"""
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            words = file.read().split()

        if not words:
            print("Файл пуст")
            return

        # Находим максимальную длину
        max_length = max(len(word) for word in words)

        # Находим все слова с максимальной длиной
        longest_words = [word for word in words if len(word) == max_length]

        print(f"Самое длинное слово(а) ({max_length} символов):")
        for word in set(longest_words):  # set для уникальности
            print(f"  '{word}'")

    except FileNotFoundError:
        print("Ошибка: Файл 'input.txt' не найден")

        # Создаем тестовый файл
        sample_text = """Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю."""

        with open('input.txt', 'w', encoding='utf-8') as file:
            file.write(sample_text)
        print("Создан тестовый файл 'input.txt'")
        find_longest_word()  # Запускаем снова

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    find_longest_word()