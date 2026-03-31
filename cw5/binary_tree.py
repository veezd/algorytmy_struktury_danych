class treeRoot:
    def __init__(self,rootNode):
        self.rootNode = rootNode

class treeNode:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.root = None

    # Wyszukuje wartosc wdg klucza lub None
    def search(self):
        return
    
    # Wstawia dana wdg klucza, jezeli klucz istnieje nadpisz
    def insert(self,node,root = None, start = True):
        if start:
            root = self.root # start od korzenia oryginalnego
            if self.root is None: # sytuacja ze drzewo puste
                self.root = node
                return

        if root.left is None: # lewa pusta
            root.left = node
            return
        elif root.right is None: # prawa pusta
            root.right = node
            return

        # jak nie sa puste to skaczemy wyzej az sie uda
        
        if node.key < root.key : # klucz 
            self.insert(node,root.left,start=False)
            return
        else:
            self.insert(node,root.right,start=False)
            return
    
    # Usuwa dana spod podanego klucza
    # usuwanie wezla bez dzieci
    # usuwanie wezla z jednym dzieckiem
    # usuniecie wezla z dwojka dzieci, zastapic wezel zastepujemy wezlem bez lewego potomka?
    def delete(self):
        return
    
    # wypisuje jako liste (jak w przykladzie)
    def print_as_list(self):
        return
    
    # wypisuje cala strukture drzewa w 2D
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
    
    # wypisuje maksymalna wysokosc drzewa (najdluzsza sciezka)
    def height(self):
        return
    


tree = binaryTree()
for i in range(8):
    node = treeNode(i,"dana")
    tree.insert(node)

tree.print_tree()