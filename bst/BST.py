# Exclusive class for BST

from customLinkedList.LinkedList import LinkedList


class BSTNode:
    """
    Binary Search Tree
    with self-balancing feature
    """

    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BST:
    """
    Binary Search Tree
    Left Node will be smaller
    Right Node will be larger
    """

    def __init__(self):
        self.head = None

    def insert(self, data):
        self.head = BST.insert_data(self.head, data)

    def is_data_exist(self, data):
        return BST.exist(self.head, data)

    # Check weather the data exist in this tree
    @staticmethod
    def exist(node, data):
        while node is not None:
            if node.get_data() == data:
                return True

            if data < node.get_data():
                node = node.left
            else:
                node = node.right

        return False

    @staticmethod
    def insert_data(node, data):
        if node is None:
            return BSTNode(data)

        if data > node.get_data():
            node.right = BST.insert_data(node.get_right(), data)
        elif data < node.get_data():
            node.left = BST.insert_data(node.get_left(), data)
        else:
            return node

        node.height = 1 + BST.get_max(BST.get_height(node.left), BST.get_height(node.right))

        # Performing the balancing
        balance = BST.get_balance(node)

        # Left - Left Case
        if balance > 1 and data < node.left.get_data():
            return BST.right_rotate(node)

        # Right - Right Case
        if balance < -1 and data > node.right.get_data():
            return BST.left_rotate(node)

        # Left - Right Case
        if balance > 1 and data > node.left.get_data():
            node.left = BST.left_rotate(node.left)
            return BST.right_rotate(node)

        # Right - Left Case
        if balance < -1 and data < node.right.get_data():
            node.right = BST.right_rotate(node.right)
            return BST.left_rotate(node)

        return node

    def delete(self, data):
        self.head = BST.delete_node(self.head, data)

    @staticmethod
    def delete_node(node, data):
        if node is None:
            return node

        if data < node.get_data():
            node.left = BST.delete_node(node.left, data)
        elif data > node.get_data():
            node.right = BST.delete_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            data = BST.get_min_data(node.right)
            node.data = data
            node.right = BST.delete_node(node.right, data)

        if node is None:
            return node

        node.height = 1 + BST.get_max(BST.get_height(node.left), BST.get_height(node.right))

        balance = BST.get_balance(node)

        # Left - Left Rotate
        if balance > 1 and BST.get_balance(node.left) >= 0:
            return BST.left_rotate(node)

        # Left - Right Rotate
        if balance > 1 and BST.get_balance(node.left) < 0:
            node.left = BST.left_rotate(node.left)
            return BST.right_rotate(node)

        # Right - Right Rotate
        if balance < -1 and BST.get_balance(node.right) <= 0:
            return BST.right_rotate(node)

        # Right - Left Rotate
        if balance < -1 and BST.get_balance(node.right) > 0:
            node.right = BST.right_rotate(node.right)
            return BST.left_rotate(node)

        return node

    @staticmethod
    def get_min_data(node):
        data = node.get_data()
        while node.left is not None:
            data = node.left.get_data()
            node = node.left

        return data

    # Get Head Node Height
    def get_head_height(self):
        return BST.get_height(self.head)

    @staticmethod
    def left_rotate(x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + BST.get_max(BST.get_height(x.left), BST.get_height(x.right))
        y.height = 1 + BST.get_max(BST.get_height(y.left), BST.get_height(y.right))

        return y

    @staticmethod
    def right_rotate(y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        x.height = 1 + BST.get_max(BST.get_height(x.left), BST.get_height(x.right))
        y.height = 1 + BST.get_max(BST.get_height(y.left), BST.get_height(y.right))

        return x

    @staticmethod
    def get_max(a, b):
        if a > b:
            return a
        else:
            return b

    # Get Current Node Height
    @staticmethod
    def get_height(node):
        if node is None:
            return 0

        return node.height

    @staticmethod
    def get_balance(node):
        if node is None:
            return 0

        return BST.get_height(node.left) - BST.get_height(node.right)

    @staticmethod
    def level_order_traversal(node, queue):
        if node is None:
            print("Empty Binary Tree!!")

        queue.insert_node(node)
        queue.insert_node(None)

        while not queue.is_empty():
            curr_node = queue.pop()

            if curr_node is None:
                if queue.is_empty():
                    break

                queue.insert_node(None)
                print()
                continue

            print(curr_node.get_data(), end=" ")

            if curr_node.left is not None:
                queue.insert_node(curr_node.left)

            if curr_node.right is not None:
                queue.insert_node(curr_node.right)

    def level_traversal(self):
        queue = LinkedList()
        BST.level_order_traversal(self.head, queue)

    def print(self):
        self.print_tree(self.head)

    def print_tree(self, node):
        if node is None:
            return

        self.print_tree(node.get_left())
        print(node.get_data(), end=" ")
        self.print_tree(node.get_right())
