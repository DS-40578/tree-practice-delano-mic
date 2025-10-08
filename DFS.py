class DFS:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def find(self, search_data):
        print(f'{self.data} == {search_data}')
        if(self.data == search_data):
            return self.data

        match = None

        if(self.left_child is not None):
            match = self.left_child.find(search_data)

        if(self.right_child is not None and not match):
            match = self.right_child.find(search_data)

        return match 

    def insert(self, new_data):
        if(new_data < self.data):
            if(self.left_child != None):
                self.left_child.insert(new_data)
            self.add_left(new_data)

        if(new_data > self.data):
            if(self.right_child != None):
                self.right_child.insert(new_data)
            self.add_right(new_data)

    def add_left(self, new_child_data):
        self.left_child = DFS(new_child_data)

    def add_right(self, new_child_data):
        self.right_child = DFS(new_child_data)

def main():
    root = DFS(100)
    root.insert(99)
    root.insert(98)
    root.insert(97)
    root.insert(96)
    root.insert(95)

    root.insert(105)
    root.insert(104)
    root.insert(103)
    root.insert(102)
    root.insert(101)

    match = root.find(101)

    print(f'Found {match}')

main()


