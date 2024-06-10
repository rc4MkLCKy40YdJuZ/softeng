import string


def strip_punctuation_ru(data):
    # Удаляем знаки препинания
    translator = str.maketrans('', '', string.punctuation)
    translate = data.translate(translator)
    words = translate.split()
    word = ' '.join(words)

    return word


if __name__ == "__main__":
    print(strip_punctuation_ru(input("Введите строку: ")))
