# Nobleza, Bhea I.
# BSCPE 2-4
# Data Structure and Algorithm

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class List:
    def __init__(self, head=None):
        self.head = head

    def merge_lists(list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.value < list2.value:
            merged_head = list1
            merged_head.next = List.merge_lists(list1.next, list2)
        else:
            merged_head = list2
            merged_head.next = List.merge_lists(list1, list2.next)

        return merged_head

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next
        print()  

# Example usage
list1 = List(ListNode(1, ListNode(2, ListNode(4))))
list2 = List(ListNode(1, ListNode(3, ListNode(4))))

print("List 1: ", end="")
List(list1.head).print_list()

print("List 2: ", end="")
List(list2.head).print_list()

merged_list = List.merge_lists(list1.head, list2.head)

print("The Merged List is: ", end="")
List(merged_list).print_list()