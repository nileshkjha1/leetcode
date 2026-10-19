from firstoccinthestr import Solution


def test_str_str():
    solution = Solution()

    assert solution.strStr("sadbutsad", "sad") == 0
    assert solution.strStr("leetcode", "leeto") == -1
    assert solution.strStr("hello", "ll") == 2
    assert solution.strStr("aaaaa", "bba") == -1