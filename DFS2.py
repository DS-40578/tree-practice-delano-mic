class DFS2:
    def __init__(self, data):
        self.data = data
        self.children = None

    def find(self, search_data):
        print(f'{self.data} == {search_data}')
        if(self.data == search_data):
            return self

        match = None

        if(self.children is not None):
            for child in self.children:
                match = child.find(search_data)
                if match is not None:
                    return match

        return match
    def insert(self, new_data):
        if(self.children is None):
            self.children = []

        new_child = DFS2(new_data)
        self.children.append(new_child)

        return new_child

    def deep_add(self, child, parent):
        match = self.find(parent)
        return match.insert(child)

def main():
    ceo = DFS2("CEO")
    ceo.deep_add("Tadashi", "CEO")
    tadashi = ceo.insert("Tadashi")
    ewen = tadashi.insert("Ewen")
    ewen.insert("Tyrone")
    seneka = ceo.insert("Seneka")
    amy = seneka.insert("Amy")
    amy.insert("Jeff")
    amy.insert("Argos")
    amy.insert("Tama")
    ceo.insert("Seneka")
    seneka.insert("Abdul")

    jeff = ceo.find("Jeff")
    print(f'Found {jeff}')

    ceo.deep_add("Monica", "Jeff")
    monica =  ceo.find("Monica")
    print(f'Found {monica}')

main()


