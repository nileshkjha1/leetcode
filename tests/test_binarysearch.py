from binaryserach import Solution


def test_search_insert():
    solution = Solution()

    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0