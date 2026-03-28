class hash_tab:
    def __init__(self,size,c1 = 1, c2 = 0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    # funkcja moze otrzymac napis lub liczbe (napis zamienic na liczbe)
    def search(self,key):
        for i in range(self.size):
            if self.tab[i] == None:
                continue
            elif self.tab[i].key == key:
                return self.tab[i].val   
        return None # gdy nic nie znajdzie
    

    def hash_func(self,key):
        # override bedzie sluzyc do ignorowania kolizji (do insert)

        if type(key) == str:
            hash_value = 0
            for letter in key:
                ascii_val = ord(letter)
                hash_value += ascii_val 

        else : # zalozenie ze jest to liczba calkowita
            hash_value = key

        id = hash_value % self.size # h(k)

        return  id
    
    def solve_collision(self,id,key,override = False):
        for i in range(self.size): # ilosc prob znalezienia wolnego miejcsa ograniczona do wielkosci tablicy
            new_id = (id + self.c1 * i + self.c2 * i**2) % self.size
            # H(k,i) = ( h(k), +ic1 + i^2c2 ) mod m
            if self.tab[new_id] == None:
                return new_id

            if override and self.tab[new_id].key == key:
                # gdy chcemy nadpisac znajdzie ID pod ktorym znajduje sie ten klucz
                return new_id
            
            
            
        return None # zwraca None gdy nie ma gdzie upchnac danej
        
    def insert(self,node): # node -> tab_node
        id = self.hash_func(node.key)
        idx = self.solve_collision(id,node.key,override = True)
        # jezeli element o takim key juz istnieje to zwroci nam jego id zamiast szukac pustego miejsca
        if idx is None: # przepelnienie
            raise IndexError("Tablica przepełniona!")
        self.tab[idx] = node
        return None
    
    def remove(self,key):
        id = self.hash_func(key)
        for i in range(self.size):
            new_id = (id + self.c1 * i + self.c2 * i**2) % self.size
            
            # usuniecie obiektu
            if self.tab[new_id].key == key:
                self.tab[new_id] = None
                return None 
                
        raise IndexError("Brak usuwanej danej")


    def __str__(self): # skonczone
        output = "{ "
        for i in range(self.size):
            output += str(self.tab[i]) + " "
        output += "}"
        return output

class tab_node: # skonczone
    def __init__(self,key,val):
        self.key = key
        self.val = val

    def __str__(self):
        string = str(self.key) + " : " + str(self.val)
        return string
    
def pierwsza(konstruktor):
    size = konstruktor[0]
    c1 = konstruktor [1]
    c2 = konstruktor[2]
    tablica = hash_tab(size) # domyslnie probkowanie liniowe

    for i in range(1,16):

        if i == 6:
            node = tab_node(18,str(64+i))
        elif i == 7:
            node = tab_node(31,str(64+i))
        else:
            node = tab_node(i,str(64+i))

        tablica.insert(node)

    print(tablica)


dane = (13,1,0)
pierwsza(dane)
