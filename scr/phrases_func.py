from random import randint


def dict_to_str(dictionary: dict) -> str:
    """Преобразовывает словарь в строку, имеющую вид списка"""
    string = ""
    for item in dictionary:
        string += f"{item} - {dictionary[item]}\n"
    return string


def random_phrase(phrases: list[str]) -> str:
    """Возвращает случайную фразу из списка"""
    return phrases[randint(0, len(phrases) - 1)]
