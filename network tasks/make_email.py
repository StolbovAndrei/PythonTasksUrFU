"""Сделать письмо где будет:

1.Правильные заголовки где в содержании From To будет ваша фамилия
2.Письмо должно быть составное и содеражть:
2.1 html часть + ссылка на картинку(можно ссылку из веба/ссылку на картинку внутри письма не приципиально)Если не выйдет то не страшно
2.2 текстовую часть
2.3 текстовое вложение
2.4 любой интересный вам MIME формат отличный от прошлых(например вложить гифку)
ВАЖНО, чтобы письмо корректно отрабатывало в каком-нибудь почтовом клиенте, если клиент на котором проверяли работу 
отличен от outlook или стандартного windows укажите это и сам клиент на котором тестировали.
В результате у вас в ответе должно быть письмо + клиент на котором проверяли работу."""


import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import os

# 1. Настройка основных параметров
sender_email = "andrey.stolbov@example.com"
sender_name = "Андрей Столбов"
receiver_email = "recipient@example.com"
receiver_name = "Получатель"

msg = EmailMessage()
msg['From'] = f"{sender_name} <{sender_email}>"
msg['To'] = f"{receiver_name} <{receiver_email}>"
msg['Subject'] = "Составное письмо от Андрея Столбова"
msg['Date'] = smtplib.email.utils.formatdate(localtime=True)
msg['Message-ID'] = make_msgid(domain='stolbov.example.com')

# 2. Текстовая версия
plain_text = """
Привет!

Это письмо было создано автоматически в демонстрационных целях.

С уважением,
Андрей Столбов
"""
msg.set_content(plain_text.strip())

# 3. HTML-версия
image_url = "https://avatars.mds.yandex.net/i?id=b69df7d00b1df80723504558aa42e483_l-5113900-images-thumbs&n=13"
html_content = f"""
<html>
  <body>
    <h1>Привет!</h1>
    <p>Это письмо было создано автоматически в демонстрационных целях.</p>
    <p>Ниже вставлено изображение по ссылке из интернета:</p>
    <img src="{image_url}" alt="Кошечка Комару" width="400">
    <p><em>С уважением,<br>Андрей Столбов</em></p>
  </body>
</html>
"""
msg.add_alternative(html_content, subtype='html')

# 4. Текстовое вложение
attachment_text = "Это текстовое вложение.\nОно демонстрирует возможность прикреплять файлы."
msg.add_attachment(
    attachment_text.encode('utf-8'),
    maintype='text',
    subtype='plain',
    filename='attachment.txt'
)

# 5. GIF-вложение
script_dir = os.path.dirname(os.path.abspath(__file__))  # папка с этим скриптом
base_name = "komaru-komaru-cat"

possible_names = [
    os.path.join(script_dir, base_name + ".gif"),
    os.path.join(script_dir, base_name)  # если расширение скрыто
]

gif_data = None
for path in possible_names:
    if os.path.exists(path):
        try:
            with open(path, 'rb') as f:
                gif_data = f.read()
            print(f"GIF-файл успешно загружен: {path}")
            break
        except Exception as e:
            print(f"Ошибка чтения файла {path}: {e}")
            continue


msg.add_attachment(
    gif_data,
    maintype='image',
    subtype='gif',
    filename='komaru-komaru-cat.gif'
)

# 6. Сохранение письма
with open('Stolbov_Email.eml', 'wb') as f:
    f.write(msg.as_bytes())

print("Письмо успешно создано и сохранено в 'Stolbov_Email.eml'")
