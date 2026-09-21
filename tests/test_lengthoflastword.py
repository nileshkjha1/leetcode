from lengthoflastword import Solution


def test_length_of_last_word():
    solution = Solution()

    assert solution.lengthOfLastWord("Hello World") == 5
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6
    assert solution.lengthOfLastWord("Hello") == 5
    assert solution.lengthOfLastWord("a") == 1