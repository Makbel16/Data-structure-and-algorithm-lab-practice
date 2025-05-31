class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        print(f"{data} inserted at head.")

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"{data} inserted as the only node.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(f"{data} inserted at tail.")

    def delete(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next  # deleting head

                if temp.next:
                    temp.next.prev = temp.prev
                print(f"{data} deleted from the list.")
                return
            temp = temp.next
        print(f"{data} not found in the list.")

    def display_forward(self):
        temp = self.head
        print("List (forward):", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp.next:
            temp = temp.next
        print("List (backward):", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"{key} found in the list.")
                return True
            temp = temp.next
        print(f"{key} not found in the list.")
        return False


# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(5)
    dll.insert_at_tail(20)
    dll.insert_at_tail(25)
    dll.display_forward()
    dll.display_backward()
    dll.search(20)
    dll.delete(10)
    dll.display_forward()
