import mergetwolist
from mergetwolist import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Give the solution the ListNode class it expects
mergetwolist.ListNode = ListNode


def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def test_merge_two_lists():
    solution = Solution()

    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    result = solution.mergeTwoLists(list1, list2)

    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]


def test_merge_with_empty_list():
    solution = Solution()

    list1 = create_linked_list([])
    list2 = create_linked_list([1, 2, 3])

    result = solution.mergeTwoLists(list1, list2)

    assert linked_list_to_list(result) == [1, 2, 3]


def test_merge_both_empty():
    solution = Solution()

    list1 = create_linked_list([])
    list2 = create_linked_list([])

    result = solution.mergeTwoLists(list1, list2)

    assert linked_list_to_list(result) == []