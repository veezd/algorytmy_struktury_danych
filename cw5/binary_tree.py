# SKONCZONE
class treeNode:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self):
        self.root = None

    def search(self,key,current=None,start=True):
        if start:
            current = self.root
        
        if current is None:
            return None
        if current.key == key:
            return current.data

        if key < current.key:
            return self.search(key,current.left,False)
        else:
            return self.search(key,current.right,False)
        
    
    def insert(self, key, data, current=None, start=True):
        if start:
            self.root = self.insert(key, data, self.root, start=False)
            return

        if current is None:
            return treeNode(key, data)

        if key < current.key:
            current.left = self.insert(key, data, current.left, start=False)
        elif key > current.key:
            current.right = self.insert(key, data, current.right, start=False)
        else:
            current.data = data

        return current

    def delete(self, key, current=None, start=True):
        if start:
            self.root = self.delete(key, self.root, False)
            return self.root

        if current is None:
            return None

        if key < current.key:
            current.left = self.delete(key, current.left, False)

        elif key > current.key:
            current.right = self.delete(key, current.right, False)

        else:
            # brak dzieci
            if current.left is None and current.right is None:
                return None

            # jedno dziecko
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left

            # dwojka dzieci 
            temp = current.right
            while temp.left is not None:
                temp = temp.left

            current.key = temp.key
            current.data = temp.data
            current.right = self.delete(temp.key, current.right, False)

        return current

    def print_as_list(self, current=None, start=True):
        if start:
            current = self.root
            print("[", end="")

        if current is not None:
            self.print_as_list(current.left, False)
            print(f"({current.key},{current.data})", end=" ")
            self.print_as_list(current.right, False)

        if start:
            print("]")

    def height(self, current=None, start=True):
        if start:
            current = self.root

        if current is None:
            return -1

        left_h = self.height(current.left, False)
        right_h = self.height(current.right, False)

        return 1 + max(left_h, right_h)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)

# utworzone puste drzewo
tree = binaryTree()

# dodano elementy
dic =  {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
for key, value in dic.items():
    tree.insert(key, value)

# drzewo wypisane
tree.print_tree()

# wypisane jako lista
tree.print_as_list()

# wypisz wartosc spod klucza 24
print(tree.search(24))

# AA do klucza 20
tree.insert(20,"AA")

# dodaj element 6:M
tree.insert(6,"M")

# usun klucz 62
tree.delete(62)

# dodaj elementy 59:N 100:P
tree.insert(59,"N")
tree.insert(100,"P")

# usun klucze 8 15
tree.delete(8)
tree.delete(15)

# wstaw 55:R
tree.insert(55,"R")

# usun klucze 50 5 24
tree.delete(50)
tree.delete(5)
tree.delete(24)

# wypisz wysokosc drzewa
print(tree.height())

# wyswietl jako liste
tree.print_as_list()

# wyswietl jako drzewo
tree.print_tree()
