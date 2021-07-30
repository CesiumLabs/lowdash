from .arrays import chunks as array_chunks
from .arrays import shuffle
from ._utils import args_type_checker

@args_type_checker
def mock(string: str) -> str:
    """
    Capitalizes the letters in the string at the even number index.
    ```py
    >>> lowdash.strings.mock("hello world")
    >>> HeLlO WoRlD
    ```
    """
    chunk = list(string)
    for i in range(len(chunk)):
        if i % 2 == 0:
            chunk[i] = upper(chunk[i])

    return "".join(chunk)


@args_type_checker
def upper(string: str) -> str:
    """
    Converts a string into uppercase.
    ```py
    >>> lowdash.strings.upper("hello world")
    >>> HELLO WORLD
    """
    return string.upper()


@args_type_checker
def lower(string: str) -> str:
    """
    Converts a string into lowercase.
    ```py
    >>> lowdash.strings.upper("HELLO WORLD")
    >>> hello world
    """
    return string.lower()


@args_type_checker
def scramble(string: str) -> str:
    """
    Scrambles the characters in the string.
    ```py
    >>> lowdash.strings.upper("hello world")
    >>> rod olllehw
    """
    return "".join(shuffle(list(string)))


@args_type_checker
def proper_case(string: str) -> str:
    """
    Converts a string into proper case.
    ```py
    >>> lowdash.strings.upper("hello world")
    >>> Hello World
    """
    chunks = string.split(" ")
    for i in range(len(chunks)):
        chunks[i] = chunks[i].capitalize()

    return " ".join(chunks)


@args_type_checker
def shorten(string: str, length: int, sep="...") -> str:
    """
    Shortens a string if the string exceeds the length with a sepearator.
    ```py
    >>> lowdash.strings.upper("hello world", 3)
    >>> hel...
    """

    if length > len(string):
        raise ValueError(
            "[lowdash.strings] Argument length must be less than string length"
        )

    return substr(string, 0, length) + sep


@args_type_checker
def substr(string: str, start: int, end: int) -> str:
    """
    Slices a string.
    ```py
    >>> lowdash.strings.substr("hello world", 6, 11)
    >>> world
    """
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
    """
    Breaks strings into chunks.
    ```py
    >>> lowdash.strings.chunks("hello world", 2)
    >>> ["he", "ll", "o ", "wo", "rl", "d"]
    """
    return array_chunks(list(string), size)
