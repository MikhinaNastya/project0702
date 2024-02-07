import os
from cryptography.fernet import Fernet

# Чтение ключа из файла secret_key.txt
with open('data/secret_key.txt', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Папка для дешифрованных отчетов
decrypted_reports_folder = 'decrypted_reports'

# Проверка и создание папки decrypted_reports
if not os.path.exists(decrypted_reports_folder):
    os.makedirs(decrypted_reports_folder)

# Проверка отчетов в папке 'spy_reports' для каждого дня октября
for day in range(1, 32):
    for animal in ['cachalot', 'whale', 'cheetah', 'gorilla', 'dolphin', 'tiger', 'elephant', 'giraffe', 'penguin', 'koala']:
        report_filename = f"{day}_10_2023_{animal}.txt"

    if os.path.exists(report_filename):
        # Чтение зашифрованного отчета
        with open(report_filename, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Дешифровка отчета
        decrypted_data = cipher.decrypt(encrypted_data)

        # Сохранение дешифрованного отчета в другом месте
        decrypted_filename = os.path.join(decrypted_reports_folder, f"{day}_10_2023_{animal}.txt")
        with open(decrypted_filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
    else:
        print(f"{day}_10_2023_{animal}.txt")

print('Дешифрование завершено.')