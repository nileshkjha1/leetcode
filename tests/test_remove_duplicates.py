import importlib.util
from pathlib import Path


file_path = Path(__file__).parent.parent / "Remove Duplicates from Sorted Array.py"

spec = importlib.util.spec_from_file_location(
    "remove_duplicates",
    file_path
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Solution = module.Solution


def test_remove_duplicates():
    solution = Solution()

    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)

    assert k == 2
    assert nums[:k] == [1, 2]


def test_remove_duplicates_multiple():
    solution = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)

    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]


def test_remove_duplicates_empty():
    solution = Solution()

    nums = []
    k = solution.removeDuplicates(nums)

    assert k == 0



