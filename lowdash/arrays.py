import random

from ._utils import args_type_checker


@args_type_checker
def chunks(array: list, size: int) -> list:
    """
    Splits an array into chunks of size
    ```py
    >>> lowdash.chunks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    ```
    """
    return [array[i : i + size] for i in range(0, len(array), size)]


@args_type_checker
def compact(array: list) -> list:
    """Removes all Falsey values from an array
    ```py
    >>> lowdash.compact([1, 2, 0, False, True, 0])
    [1, 2, True]
    ```
    """
    return [i for i in array if i]


@args_type_checker
def concat(array: list, *args) -> list:
    """
    Concatenates all Arrays passed to the function
    ```py
    >>> lowdash.concat([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    ```
    """
    return array + flatten(list(args))


@args_type_checker
def difference(array_a: list, array_b: list) -> list:
    """
    Removes all values that are in the args from the array
    ```py
    >>> lowdash.difference([1, 2, 3, 4, 5], [2, 3, 4])
    [1, 5]
    ```
    """
    return [i for i in array_a if i not in flatten(list(array_b))]


@args_type_checker
def drop(array: list, n: int) -> list:
    """
    Removes the nth element from the array
    ```py
    >>> lowdash.drop([1, 2, 3, 4, 5], 2)
    [1, 3, 4, 5]
    ```
    """
    array.pop(n)
    return array


@args_type_checker
def drop_right(array: list, n: int) -> len:
    """
    Similar to drop, but drops the nth element from the right
    ```py
    >>> lowdash.drop_right([1, 2, 3, 4, 5], 2)
    [1, 3, 4]
    ```
    """
    length = len(array)
    if n < 0 > length:
        raise ValueError(
            "[lowdash.drop_right]: Index must be greater than 0 and less than the length of the array."
        )

    return array.pop(length - n)


@args_type_checker
def fill(array: list, value, start: int, end: int) -> list:
    """
    Fills the array with the value passed in
    ```py
    >>> lowdash.fill([0,1,3,4,5],8,0,2)
    [8, 8, 3, 4, 5]
    ```
    """
    if start < 0:
        raise ValueError("[lowdash.fill]: Start must be greater than 0.")
    if end < 0:
        raise ValueError("[lowdash.fill]: End must be greater than 0.")
    if start > end:
        raise ValueError("[lowdash.fill]: Start must be less than or equal to end.")
    if len(array) < end:
        raise ValueError(
            "[lowdash.fill]: End must be greater than or equal to length of array."
        )
    if len(array) < start:
        raise ValueError(
            "[lowdash.fill]: Start must be less than or equal to length of array."
        )
    return array[:start] + [value] * (end - start) + array[end:]


@args_type_checker
def flatten(array: list) -> list:
    """
    Flattens a list of lists into a single list
    ```py
    >>> lowdash.flatten([[1, 2], [3, 4]])
    >>> [1, 2, 3, 4]
    ```
    """
    new_list = list()
    for i in array:
        if isinstance(i, list):
            new_list.extend(flatten(i))
        else:
            new_list.append(i)

    return new_list


@args_type_checker
def find_index(array: list, fn) -> int:
    """
    Returns the index of the first element in the array that matches the function
    ```py
    >>> lowdash.find_index([1, 2, 3, 4, 5], lambda x: x == 3)
    2
    """
    for i in range(len(array)):
        if fn(array[i]):
            return i

    return -1


@args_type_checker
def find_last_index(array: list, fn) -> int:
    """
    Similar to findIndex, but finds the last index of the first element that matches the function
    ```py
    >>> lowdash.find_last_index([1, 2, 3, 4, 5], lambda x: x == 3)
    4
    ```
    """
    for i in range(len(array)):
        if fn(array[i]):
            return len(array) - i - 1

    return -1


@args_type_checker
def index_of(array: list, value) -> int:
    """
    Returns the index of the first element in the array that matches the value
    ```py
    >>> lowdash.index_of([1, 2, 3, 4, 5], 3)
    2
    ```
    """
    try:
        return array.index(value)
    except ValueError:
        return -1


@args_type_checker
def insert(array: list, index: int, value) -> list:
    """
    Inserts the value into the array at the index passed in
    ```py
    >>> lowdash.insert([1, 2, 3, 4, 5], 2, 6)
    [1, 2, 6, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("[lowdash.insert]: Expected list for parameter array.")

    array.insert(index, value)
    return array


@args_type_checker
def from_pairs(array: list) -> dict:
    """
    Converts a list of pairs into a dictionary
    ```py
    >>> lowdash.from_pairs([("a", 1), ("b", 2), ("c", 3)])
    {"a": 1, "b": 2, "c": 3}
    ```
    """
    pairs = {}
    for i in range(len(array)):
        if isinstance(array[i], list):
            pairs[array[i][0]] = array[i][1]

    return pairs


@args_type_checker
def head(array: list):
    """
    Returns the first element of the array
    ```py
    >>> lowdash.head([1, 2, 3, 4, 5])
    1
    ```
    """
    return array[0] if len(array) else None


@args_type_checker
def intersection(array: list, *args) -> list:
    """
    Returns the intersection of the arrays passed in
    ```py
    >>> lowdash.intersection([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    [2, 3, 4, 5]
    ```
    """
    return list(
        set([i for i in array if i not in args]).union(
            set(flatten([i for i in args if i not in array]))
        )
    )


@args_type_checker
def join(array: list, delimiter: str) -> str:
    """
    Joins the elements of the array into a string
    ```py
    >>> lowdash.join([1, 2, 3, 4, 5], ",")
    "1,2,3,4,5"
    ```
    """
    return delimiter.join(array)


@args_type_checker
def last(array: list):
    """
    Returns the last element of the array
    ```py
    >>> lowdash.last([1, 2, 3, 4, 5])
    5
    ```
    """
    return array[:-1]


@args_type_checker
def nth(array: list, index: int):
    """
    Returns the nth element of the array
    ```py
    >>> lowdash.nth([1, 2, 3, 4, 5], 2)
    3
    ```
    """
    return array[index]


@args_type_checker
def pull(array: list, *args) -> list:
    """
    Removes the elements of the array passed in from the array
    ```py
    >>> lowdash.pull([1, 2, 3, 4, 5], 2)
    [1, 3, 4, 5]
    ```
    """
    return [i for i in array if i not in args]


@args_type_checker
def remove(array: list, fn) -> list:
    """
    Removes the elements of the array that match the function passed in
    ```py
    >>> lowdash.remove([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    [1, 3, 5]
    """
    return [i for i in array if not fn(i)]


@args_type_checker
def reverse(array: list) -> list:
    """
    Reverses an array
    ```py
    >>> lowdash.reverse([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    ```
    """
    return list(array).reverse()


@args_type_checker
def slice(array: list, start: int, end: int) -> list:
    """
    Returns a slice of the array
    ```py
    >>> lowdash.slice([1, 2, 3, 4, 5], 1, 3)
    [2, 3]
    ```
    """
    if start < 0 or end < 0:
        raise ValueError("[lowdash.slice]: Start and end cannot be negative.")
    if start > end:
        raise ValueError("[lowdash.slice]: Start must be less than end.")
    if start > len(array) - 1:
        raise ValueError("[lowdash.slice]: Start must be less than length of array.")
    return array[start:end]


@args_type_checker
def tail(array: list) -> list:
    """
    Removes the first element of the array
    ```py
    >>> lowdash.tail([1, 2, 3, 4, 5])
    [2, 3, 4, 5]
    ```
    """
    return [] if len(array) < 2 else array[1:]


@args_type_checker
def take(array: list, till: int = 0) -> list:
    """
    Returns a slice of the array
    ```py
    >>> lowdash.take([1, 2, 3, 4, 5], 3)
    [1, 2, 3]
    ```
    """
    return array[:till]


@args_type_checker
def uniq(array: list) -> list:
    """
    Returns a list of unique elements of the array
    ```py
    >>> lowdash.uniq([1, 2, 3, 4, 5, 5, 4, 4])
    [1, 2, 3, 4, 5]
    ```
    """
    return list(set(array))


@args_type_checker
def without(array: list, *args) -> list:
    """
    Removes the elements of the array passed in from the array
    ```py
    >>> lowdash.without([1, 2, 3, 4, 5], 2, 3)
    [1, 4, 5]
    ```
    """
    return [i for i in array if i not in args]


@args_type_checker
def shift(array: list) -> list:
    """
    Similar to `tail` function removes the first element of the array
    ```py
    >>> lowdash.shift([1, 2, 3, 4, 5])
    [2, 3, 4, 5]
    ```
    """
    if len(array):
        array.pop(0)

    return array


@args_type_checker
def unshift(array: list, value) -> list:
    """
    Adds an element to the beginning of the array
    ```py
    >>> lowdash.unshift([1, 2, 3, 4, 5], 6)
    [6, 1, 2, 3, 4, 5]
    ```
    """
    return array.insert(0, value)


@args_type_checker
def union(array: list, *args) -> list:
    """
    Returns a list of union elements of the array and arguments passed in
    ```py
    >>> lowdash.union([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    ```
    """
    return list(
        set([i for i in array if i not in args]).union(
            set(flatten([i for i in args if i not in array]))
        )
    )


@args_type_checker
def xor(array: list, *args) -> list:
    """
    Returns a list of elements that are in one of the arrays and not in both
    ```py
    >>> lowdash.xor([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    [1, 6]
    ```
    """
    return list(
        set([i for i in array if i not in args]).symmetric_difference(
            set(flatten([i for i in args if i not in array]))
        )
    )


@args_type_checker
def shuffle(array: list) -> list:
    random.shuffle(array)
    return array


@args_type_checker
def zip(array: list, *args) -> list:
    """Returns a list of tuples of the elements of the arrays and arguments passed in
    Args:
        array (list): [The main array]
    Returns:
        list: [zipped list]
    Example:
    .. code-block::python
        >>> lowdash.zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
        [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
    """
    return list(zip(array, *args))
