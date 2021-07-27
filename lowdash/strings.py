from .arrays import chunks as array_chunks
from .arrays import shuffle


def mock(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument must be of type string")
    chunk = list(string)
    for i in range(len(chunk)):
        if i % 2 == 0:
            chunk[i] = upper(chunk[i])

    return "".join(chunk)


def upper(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument must be of type string")
    return string.upper()


def lower(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument must be of type string")
    return string.lower()


def scramble(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument must be of type string")

    return "".join(shuffle(list(string)))


def proper_case(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument must be of type string")
    chunks = string.split(" ")
    for i in range(len(chunks)):
        chunks[i] = chunks[i].capitalize()
    return " ".join(chunks)


def shorten(string: str, length: int, sep="...") -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument string must be of type string")
    if not isinstance(length, int):
        raise TypeError("[lowdash.strings] Argument length must be of type int")
    if not isinstance(sep, str):
        raise TypeError("[lowdash.strings] Argument sep must be of type string")
    if length > len(string):
        raise ValueError(
            "[lowdash.strings] Argument length must be less than string length"
        )
    return substr(string, 0, length) + sep


def substr(string: str, start: int, end: int) -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument string must be of type string")
    if not isinstance(start, int):
        raise TypeError("[lowdash.strings] Argument start must be of type int")
    if not isinstance(end, int):
        raise TypeError("[lowdash.strings] Argument end must be of type int")
    if start > len(string):
        raise ValueError(
            "[lowdash.strings] Argument start must be less than string length"
        )
    if end > len(string):
        raise ValueError(
            "[lowdash.strings] Argument end must be less than string length"
        )
    return string[start:end]


def chunks(string: str, size: int) -> str:
    if not isinstance(string, str):
        raise TypeError("[lowdash.strings] Argument string must be of type string")
    if not isinstance(size, int):
        raise TypeError("[lowdash.strings] Argument size must be of type int")
    return array_chunks(list(string), size)
