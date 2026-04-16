"""1.Отправить письмо на тестовый адрес
В теле и теме письма дожна быть ваша фамилия ТРАНСЛИТОМ и группа
2.Создать ПАПКУ с фашей фамилией ТРАНСЛИТОМ
3.Найти свое письмо на почтовом ящике и копировать его в созданную папку.
Можете использовать OpenSSl можете написать свой код.
Результат письмо в папке на ящике."""


import smtplib
import imaplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.mail.ru"
SMTP_PORT = 465
IMAP_SERVER = "imap.mail.ru"
IMAP_PORT = 993

LOGIN = "<login>"
PASSWORD = "<password>"

FAMILY_NAME = "Stolbov"
GROUP = "MO-201"
MESSAGE_BODY = f"{FAMILY_NAME} {GROUP}"

def send_email():
    print("1. Отправка письма...")
    msg = MIMEText(MESSAGE_BODY)
    msg['Subject'] = MESSAGE_BODY
    msg['From'] = LOGIN
    msg['To'] = LOGIN

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(LOGIN, PASSWORD)
        server.send_message(msg)
    print(f"   Письмо отправлено на {LOGIN}")
    return msg

def create_folder_imap(mail, folder_name):
    status, folders = mail.list()
    existing = [f.decode().split(' "/" ')[-1].strip('"') for f in folders]
    if folder_name in existing:
        print(f"   Папка '{folder_name}' уже существует.")
    else:
        mail.create(folder_name)
        print(f"   Папка '{folder_name}' создана.")

def append_email_to_folder(mail, folder_name, msg):
    raw_message = msg.as_string().encode('utf-8')
    result = mail.append(folder_name, None, None, raw_message)
    if result[0] == 'OK':
        print(f"3. Письмо сохранено в папку '{folder_name}' через APPEND.")
    else:
        print("Ошибка при добавлении письма:", result)

def main():
    msg = send_email()

    print("2. Подключение к IMAP и работа с папками...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail._encoding = 'utf-8'
    mail.login(LOGIN, PASSWORD)

    create_folder_imap(mail, FAMILY_NAME)

    append_email_to_folder(mail, FAMILY_NAME, msg)

    mail.logout()
    print("\nЗадание выполнено успешно!")

if __name__ == "__main__":
    main()
