# Задание 4: Фильтр запрещенных слов
def load_forbidden_words():
    """Загружает запрещенные слова из файла"""
    try:
        with open('forbidden_words.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            return set(content.lower().split())
    except FileNotFoundError:
        print("Ошибка: Файл 'forbidden_words.txt' не найден")
        return set()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return set()


def censor_text(text, forbidden_words):
    """Заменяет запрещенные слова на звездочки"""
    words = text.split()
    censored_words = []

    for word in words:
        # Очищаем слово от знаков препинания для проверки
        clean_word = ''.join(char for char in word if char.isalnum())

        if clean_word.lower() in forbidden_words:
            # Заменяем на звездочки той же длины
            censored_word = '*' * len(clean_word)

            # Восстанавливаем знаки препинания
            result_word = ''
            clean_chars = list(censored_word)
            for char in word:
                if char.isalnum():
                    if clean_chars:
                        result_word += clean_chars.pop(0)
                    else:
                        result_word += char
                else:
                    result_word += char
            censored_words.append(result_word)
        else:
            censored_words.append(word)

    return ' '.join(censored_words)


def main():
    """Основная функция"""
    forbidden_words = load_forbidden_words()

    if not forbidden_words:
        return

    print("Запрещенные слова:", forbidden_words)
    print("\nВведите текст для проверки (Ctrl+D/Ctrl+Z для завершения):")

    try:
        # Чтение многострочного ввода
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break

        input_text = '\n'.join(lines)

        if not input_text.strip():
            # Если ввод пустой, используем тестовый пример
            input_text = """Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!!"""
            print(f"\nИспользуется тестовый текст:\n{input_text}")

        print("\nРезультат:")
        censored_text = censor_text(input_text, forbidden_words)
        print(censored_text)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()