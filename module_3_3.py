message = 'Это сообщение для проверки связи'
recipient = 'vasyok1337@gmail.uk'
sender = 'urban.teacher@mail.com'
end_1 = recipient.endswith((".com", '.ru', '.net')) and sender.endswith((".com", '.ru', '.net'))
find_1 = recipient.find('@') and sender.find('@')
if end_1 == 0  or find_1 < 0:
    print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
elif sender == recipient:
    print("Нельзя отправить письмо самому себе!")
elif sender == 'university.help@gmail.com'and recipient != 'university.help@gmail.com':
    print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
else:
    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

