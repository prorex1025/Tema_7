# Задание 5: Собственная задача - Анализатор логов
def log_analyzer():
    """
    Анализатор логов - читает файл с логами и выводит статистику:
    - Общее количество записей
    - Количество ошибок, предупреждений, информационных сообщений
    - Самые частые типы сообщений
    """

    def generate_sample_log():
        """Генерирует пример лог-файла для демонстрации"""
        sample_logs = [
            "2024-01-15 10:30:15 INFO: Application started successfully",
            "2024-01-15 10:31:22 WARNING: High memory usage detected",
            "2024-01-15 10:32:45 ERROR: Database connection failed",
            "2024-01-15 10:33:10 INFO: User login successful",
            "2024-01-15 10:34:20 ERROR: File not found",
            "2024-01-15 10:35:30 INFO: Data saved successfully",
            "2024-01-15 10:36:45 WARNING: Slow response time",
            "2024-01-15 10:37:50 INFO: Backup completed",
            "2024-01-15 10:38:55 ERROR: Permission denied",
            "2024-01-15 10:39:59 INFO: System shutdown"
        ]

        with open('app_log.txt', 'w', encoding='utf-8') as file:
            for log in sample_logs:
                file.write(log + '\n')
        print("Сгенерирован пример лог-файла 'app_log.txt'")

    def analyze_logs():
        """Анализирует лог-файл и выводит статистику"""
        try:
            with open('app_log.txt', 'r', encoding='utf-8') as file:
                logs = file.readlines()

            if not logs:
                print("Лог-файл пуст")
                return

            total_logs = len(logs)
            log_types = {'INFO': 0, 'WARNING': 0, 'ERROR': 0, 'OTHER': 0}

            for log in logs:
                if 'INFO:' in log:
                    log_types['INFO'] += 1
                elif 'WARNING:' in log:
                    log_types['WARNING'] += 1
                elif 'ERROR:' in log:
                    log_types['ERROR'] += 1
                else:
                    log_types['OTHER'] += 1

            # Вывод статистики
            print("\n" + "=" * 50)
            print("АНАЛИЗ ЛОГ-ФАЙЛА")
            print("=" * 50)
            print(f"Всего записей: {total_logs}")
            print(f"INFO: {log_types['INFO']} записей")
            print(f"WARNING: {log_types['WARNING']} записей")
            print(f"ERROR: {log_types['ERROR']} записей")
            print(f"OTHER: {log_types['OTHER']} записей")

            # Поиск самого частого типа
            most_common_type = max(log_types, key=log_types.get)
            print(f"Самый частый тип: {most_common_type}")

            # Примеры ошибок
            error_logs = [log for log in logs if 'ERROR:' in log]
            if error_logs:
                print(f"\nПримеры ошибок ({len(error_logs)}):")
                for i, error in enumerate(error_logs[:3], 1):
                    print(f"  {i}. {error.strip()}")

            print("=" * 50)

        except FileNotFoundError:
            print("Лог-файл 'app_log.txt' не найден")
            generate = input("Создать пример лог-файла? (y/n): ")
            if generate.lower() == 'y':
                generate_sample_log()
                analyze_logs()

    # Запуск анализатора
    analyze_logs()


if __name__ == "__main__":
    log_analyzer()