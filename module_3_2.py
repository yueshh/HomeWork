user = "university.help@gmail.com"
def send_email(message, recipient, sender="university.help@gmail.com"):
    checkDomen = [".com", ".ru", ".net"]
    if ((recipient.find("@") == -1
            or sender.find("@") == -1)
            or not any([t in recipient for t in checkDomen])
            or not any([t in sender for t in checkDomen])):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == user:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != user:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Это сообщение для проверки', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Это сообщение для проверки', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
