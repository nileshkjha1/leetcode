
import unittest
import importlib.util
from pathlib import Path

# Locate the solution file in the project root
solution_path = (
    Path(__file__).resolve().parent.parent
    / "2089_target_indices.py"
)

spec = importlib.util.spec_from_file_location(
    "solution_2089_target_indices",
    solution_path
)

solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

Solution = solution_module.Solution


class TestTargetIndices(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.targetIndices([1, 2, 5, 2, 3], 2),
            [1, 2]
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.targetIndices([1, 2, 5, 2, 3], 3),
            [3]
        )

    def test_example_3(self):
        self.assertEqual(
            self.solution.targetIndices([1, 2, 5, 2, 3], 5),
            [4]
        )

    def test_target_not_found(self):
        self.assertEqual(
            self.solution.targetIndices([1, 2, 3], 4),
            []
        )

    def test_all_elements_are_target(self):
        self.assertEqual(
            self.solution.targetIndices([2, 2, 2], 2),
            [0, 1, 2]
        )

    def test_single_element(self):
        self.assertEqual(
            self.solution.targetIndices([5], 5),
            [0]
        )


if __name__ == "__main__":
    unittest.main()

