# Merge-Linked-Lists Description

This Python script offers a fundamental implementation of singly linked lists and 
includes a function to combine two sorted linked lists into a unified, sorted linked list.

## Classes

### `ListNode`

- Represents a node in the linked list.
- Attributes:
  - `value`: The value of the node.
  - `next`: Reference to the next node.

### `List`

- Represents a singly linked list.
- Attributes:
  - `head`: Points to the first node in the list.

## Methods

### `merge_lists(list1, list2)`

- A method that accepts two sorted linked lists (list1 and list2) and combines them to generate a fresh, sorted linked list.
- It then yields the head of this merged list.

### `print_list()`

- A method associated with the List class, operating at the instance level.
- Prints the elements of the linked list in a sequential order.

## Example Usage

```python
# Create two sorted linked lists
list1 = List(ListNode(1, ListNode(2, ListNode(4))))
list2 = List(ListNode(1, ListNode(3, ListNode(4))))

# Print the original lists
print("List 1: ", end="")
List(list1.head).print_list()

print("List 2: ", end="")
List(list2.head).print_list()

# Merge the lists
merged_list = List.merge_lists(list1.head, list2.head)

# Print the merged list
print("The Merged List is: ", end="")
List(merged_list).print_list()
