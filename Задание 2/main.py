
def is_palindrome(data):
    str1 = data.lower()
    str2 = data.lower()[::-1]
    result = str1 == str2
    return result


if __name__ == "__main__":
    str1 = input("Введите строку: ").strip()
    print(is_palindrome(str1))
