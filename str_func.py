def to_uppercase(input_str):
    """
    Преобразует все символы строки в верхний регистр.

    :param input_str: Исходная строка
    :return: Строка с преобразованными символами в верхний регистр
    """
    return input_str.upper()


# str_func.py

def capitalize_first_letters(input_str):
    """
    Преобразует первые буквы каждого слова в строке в верхний регистр.

    :param input_str: Исходная строка
    :return: Строка с преобразованными первыми буквами каждого слова в верхний регистр
    """
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
