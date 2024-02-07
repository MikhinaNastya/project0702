import os
from cryptography.fernet import Fernet

# Папка для отчетов после проверки
checked_reports_folder = 'checked_reports'

# Проверка и создание папки checked_reports
if not os.path.exists(checked_reports_folder):
    os.makedirs(checked_reports_folder)

# Прочитать дешифрованные файлы
for filename in os.listdir(decrypted_reports_folder):
    if filename.endswith('.txt'):
        report_path = os.path.join(decrypted_reports_folder, filename)

        # Чтение дешифрованного отчета
        with open(report_path, 'r') as report_file:
            report_content = report_file.read()

        # Замена префиксов и добавление строки "Проверено!"
        updated_content = report_content.replace('вра', 'дру', -1)  # -1 для замены всех вхождений
        updated_content += '\nПроверено!'

        # Сохранение обновленного отчета
        checked_filename = os.path.join(checked_reports_folder, filename)
        with open(checked_filename, 'w') as checked_file:
            checked_file.write(updated_content)

        print(f'Отчет {filename} обновлен и сохранен в {checked_reports_folder}.')

print('Проверка отчетов завершена.')