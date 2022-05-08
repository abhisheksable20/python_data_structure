from customLinkedList.CustomNode import CustomNode


# Custom Linked List in Python
# You can use it as Queue Data Structure also
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert data in list
    def insert_node(self, data):
        self.size += 1
        if self.head is None:
            self.head = CustomNode(data)
            self.tail = self.head
            return

        new_node = CustomNode(data)
        self.tail.set_next(new_node)
        self.tail = new_node

    # Iterate through list
    def iterate(self):
        temp = self.head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    # Delete first item from list
    def pop(self):
        if self.head is None:
            return None

        data = self.head.get_data()
        self.head = self.head.get_next()

        if self.head is None:
            self.tail = None

        self.size -= 1

        return data

    # Delete Last element
    def delete_last(self):
        if self.head is None:
            return -1

        self.size -= 1

        if self.head == self.tail:
            data = self.head.get_data()
            self.head = None
            self.tail = None
            return data

        temp = self.head
        prev = None
        while temp is not self.tail:
            prev = temp
            temp = temp.get_next()

        data = temp.get_data()

        prev.set_next(None)
        self.tail = prev
        return data

    # Delete data from list
    def delete(self, data):
        if self.head is None or not isinstance(data, type(self.head.get_data())):
            return 0

        temp = self.head
        prev = None
        while temp is not None:
            if temp.get_data() == data:
                if temp == self.head:
                    self.pop()
                    return
                else:
                    prev.set_next(temp.get_next())
                    if temp == self.tail:
                        self.tail = prev
                    return

            prev = temp
            temp = temp.get_next()
            self.size -= 1

        return 0

    # Check weather item exist is list
    def exists(self, data):
        if self.head is None or not isinstance(data, type(self.head.get_data())):
            return False

        temp = self.head
        while temp is not None:
            if temp.get_data() == data:
                return True

            temp = temp.get_next()

        return False

    # Get list size
    def get_size(self):
        return self.size

    # Check weather the list is empty or not
    def is_empty(self):
        return self.size == 0
