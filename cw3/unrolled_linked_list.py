class node:
    def __init__(self):
        size = 4
        self.tab = [None for i in range(size)]
        self.elements = 0 # ilosc elementow w node
        self.next = None
        # metoda wstaw i usun w indeks?

    def insert(self,indice,data): #shit
        self.tab.insert(indice,data)
        self.elements += 1

class unrolled_list:
    def __init__(self):
        self.head = node()

    def __get__(self):
        