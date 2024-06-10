def is_correct_mobile_phone_number(number):
    number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if number.startswith("+7") or number.startswith("8"):
        number = number.replace("+", "")
        if len(number) == 11 and number.isdigit():
            return True
    return False


if __name__ == "__main__":
    phone_number = input("Введите номер телефона: ")
    print(is_correct_mobile_phone_number(phone_number))
