#SKONCZONE
node_size = 6 # rozmiar node'a jednego

class Node:
    def __init__(self):
        self.tab = [None for _ in range(node_size)]
        self.fill = 0
        self.next = None

    def insert_at(self, idx, item):
        for i in range(self.fill, idx, -1):
            self.tab[i] = self.tab[i-1]
        self.tab[idx] = item
        self.fill += 1

    def delete_at(self, idx):
        item = self.tab[idx]
        for i in range(idx, self.fill - 1):
            self.tab[i] = self.tab[i+1]
        self.tab[self.fill - 1] = None
        self.fill -= 1
        return item

    def __str__(self):
        return str(self.tab) # do testow


class unrolled_list:
    def __init__(self):
        self.head = Node()
    
    def get(self, id):
        curr = self.head
        while curr:
            if id < curr.fill:
                return curr.tab[id]
            id -= curr.fill
            curr = curr.next
        raise IndexError("Id poza zakresem")
    
    def insert(self, id, item):
        curr = self.head
        
        while curr.next is not None and id >= curr.fill:
            id -= curr.fill
            curr = curr.next
            
        if id > curr.fill:
            id = curr.fill

        if curr.fill == node_size:
            new_node = Node()
            half = node_size // 2
            
            for i in range(half, node_size):
                new_node.tab[i - half] = curr.tab[i]
                curr.tab[i] = None
            
            curr.fill = half
            new_node.fill = node_size - half
            
            new_node.next = curr.next
            curr.next = new_node
            
            if id <= half:
                curr.insert_at(id, item)
            else:
                new_node.insert_at(id - half, item)
        else:
            curr.insert_at(id, item)

    def delete(self, id):
        curr = self.head
        
        while curr:
            if id < curr.fill:
                break
            if curr.next is None:
                raise IndexError("Id poza zakresem")
            id -= curr.fill
            curr = curr.next
            
        curr.delete_at(id)
        half = node_size // 2
        if curr.fill < half and curr.next is not None:
            if curr.fill + curr.next.fill <= node_size:
                for i in range(curr.next.fill):
                    curr.tab[curr.fill] = curr.next.tab[i]
                    curr.fill += 1
                curr.next = curr.next.next
            else:
                while curr.fill < half:
                    borrowed = curr.next.delete_at(0)
                    curr.insert_at(curr.fill, borrowed)
                    
    def __str__(self): # tez do testow
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.tab))
            curr = curr.next
        return " >> ".join(res)
    
# utworzona pusta lista
lista = unrolled_list()

# wywolanie insert dla 1-9
for i in range(1,10):
    lista.insert(i-1,i) # id, wartosc, id wieksze wiec dodaje na koniec

# get dla elementu o id 4
a = lista.get(4)

# inset 10, 11 pod id 1,8
lista.insert(1,10)
lista.insert(8,11)

# wypisanie stanu listy tablic
print(lista)

# uysuniecie id 1,2
lista.delete(1)
lista.delete(2)

# drugi wypis stanu
print(lista)
