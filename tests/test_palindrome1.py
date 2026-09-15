from PALINDROME1 import Solution


def test_palindrome_numbers():
    solution = Solution()

    assert solution.isPalindrome(121) is True
    assert solution.isPalindrome(1221) is True
    assert solution.isPalindrome(0) is True


def test_not_palindrome_numbers():
    solution = Solution()

    assert solution.isPalindrome(123) is False
    assert solution.isPalindrome(1234) is False


def test_negative_numbers():
    solution = Solution()

    assert solution.isPalindrome(-121) is False
    assert solution.isPalindrome(-1) is False


def test_single_digit_numbers():
    solution = Solution()

    assert solution.isPalindrome(5) is True
    assert solution.isPalindrome(9) is True