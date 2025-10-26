# Задание 2: Учет расходов
import datetime


def expense_tracker():
    """Программа для учета расходов"""

    def add_expense():
        """Добавляет новую запись о расходе"""
        try:
            amount = float(input("Введите сумму расхода: "))
            category = input("Введите категорию расхода: ")
            description = input("Введите описание: ")

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open('expenses.txt', 'a', encoding='utf-8') as file:
                file.write(f"{timestamp}|{amount}|{category}|{description}\n")

            print("Запись успешно добавлена!\n")

        except ValueError:
            print("Ошибка: Сумма должна быть числом!\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    def show_expenses():
        """Показывает все записи о расходах"""
        try:
            with open('expenses.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            if not lines:
                print("Записей о расходах нет.\n")
                return

            total = 0
            print("\n" + "=" * 60)
            print("ИСТОРИЯ РАСХОДОВ:")
            print("=" * 60)

            for i, line in enumerate(lines, 1):
                parts = line.strip().split('|')
                if len(parts) == 4:
                    timestamp, amount, category, description = parts
                    total += float(amount)
                    print(f"{i}. {timestamp} | {amount} руб. | {category} | {description}")

            print("=" * 60)
            print(f"ОБЩАЯ СУММА: {total:.2f} руб.\n")

        except FileNotFoundError:
            print("Файл с расходами не найден. Сначала добавьте записи.\n")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}\n")

    # Основной цикл программы
    while True:
        print("УЧЕТ РАСХОДОВ")
        print("1 - Добавить расход")
        print("2 - Показать все расходы")
        print("3 - Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")


if __name__ == "__main__":
    expense_tracker()