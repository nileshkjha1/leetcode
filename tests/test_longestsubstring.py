from longestsubstring import Solution


def test_basic_cases():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3


def test_empty_string():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("") == 0


def test_single_character():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("a") == 1


def test_all_unique_characters():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcdef") == 6


def test_repeated_characters():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("aabbcc") == 2


def test_spaces():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("a b c") == 3


def test_numbers_and_symbols():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("123123") == 3
    assert solution.lengthOfLongestSubstring("!@#!@#") == 3