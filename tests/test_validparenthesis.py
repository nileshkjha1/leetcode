from validparenthesis import Solution


def test_valid_parentheses():
    solution = Solution()

    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("{[]}") is True


def test_invalid_parentheses():
    solution = Solution()

    assert solution.isValid("(]") is False
    assert solution.isValid("([)]") is False
    assert solution.isValid("]") is False


def test_unclosed_parentheses():
    solution = Solution()

    assert solution.isValid("(") is False
    assert solution.isValid("(((") is False
    assert solution.isValid("{[") is False


def test_empty_string():
    solution = Solution()

    assert solution.isValid("") is True