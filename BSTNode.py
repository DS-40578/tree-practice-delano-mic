
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, new_data):
        if(new_data < self.data):
            if(self.left_child != None):
                self.left_child.insert(new_data)
            add_left(new_data)

        if(new_data > self.data):
            if(self.right_child != None):
                self.right_child.insert(new_data)
            add_right(new_data)

    def add_left(self, new_child_data):
        self.left_child = BSTNode(new_child_data)

    def add_right(self, new_child_data):
        self.right_child = BSTNode(new_child_data)

def main():
    root = BSTNode(100)