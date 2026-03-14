class linkedList:
    def __init__(self): # zaczyna sie łbem a kończy ogonem
        self.head = None
        self.tail = None
    # create robi to konstruktor
    
    def destroy(self): # destroy TODO
        self.head = None
        
    def add(self, data): # na poczatek TODO
        node = listNode(data)
        node.next = self.head
        self.head = node # prev dalej domyslnie NULL bo 1 element

        if(self.head.next == None):
            self.tail = node # gdy lista ma jeden element koncowka jest poczatkiem
    
    def append(self,data): # na koniec 
        node = listNode(data)

        if (self.head == None): # pusta lista
            self.head = node
            self.tail = node
            return None
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node 

        return None

    def pop_front(self): # remove
        if self.head is None :
            return None

        self.head = self.head.next

        return None
        

    def pop_back(self): # remove_end
        if (self.head == None):
            return None
        
        if (self.head.next == None):
            self.head = None
            return None
        
        ptr = self.head

        while(ptr.next.next != None):
            ptr = ptr.next

        ptr.next = None

        return None

    def is_empty(self):
        if(self.head == None):
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
    

class listNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
