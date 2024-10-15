def address_verification(address):
    a = True
    b = True
    c = len(address)
    if address.find('.com') + 4 == c or address.find('.net') + 4 == c or address.find('.ru') + 3 == c:
        a = False
    else:
        a = True
    if address.find('@') != 0 and address.find('@') < address.rfind('.') - 1 and address.find('@') != -1:
        b = False
    else:
        b = True
    if a == False and b == False:
        return False
    else:
        return True


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if address_verification(recipient) or address_verification(sender):
        return print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)

    if sender == recipient:
        return print("Нельзя отправить письмо самому себе!")

    if sender == "university.help@gmail.com":
        return print("Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
