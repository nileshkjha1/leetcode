from longestcommonrefix import Solution


def test_longest_common_prefix():
    solution = Solution()

    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
    assert solution.longestCommonPrefix(["apple", "apple", "apple"]) == "apple"