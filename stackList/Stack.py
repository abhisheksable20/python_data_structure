# Stack Data Structure using list

class Stack:
    def __init__(self, stack_size):
        self.stack = []
        self.top = -1

        for i in range(stack_size):
            self.stack.append(-1)

    def insert_data(self, data):
        if self.top >= len(self.stack):
            return "Stack size full"

        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            return -1

        data = self.stack[self.top]
        self.top -= 1
        return data

    def iterate(self):
        if self.top == -1:
            print("Stack is empty")
            return -1

        temp = self.top
        while temp >= 0:
            print(self.stack[temp])
            temp -= 1
