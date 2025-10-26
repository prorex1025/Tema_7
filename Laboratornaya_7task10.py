# Задание 10: Создание CSV файла с задержкой
import csv
import datetime
import time


def create_csv_with_delay():
    """Создает CSV файл с данными и задержкой"""
    try:
        with open('rows_300.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)

            # Заголовки
            writer.writerow(['№', 'Секунда', 'Микросекунда'])

            print("Создание файла rows_300.csv...")

            for i in range(1, 301):
                # Получаем текущее время
                now = datetime.datetime.now()
                second = now.second
                microsecond = now.microsecond

                # Записываем строку
                writer.writerow([i, second, microsecond])

                # Задержка 0.01 секунды
                time.sleep(0.01)

                # Прогресс
                if i % 30 == 0:
                    print(f"Записано {i}/300 строк...")

        print("Файл 'rows_300.csv' успешно создан!")

        # Показываем первые 5 строк для проверки
        print("\nПервые 5 строк файла:")
        with open('rows_300.csv', 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if i < 6:  # 0 - заголовок, 1-5 - данные
                    print(line.strip())
                else:
                    break

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    create_csv_with_delay()