# Задание 8: Рекурсивный обход директорий
import os


def print_docs(directory):
    """Выводит содержимое директории и всех поддиректорий"""
    try:
        print(f"Содержимое директории: {directory}")
        print("=" * 50)

        for root, dirs, files in os.walk(directory):
            # Вычисляем уровень вложенности для отступов
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 2 * level

            print(f"{indent}📁 {os.path.basename(root)}/")
            sub_indent = ' ' * 2 * (level + 1)

            for file in files:
                print(f"{sub_indent}📄 {file}")

            # Если нет подпапок и файлов
            if not dirs and not files:
                print(f"{sub_indent}(пусто)")

            print()  # Пустая строка между папками

    except FileNotFoundError:
        print(f"Ошибка: Директория '{directory}' не найдена")
    except PermissionError:
        print(f"Ошибка: Нет доступа к директории '{directory}'")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    # Можно изменить на любую существующую папку
    test_directory = "."  # Текущая директория
    print_docs(test_directory)