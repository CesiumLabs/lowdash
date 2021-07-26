def chunks(array: list, size: int) -> list:
    """
    Splits an array into chunks of size
    ```py
    >>> arrays.chunks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    >>> [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")

    return [array[i: i + size] for i in range(0, len(array), size)]


def compact(array: list) -> list:
    """Removes all Falsey values from an array
    ```py
    >>> arrays.compact([1, 2, 0, False, True, 0])
    >>> [1, 2, True]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return [i for i in array if i]


def concat(array: list, *args) -> list:
    """
    Concatenates all arrays passed to the function
    ```py
    >>> arrays.concat([1, 2, 3], [4, 5, 6])
    >>> [1, 2, 3, 4, 5, 6]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return array + flatten(list(args))


def difference(array: list, *args) -> list:
    """
    Removes all values that are in the args from the array
    ```py
    >>> arrays.difference([1, 2, 3, 4, 5], [2, 3, 4])
    >>> [1, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")

    return [i for i in array if i not in flatten(list(args))]


def drop(array: list, i: int) -> list:
    """
    Removes the ith element from the array
    ```py
    >>> arrays.drop([1, 2, 3, 4, 5], 2)
    >>> [1, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if i < 0:
        raise ValueError("Index must be greater than 0")
    if i > len(array):
        raise ValueError("Index must be less than length of list")
    new_arr = list()
    for j in range(i, len(array)):
        new_arr.append(array[j])
    return new_arr


def drop_right(array: list, i: int) -> len:
    """
    Similar to drop, but drops the ith element from the right
    ```py
    >>> arrays.drop_right([1, 2, 3, 4, 5], 2)
    >>> [1, 3, 4]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if i < 0:
        raise ValueError("Index must be greater than 0")
    if i > len(array):
        raise ValueError("Index must be less than length of list")
    new_arr = list()
    for j in range(0, i):
        new_arr.append(array[j])
    return new_arr


def fill(array: list, value, start: int, end: int) -> list:
    """
    Fills the array with the value passed in
    ```py
    >>> arrays.fill([0,1,3,4,5],8,0,2)
    >>> [8, 8, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not end:
        end = len(array)
    return array[:start] + [value] * (end - start) + array[end:]


def find_index(array: list, fn) -> int:
    """
    Returns the index of the first element in the array that matches the function
    ```py
    >>> arrays.find_index([1, 2, 3, 4, 5], lambda x: x == 3)
    >>> 2
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not fn:
        raise ValueError("Function must be defined")
    index = -1
    for i in range(len(array)):
        if fn(array[i]):
            index = i
            break
    return index


def find_last_index(array: list, fn) -> int:
    """
    Similar to findIndex, but finds the last index of the first element that matches the function
    ```py
    >>> arrays.find_last_index([1, 2, 3, 4, 5], lambda x: x == 3)
    >>> 4
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not fn:
        raise ValueError("Function must be defined")
    index = -1
    for i in range(len(array)):
        if fn(array[i]):
            index = len(array) - i - 1
            break
    return index


def flatten(array: list) -> list:
    """
    Flattens a list of lists into a single list
    ```py
    >>> arrays.flatten([[1, 2], [3, 4]])
    >>> [1, 2, 3, 4]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    new_arr = []
    for i in array:
        if isinstance(i, list):
            tempArr = []
            for j in range(len(i)):
                tempArr.append(i[j])
            new_arr.extend(tempArr)
        else:
            new_arr.append(i)
    return new_arr


def index_of(array: list, value) -> int:
    """
    Returns the index of the first element in the array that matches the value
    ```py
    >>> arrays.index_of([1, 2, 3, 4, 5], 3)
    >>> 2
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not value:
        raise ValueError("Value must be defined")
    try:
        return array.index(value)
    except ValueError:
        return -1


def insert(array: list, index: int, value) -> list:
    """
    Inserts the value into the array at the index passed in
    ```py
    >>> arrays.insert([1, 2, 3, 4, 5], 2, 6)
    >>> [1, 2, 6, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not index and index != 0:
        raise ValueError("Index must be defined")
    if index < 0:
        raise ValueError("Index must be greater than 0")
    if index > len(array):
        raise ValueError("Index must be less than length of list")
    array.insert(index, value)
    return array


def from_pairs(array: list) -> dict:
    """
    Converts a list of pairs into a dictionary
    ```py
    >>> arrays.from_pairs([("a", 1), ("b", 2), ("c", 3)])
    >>> {"a": 1, "b": 2, "c": 3}
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    pairs = {}
    for i in range(len(array)):
        if isinstance(array[i], list):
            pairs[array[i][0]] = array[i][1]

    return pairs


def head(array: list) -> int:
    """
    Returns the first element of the array
    ```py
    >>> arrays.head([1, 2, 3, 4, 5])
    >>> 1
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return array[0]


def initial(array: list) -> int:
    """
    Returns the initial element of the array
    ```py
    >>> arrays.initial([1, 2, 3, 4, 5])
    >>> 1
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return array[0: len(array) - 1]


def intersection(array: list, *args) -> list:
    """
    Returns the intersection of the arrays passed in
    ```py
    >>> arrays.intersection([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    >>> [2, 3, 4, 5]
    ```
    """
    return list(
        set([i for i in array if i not in args]).union(
            set(flatten([i for i in args if i not in array]))
        )
    )


def join(array: list, delimiter: str) -> str:
    """
    Joins the elements of the array into a string
    ```py
    >>> arrays.join([1, 2, 3, 4, 5], ",")
    >>> "1,2,3,4,5"
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not isinstance(delimiter, str):
        raise TypeError("Expected string")
    return delimiter.join(array)


def last(array: list):
    """
    Returns the last element of the array
    ```py
    >>> arrays.last([1, 2, 3, 4, 5])
    >>> 5
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return array[:-1]


def nth(array: list, index: int):
    """
    Returns the nth element of the array
    ```py
    >>> arrays.nth([1, 2, 3, 4, 5], 2)
    >>> 3
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if index < 0:
        raise ValueError("Index must be greater than 0")
    return array[index]


def pull(array: list, *args) -> list:
    """
    Removes the elements of the array passed in from the array
    ```py
    >>> arrays.pull([1, 2, 3, 4, 5], 2)
    >>> [1, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return [i for i in array if i not in args]


def remove(array: list, fn) -> list:
    """
    Removes the elements of the array that match the function passed in
    ```py
    >>> arrays.remove([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    >>> [1, 3, 5]
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not fn:
        raise ValueError("Function must be defined")

    return [i for i in array if fn(i) == False]


def reverse(array: list) -> list:
    """
    Reverses an array
    ```py
    >>> arrays.reverse([1, 2, 3, 4, 5])
    >>> [5, 4, 3, 2, 1]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    array.reverse()
    return array


def slice(array: list, start: int, end: int) -> list:
    """
    Returns a slice of the array
    ```py
    >>> arrays.slice([1, 2, 3, 4, 5], 1, 3)
    >>> [2, 3]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not start:
        start = 0
    if not end:
        end = len(array)
    return array[start:end]


def tail(array: list) -> list:
    """
    Removes the first element of the array
    ```py
    >>> arrays.tail([1, 2, 3, 4, 5])
    >>> [2, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return array[1:]


def take(array: list, till: int) -> list:
    """
    Returns a slice of the array
    ```py
    >>> arrays.take([1, 2, 3, 4, 5], 3)
    >>> [1, 2, 3]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    if not till:
        till = 1
    return array[:till]


def uniq(array: list) -> list:
    """
    Returns a list of unique elements of the array
    ```py
    >>> arrays.uniq([1, 2, 3, 4, 5, 5, 4, 4])
    >>> [1, 2, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    unique = set()
    return [i for i in array if i not in unique and not unique.add(i)]


def without(array: list, *args) -> list:
    """
    Removes the elements of the array passed in from the array
    ```py
    >>> arrays.without([1, 2, 3, 4, 5], 2, 3)
    >>> [1, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return [i for i in array if i not in args and i not in args]


def shift(array: list) -> list:
    """
    Similar to `tail` function removes the first element of the array
    ```py
    >>> arrays.shift([1, 2, 3, 4, 5])
    >>> [2, 3, 4, 5]
    ```
    """
    return tail(array)


def unshift(array: list, value) -> list:
    """
    Adds an element to the beginning of the array
    ```py
    >>> arrays.unshift([1, 2, 3, 4, 5], 6)
    >>> [6, 1, 2, 3, 4, 5]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return insert(array, 0, value)


def union(array: list, *args) -> list:
    """
    Returns a list of union elements of the array and arguments passed in
    ```py
    >>> arrays.union([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    >>> [1, 2, 3, 4, 5, 6]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return list(
        set([i for i in array if i not in args]).union(
            set(flatten([i for i in args if i not in array]))
        )
    )


def xor(array: list, *args) -> list:
    """
    Returns a list of elements that are in one of the arrays and not in both
    ```py
    >>> arrays.xor([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    >>> [1, 6]
    ```
    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return list(
        set([i for i in array if i not in args]).symmetric_difference(
            set(flatten([i for i in args if i not in array]))
        )
    )


def zip(array: list, *args) -> list:
    """Returns a list of tuples of the elements of the arrays and arguments passed in

    Args:
        array (list): [The main array]

    Returns:
        list: [zipped list]

    Example:
    .. code-block::python
        >>> arrays.zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
        >>> [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

    """
    if not isinstance(array, list):
        raise TypeError("Expected list")
    return list(zip(array, *args))
