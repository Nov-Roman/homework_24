import re
from typing import Iterator, List, Iterable, Set, Union


def filter_(iterable: Iterator, string_to_search: str) -> Iterable:
    """Получить данные, которые содержат указанный текст"""
    if not isinstance(string_to_search, str):
        raise TypeError("В функцию фильтра переданы неверные данные, разрешены только строки")
    return filter(lambda line: string_to_search in line, iterable)


def sort_(iterable: Iterator, order: str = 'asc') -> List:
    """Сортировка данных в порядке возрастания или убывания"""
    if order not in ('asc', 'desc'):
        raise ValueError('Передан неверный аргумент, разрешено использовать только по возрастанию или по убыванию.')
    if order == 'desc':
        return sorted(iterable, reverse=True)
    return sorted(iterable, reverse=False)


def map_(iterable: Iterator, column: Union[str, int]) -> Iterable:
    """Получить только указанный столбец"""

    regex = re.compile(r'(?: - - \[)|(?:\] ")|(?:" ")|(?: \")|(?:\" )')

    if not str(column).isdigit():
        raise TypeError('Отрицательное число или текст, переданный в качестве номера столбца в функцию карты')

    return map(lambda line: regex.split(line)[int(column)], iterable)


def limit_(iterable: Iterator, number: Union[str, int]) -> List:
    """Предельные строки, возвращаемые переданным числом"""
    if not str(number).isdigit():
        raise TypeError('Разрешены только цифры')
    return list(iterable)[:int(number)]


def unique_(iterable: Iterator, *args) -> Set:
    """Возвращает только уникальные строки"""
    return set(iterable)


def regex_(iterable: Iterator, expression: str) -> Iterable:
    """Данные с переданным регулярным выражением"""
    regex = re.compile(rf'{str(expression)}')
    return filter(lambda line: regex.search(line), iterable)
