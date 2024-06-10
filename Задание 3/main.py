def is_correct_mobile_phone_number(number):
    number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if number.startswith("+7") or number.startswith("8"):
        number = number.replace("+", "")
        if len(number) == 11 and number.isdigit():
            return True
    return False


def test_is_correct_mobile_phone_number():
    test_cases = [
        ("+7 (927) 123-45-67", True),
        (" 8 (937) 123-45-67", True),
        ("+7 999 123 45 67", True),
        ("79991234567", False),
        ("7 999 123 45 67", False),
        ("+7(900)1234567", True),
        ("+7 999 123-45-6", False),
        ("+7 999 123 45", False),
        ("7999123456", False),
        ("7999123456a", False),
        ("+7 999 123 45 678", False),
        ("+7 999 123 45 67a", False),
    ]

    for test_case in test_cases:
        number, expected_result = test_case
        result = is_correct_mobile_phone_number(number)
        if result == expected_result:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    test_is_correct_mobile_phone_number()
