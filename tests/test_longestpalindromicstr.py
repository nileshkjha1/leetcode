from longestpalindromicstr import Solution


def test_longest_palindrome_examples():
    solution = Solution()

    # Example 1
    assert solution.longestPalindrome("babad") in ["bab", "aba"]

    # Example 2
    assert solution.longestPalindrome("cbbd") == "bb"


def test_single_character():
    solution = Solution()

    assert solution.longestPalindrome("a") == "a"


def test_all_same_characters():
    solution = Solution()

    assert solution.longestPalindrome("aaaa") == "aaaa"


def test_two_different_characters():
    solution = Solution()

    assert solution.longestPalindrome("ab") in ["a", "b"]