# Задание 7: Перезапись файла
def rewrite_file():
    """Перезаписывает файл новыми данными"""
    try:
        # Новые данные для записи
        new_data = [
            "Это первая строка новых данных",
            "Вторая строка с другой информацией",
            "Третья строка перезаписанного файла",
            "И заключительная четвертая строка"
        ]

        # Перезаписываем файл
        with open('task1.txt', 'w', encoding='utf-8') as file:
            for line in new_data:
                file.write(line + '\n')

        # Проверяем запись
        with open('task1.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        print("Файл успешно перезаписан!")
        print("Новое содержимое:")
        print("-" * 40)
        print(content)
        print("-" * 40)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    rewrite_file()