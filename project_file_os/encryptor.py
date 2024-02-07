import os
from cryptography.fernet import Fernet

# Папка для зашифрованных отчетов
encrypted_reports_folder = 'encrypted_reports'

# Проверка и создание папки encrypted_reports
if not os.path.exists(encrypted_reports_folder):
    os.makedirs(encrypted_reports_folder)

# Проверить папку 'decrypted_reports'
for filename in os.listdir(decrypted_reports_folder):
    if 'c' not in filename.lower():  # Если нет буквы "c" в нижнем регистре
        report_path = os.path.join(decrypted_reports_folder, filename)

        # Чтение дешифрованного отчета
        with open(report_path, 'rb') as decrypted_file:
            decrypted_data = decrypted_file.read()

        # Зашифровка отчета
        encrypted_data = cipher.encrypt(decrypted_data)

        # Сохранение зашифрованного отчета
        encrypted_filename = os.path.join(encrypted_reports_folder, filename)
        with open(encrypted_filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f'Отчет {filename} зашифрован и сохранен в {encrypted_reports_folder}.')

print('Шифрование завершено.')