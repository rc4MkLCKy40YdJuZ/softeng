
def is_palindrome(data):
    str1 = data.lower()
    str2 = data.lower()[::-1]
    result = str1 == str2
    return result


def test_is_palindrome():
    # Тестовые случаи
    test_cases = [
        ("Abba", True),
        ("World", False),
        ("raDaR", True),
        ("hello", False),
        ("Java", False),
        ("LeVeL", True),
        ("C++", False),
        ("ReFeR", True),
        ("madaM", True),
        ("python", False),
    ]

    # Тестирование функции
    for test_case in test_cases:
        s, expected_result = test_case
        result = is_palindrome(s)
        if result == expected_result:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    test_is_palindrome()
