class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLongestConsecutiveLength(head, common_diff):
    if not head:
        return 0

    max_length = 0
    current_length = 1

    # Create a dictionary to store the length of sequences ending at each element
    length_dict = {}

    while head:
        data = head.data

        # Check if the previous element in the sequence exists
        prev_data = data - common_diff

        # If the previous element is in the dictionary, update the current length
        if prev_data in length_dict:
            current_length = length_dict[prev_data] + 1
        else:
            current_length = 1

        # Update the length for the current element in the dictionary
        length_dict[data] = current_length

        # Update the maximum length
        max_length = max(max_length, current_length)

        head = head.next

    return max_length

# Helper function to create a linked list from a list of elements
def createLinkedList(elements):
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for elem in elements[1:]:
        current.next = Node(elem)
        current = current.next
    return head

# Read input
n = int(input())
elements = list(map(int, input().split()))

# Common difference for arithmetic progression
common_diff = elements[1] - elements[0]

# Create a linked list from the input elements
linked_list = createLinkedList(elements)

# Find the longest consecutive sequence length
result = findLongestConsecutiveLength(linked_list, common_diff)

# Print the result
print(result)
