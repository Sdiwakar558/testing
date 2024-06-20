class Node:
    def __init__(self,data):
        self.next=None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next=new_Node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Create a new linked list and insert the values 2, 3, 4, 5, 6, 7
new_linked_list = LinkedList()
values = [2, 3, 4, 5, 6, 7]

for value in values:
    new_linked_list.insert(value)

# Print the linked list to verify
print("Linked List:")
new_linked_list.print_list()
        


