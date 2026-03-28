#NIESKONCZONE
class queue:
    def __init__(self,length=5):
        self.tab = [None for i in range(length)]
        self.save_i = 0
        self.read_i = 0
        self.size = 0

    def is_empty(self):
        if(self.save_i == self.read_i):
            return True
        else:
            return False
    
    def peek(self):
        if(self.is_empty()):
            return None
        
        return self.tab[self.read_i]
    
    def dequeue(self):
        if(self.is_empty()):
            return None
        
        var = self.tab[self.read_i]
        self.tab[self.read_i] = None # usuwa
        self.read_i += 1

        if(self.read_i >= len(self.tab)): # petla
            self.read_i = 0

        if self.size > 0:
            self.size -= 1

        return var
    
    def enqueue(self,data):
        self.tab[self.save_i] = data # wstaw dane
        self.save_i += 1
        self.size += 1


        if(self.save_i >= len(self.tab)): # petla
            self.save_i = 0
            
        if(self.read_i == self.save_i): # sprawdza czy indeksy sa takie same
            for i in range(len(self.tab)):
               self.tab.insert(self.read_i,None)
               self.read_i +=1

    def __str__(self):
        it_r = self.read_i # kopie do iteracji w funkcji

        output = "["
        for i in range(self.size):
            output += " " + str(self.tab[it_r]) + " "
            it_r += 1
            if it_r >= len(self.tab): # petla
                it_r = 0
        output += "]"
        return output

        


# Utworzenie pustej kolejki
q = queue()
# Enqueue wpisuje 4 dane
for i in range(1,5):
    q.enqueue(i)

# Dequeue odczyt i wypisanie pierwszej danej
print(q.dequeue())

# Peek do odczytu drugiej danej (aktualnego read_i)
print(q.peek())

# Testowe wypisanie stanu kolejki
print(q)

# 4 kolejne dane liczby od 5 do 8
for i in range(5,9):
    q.enqueue(i)

# Wypisanie wewnetrznego stanu tablicy
print(q.tab)

# Oproznienie kolejki z wypisaniem

while not (q.is_empty()):
    print(q.dequeue())

# Wypisanie pustej kolejki
    
print(q)


