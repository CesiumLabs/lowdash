from .arrays import chunks as array_chunks
from .arrays import shuffle

from ._utils import args_type_checker


@args_type_checker
def mock(string: str) -> str:
    chunk = list(string)
    return "".join([chunk[i].upper() if i % 2 else chunk[i].lower() for i in range(len(chunk))])


@args_type_checker
def upper(string: str) -> str:
    return string.upper()


@args_type_checker
def lower(string: str) -> str:
    return string.lower()


@args_type_checker
def scramble(string: str) -> str:
    return "".join(shuffle(list(string)))


@args_type_checker
def proper_case(string: str) -> str:
    chunks = string.split(" ")
    for i in range(len(chunks)):
        chunks[i] = chunks[i].capitalize()
    return " ".join(chunks)


@args_type_checker
def shorten(string: str, length: int, sep="...") -> str:
    if length > len(string):
        raise ValueError(
            "[lowdash.strings] Argument length must be less than string length"
        )
    return substr(string, 0, length) + sep


@args_type_checker
def substr(string: str, start: int, end: int) -> str:
    if start > len(string):
        raise ValueError(
            "[lowdash.strings] Argument start must be less than string length"
        )
    if end > len(string):
        raise ValueError(
            "[lowdash.strings] Argument end must be less than string length"
        )
    return string[start:end]


@args_type_checker
def chunks(string: str, size: int) -> str:
    return array_chunks(list(string), size)
