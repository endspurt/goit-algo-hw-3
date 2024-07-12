import os
import shutil
import sys
import argparse

# Функція для парсингу аргументів командного рядка
def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів та сортування за розширенням.")
    parser.add_argument('src', type=str, help='Шлях до вихідної директорії.')
    parser.add_argument('dst', type=str, nargs='?', default='dist', help='Шлях до директорії призначення.')
    return parser.parse_args()

# Функція для рекурсивного копіювання файлів
def copy_files(src, dst):
    # Перевірка, чи існує директорія призначення, якщо ні - створюється
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    # Перебір всіх елементів у вихідній директорії
    for item in os.listdir(src):
        s = os.path.join(src, item)
        # Якщо елемент є директорією, викликається функція рекурсивно
        if os.path.isdir(s):
            copy_files(s, dst)
        else:
            # Отримання розширення файлу
            ext = item.split('.')[-1]
            dest_dir = os.path.join(dst, ext)
            # Перевірка, чи існує піддиректорія для цього розширення, якщо ні - створюється
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # Копіювання файлу до відповідної піддиректорії
            shutil.copy2(s, os.path.join(dest_dir, item))

# Основна функція програми
def main():
    args = parse_arguments()
    try:
        # Виклик функції копіювання файлів з отриманими аргументами
        copy_files(args.src, args.dst)
        print("Файли успішно скопійовані.")
    except Exception as e:
        # Виведення повідомлення про помилку у разі виникнення винятку
        print(f"Помилка: {e}")

# Виконання основної функції при запуску скрипта
if __name__ == "__main__":
    main()

