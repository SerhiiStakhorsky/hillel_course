def add_one(digits) -> int:
    number = int(''.join(map(str, digits)))
    number += 1
    result = [int(digit) for digit in str(number)]
    return result


if __name__ == "__main__":
    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test 1 failed"
    assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test 2 failed"
    assert add_one([0]) == [1], "Test 3 failed"
    assert add_one([9]) == [1, 0], "Test 4 failed"

    print("Ok")
