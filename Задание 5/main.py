import string


def strip_punctuation_ru(data):
    # Удаляем знаки препинания
    translator = str.maketrans('', '', string.punctuation)
    translate = data.translate(translator)
    words = translate.split()
    word = ' '.join(words)

    return word


def test_strip_punctuation_ru():
    test_cases = [
        ("Привет, мир!", "Привет мир"),
        ("Тестовая строка...", "Тестовая строка"),
        ("Скобки (и) и точки.", "Скобки и и точки"),
        ("Восклицательные знаки!", "Восклицательные знаки"),
        ("Апострофы 'и' кавычки.", "Апострофы и кавычки"),
        ("Многоточие...", "Многоточие"),
        ("Вопросительный знак?", "Вопросительный знак"),
        ("Восклицательный знак!", "Восклицательный знак"),
    ]

    for test_case in test_cases:
        number, expected_result = test_case
        result = strip_punctuation_ru(number)
        if result == expected_result:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    test_strip_punctuation_ru()
