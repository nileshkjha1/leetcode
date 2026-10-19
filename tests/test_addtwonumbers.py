import addtwonumbers
from addtwonumbers import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Make ListNode available to the solution
addtwonumbers.ListNode = ListNode


def create_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def get_values(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def test_add_two_numbers():
    solution = Solution()

    # 342 + 465 = 807
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])

    result = solution.addTwoNumbers(l1, l2)

    assert get_values(result) == [7, 0, 8]


def test_add_two_numbers_with_zero():
    solution = Solution()

    l1 = create_list([0])
    l2 = create_list([0])

    result = solution.addTwoNumbers(l1, l2)

    assert get_values(result) == [0]


def test_add_two_numbers_different_lengths():
    solution = Solution()

    # 9999 + 99 = 10098
    l1 = create_list([9, 9, 9, 9])
    l2 = create_list([9, 9])

    result = solution.addTwoNumbers(l1, l2)

    assert get_values(result) == [8, 9, 0, 0, 1]