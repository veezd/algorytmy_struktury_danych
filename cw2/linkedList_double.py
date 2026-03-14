#SKONCZONE

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # create robi to konstruktor
    
    def destroy(self): # destroy
        ptr = self.head

        while ptr is not None:
            temp = ptr.next
            ptr.next = None
            ptr.prev = None
            ptr = temp

        self.head = None
        self.tail = None
                
    def add(self, data): # na poczatek
        node = listNode(data)
        if(self.head == None and self.tail == None): # Lista jest pusta
            self.head = node
            self.tail = node
            return None

        self.head.prev = node
        node.next = self.head
        self.head = node

        return None
    
    def append(self,data): # na koniec
        node = listNode(data)

        if(self.head == None and self.tail == None): # Jezeli nie ma zadnych Node to uczyn go pierwszym
            self.head = node
            self.tail = node
            return None
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        return None

    def pop_front(self): # remove
        if self.head is None :
            return None

        if(self.head.next == None): #1 element w liscie 
            self.head = None
            self.tail = None
            return None
        
        second_node = self.head.next
        second_node.prev = None
        self.head = second_node

        return None
        

    def pop_back(self): # remove_end
        if (self.tail == None):
            return None
        
        if (self.tail.prev == None): # 1 element w liscie
            self.head = None
            self.tail = None
            return None
        
        second_to_last = self.tail.prev
        second_to_last.next = None
        self.tail = second_to_last

        return None

    def is_empty(self):
        if(self.head == None and self.tail == None):
            return True
        else:
            return False
        
    def __len__(self): # length
        size = 0
        ptr = self.head

        while(ptr != None):
            size += 1
            ptr = ptr.next

        return size
    
    def get(self):
        if(self.head == None):
            return None
        return self.head.data
    

    def __str__(self): # aka print
        ptr = self.head
        output = ""
        while(ptr != None):
            output += "-> " + str(ptr.data) + "\n"
            ptr = ptr.next

        return output
    
    def printBackwards(self): # aka print od tylu
        ptr = self.tail
        output = ""

        while(ptr != None):
            output += "-> " + str(ptr.data) + "\n"
            ptr = ptr.prev
        return output
    

class listNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

lista_uczelni = [
    ('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)
]

#
uczelnie = linkedList()
#
for i in range (0,3):
    uczelnie.append(lista_uczelni[i])
#
uczelnie.add(lista_uczelni[3])
uczelnie.add(lista_uczelni[4])
uczelnie.add(lista_uczelni[5])
#
print(uczelnie)
print(uczelnie.printBackwards())
#
print("Długość listy : " + str(len(uczelnie)))
#
uczelnie.pop_front()
#
print("Obecny HEAD listy: " + str(uczelnie.get()))
#
uczelnie.pop_back()
#
print(uczelnie)
print(uczelnie.printBackwards())
#
uczelnie.destroy()
#
print("Czy lista jest pusta? : " + str(uczelnie.is_empty()))
#
uczelnie.pop_front()
uczelnie.pop_back()
#
uczelnie.append(lista_uczelni[0]) # AGH
uczelnie.pop_back()
print("Czy AGH usunięto? :( " + str(uczelnie.is_empty()))
print(uczelnie)
