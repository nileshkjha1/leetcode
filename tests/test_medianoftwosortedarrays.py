from medianoftwosortedarrays import Solution


def test_median_examples():
    solution = Solution()

    # Example 1
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0

    # Example 2
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5


def test_one_empty_array():
    solution = Solution()

    assert solution.findMedianSortedArrays([], [1]) == 1.0
    assert solution.findMedianSortedArrays([2], []) == 2.0


def test_same_values():
    solution = Solution()

    assert solution.findMedianSortedArrays([1, 1], [1, 1]) == 1.0


def test_negative_numbers():
    solution = Solution()

    assert solution.findMedianSortedArrays([-5, -3], [-2, -1]) == -2.5