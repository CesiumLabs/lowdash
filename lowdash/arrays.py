class arrays:
    def compact(array: list) -> list:
        """Removes all Falsey values from an array
        ```py
        >>> arrays.compact([1, 2, 0, False, True, 0])
        >>> [1, 2, True]
        ```
        """
        if not isinstance(array, list):
            raise TypeError("Expected list")
        newArr = list()
        for i in array:
            if (i == 0 or i == False or i == None):
                continue
            else:
                newArr.append(i)
        return newArr

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
        for i in args:
            array.append(i)
        return array

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
        for i in args:
            array.remove(i)
        return array

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
        newArr = list()
        for j in range(i, len(array)):
            newArr.append(array[j])
        return newArr

    def drop_right(array: list, i: int) -> len:
        """
        Similar to drop, but drops the ith element from the right
        ```py
        >>> arrays.dropRight([1, 2, 3, 4, 5], 2)
        >>> [1, 3, 4]
        ```
        """
        if not isinstance(array, list):
            raise TypeError("Expected list")
        if i < 0:
            raise ValueError("Index must be greater than 0")
        if i > len(array):
            raise ValueError("Index must be less than length of list")
        newArr = list()
        for j in range(0, i):
            newArr.append(array[j])
        return newArr

    def fill(array: list, value, start: int, end: int) -> list:
        """
        Fills the array with the value passed in
        ```py
        >>> arrays.fill([1, 2, 3, 4], 0, 2, 4)
        >>> [0, 1, 2, 3, 4]
        ```
        """
        if not isinstance(array, list):
            raise TypeError("Expected list")
        if(not end):
            end = len(array)
        newArr = []
        for i in range(start, end):
            newArr.append(value)
        return newArr

    def find_index(array: list, fn) -> int:
        """
        Returns the index of the first element in the array that matches the function
        ```py
        >>> arrays.findIndex([1, 2, 3, 4, 5], lambda x: x == 3)
        >>> 2
        """
        if not isinstance(array, list):
            raise TypeError("Expected list")
        if(not fn):
            raise ValueError("Function must be defined")
        index = -1
        for i in range(len(array)):
            if(fn(array[i])):
                index = i
                break
        return index

    def find_last_index(array: list, fn) -> int:
        """
        Similar to findIndex, but finds the last index of the first element that matches the function
        ```py
        >>> arrays.findLastIndex([1, 2, 3, 4, 5], lambda x: x == 3)
        >>> 4
        ```
        """
        if not isinstance(array, list):
            raise TypeError("Expected list")
        if(not fn):
            raise ValueError("Function must be defined")
        index = -1
        for i in range(len(array)):
            if(fn(array[i])):
                index = len(array)-i-1
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
        newArr = []
        for i in array:
            if isinstance(i, list):
                tempArr = []
                for j in range(len(i)):
                    tempArr.append(i[j])
                newArr.extend(tempArr)
            else:
                newArr.append(i)
        return newArr

    def index_of(array: list, value) -> int:
        """
        Returns the index of the first element in the array that matches the value
        ```py
        >>> arrays.indexOf([1, 2, 3, 4, 5], 3)
        >>> 2
        ```
        """
        if not isinstance(array, list):
            raise TypeError("Expected list")
        if(not value):
            raise ValueError("Value must be defined")
        index = -1
        for i in range(len(array)):
            if(array[i] == value):
                index = i
                break
        return index

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
        if(not index):
            raise ValueError("Index must be defined")
        if(index < 0):
            raise ValueError("Index must be greater than 0")
        if(index > len(array)):
            raise ValueError("Index must be less than length of list")
        array.insert(index, value)
        return array

    def from_pairs(array: list) -> dict:
        """
        Converts a list of pairs into a dictionary
        ```py
        >>> arrays.fromPairs([("a", 1), ("b", 2), ("c", 3)])
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
        return array[0:len(array)-1]

    def intersection(array: list, *args) -> list:
        """
        Returns the intersection of the arrays passed in
        TODO not made yet feel free to make it for me :) here -> https://github.com/abh80/lowdash
        """
        # TODO
        return array

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
        return array[len(array)-1]

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
        newArr = []
        for i in array:
            if i not in args:
                newArr.append(i)
        return newArr

    def remove(array: list, fn) -> list:
        """
        Removes the elements of the array that match the function passed in
        ```py
        >>> arrays.remove([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        >>> [1, 3, 5]
        """
        if not isinstance(array, list):
            raise TypeError("Expected list")
        if(not fn):
            raise ValueError("Function must be defined")
        newArr = []
        for i in array:
            if(not fn(i)):
                newArr.append(i)
        return newArr

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
        if(not start):
            start = 0
        if(not end):
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
        return array[1:len(array)]

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
        if(not till):
            till = 1
        return array[0:till]

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
        newArr = []
        for i in array:
            if i not in newArr:
                newArr.append(i)
        return newArr

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
        newArr = []
        for i in array:
            if i not in args:
                newArr.append(i)
        return newArr
