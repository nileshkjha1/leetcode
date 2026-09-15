from ROMANTOINT import Solution


def test_basic_roman_numbers():
    solution = Solution()

    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("V") == 5
    assert solution.romanToInt("X") == 10
    assert solution.romanToInt("L") == 50
    assert solution.romanToInt("C") == 100
    assert solution.romanToInt("D") == 500
    assert solution.romanToInt("M") == 1000


def test_subtraction_cases():
    solution = Solution()

    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("IX") == 9
    assert solution.romanToInt("XL") == 40
    assert solution.romanToInt("XC") == 90
    assert solution.romanToInt("CD") == 400
    assert solution.romanToInt("CM") == 900


def test_complex_roman_numbers():
    solution = Solution()

    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
    assert solution.romanToInt("MMXXIV") == 2024