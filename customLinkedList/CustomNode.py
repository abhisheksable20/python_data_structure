class CustomNode:
    def __init__(self, a_data):
        self.data = a_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, a_next):
        self.next = a_next
