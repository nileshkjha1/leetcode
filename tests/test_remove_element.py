from removeelement import Solution


def test_remove_element():
    solution = Solution()

    nums = [3, 2, 2, 3]
    k = solution.removeElement(nums, 3)

    assert k == 2
    assert nums[:k] == [2, 2]


def test_remove_element_multiple():
    solution = Solution()

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = solution.removeElement(nums, 2)

    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]


def test_remove_element_no_match():
    solution = Solution()

    nums = [1, 2, 3]
    k = solution.removeElement(nums, 4)

    assert k == 3
    assert nums[:k] == [1, 2, 3]


def test_remove_element_empty():
    solution = Solution()

    nums = []
    k = solution.removeElement(nums, 1)

    assert k == 0
    assert nums[:k] == []