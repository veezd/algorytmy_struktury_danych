class treeNode:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


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
        
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
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

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))

        balance = self.get_balance(current)

        # RR
        if balance >= 2 and self.get_balance(current.left) >= 0:
            return self.rotate_right(current)
        
        # LR 
        if balance >= 2 and self.get_balance(current.left) < 0:
            current.left = self.rotate_left(current.left)
            return self.rotate_right(current)
        
        # LL
        if balance <= -2 and self.get_balance(current.right) <= 0:
            return self.rotate_left(current)
        
        # RL
        if balance <= -2 and self.get_balance(current.right) > 0:
            current.right = self.rotate_right(current.right)
            return self.rotate_left(current)

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

        if current is None:
            return current

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))

        balance = self.get_balance(current)

        # RR
        if balance >= 2 and self.get_balance(current.left) >= 0:
            return self.rotate_right(current)
        
        # LR 
        if balance >= 2 and self.get_balance(current.left) < 0:
            current.left = self.rotate_left(current.left)
            return self.rotate_right(current)
        
        # LL
        if balance <= -2 and self.get_balance(current.right) <= 0:
            return self.rotate_left(current)
        
        # RL
        if balance <= -2 and self.get_balance(current.right) > 0:
            current.right = self.rotate_right(current.right)
            return self.rotate_left(current)

        return current

    def print_as_list(self, current=None, start=True):
        if start:
            current = self.root
            print("[", end="")

        if current is not None:
            self.print_as_list(current.left, False)
            print(f"{current.key}:{current.data}", end=" ")
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


# utworzono puste drzewo
tree = binaryTree()

# dodano elementy
dic = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
for key, value in dic.items():
    tree.insert(key, value)

# drzewo wypisane
tree.print_tree()

# wypisane jako lista
tree.print_as_list()

# wypisz element spod klucza 10
print(tree.search(10))

# usuń element o kluczu 50,52,11,57,1,12
tree.delete(50)
tree.delete(52)
tree.delete(11)
tree.delete(57)
tree.delete(1)
tree.delete(12)

# dodaj element o kluczu 3:AA, 4:BB
tree.insert(3, "AA")
tree.insert(4, "BB")

# usuń element o kluczu 7, 8
tree.delete(7)
tree.delete(8)

# wyświetl drzewo 2D
tree.print_tree()

# wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
tree.print_as_list()