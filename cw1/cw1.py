#NIESKONCZONE

class matrix:
    def __init__(self, list, o=0):
        if (isinstance(list,tuple)): # Krotka
            if (len(list) != 2):
                raise ValueError("Krotka nie zawiera dokładnie dwóch elementów")
            if not ( isinstance(list[0],int) and isinstance(list[1],int) ):
                raise TypeError("Elementy krotki mają niezgodny typ danych")
            if ( list[0] < 0 or list[1] < 0):
                raise ValueError("Wiersze i kolumny muszą być dodatnie")
            if( (list[0] == 0 or list[1] == 0) and list[0] != list[1] ):
                raise ValueError("Podana para liczb tworzy niepoprawna macierz")
            
            # Po wstepnym sprawdzeniu wiemy ze krotka na pewno jest poprawna lub rowna 0,0

            if(list == (0,0)):
                self._matrix = []
            else:
                self._matrix = []
                for i in range (0,list[0]):
                    self._matrix.append([o] * list[1])

        else: # W przeciwnym wypadku zakladamy ze otrzymalismy liste list
            self._matrix = []
            for i in list:
                if len(i) != len(list[0]):
                    raise ValueError("Wiersze macierzy mają różne wielkosci")
                for j in i:
                    if not isinstance(j,(int,float)):
                        raise TypeError("Elementy macierzy muszą być liczbami")
            self._matrix = list

    def __str__(self):
        # zgodnie z zalozeniami mamy poprawnie zbudowana macierz z konstruktora
        if(self.size() == (0,0)):
            return "| |" # wyjatek pustej macierzy
        
        output = ""
        for i in self._matrix:
            output = output + "| "
            for j in i:
                output = output + str(j)  + " "
            output = output + "|\n"

        return output
    
    def size(self):
        rows = len(self._matrix)

        if(rows == 0):
            return (0,0)
            
        cols = len(self._matrix[0]) # znowu, konstruktor gwarantuje poprawna macierz
        return (rows,cols)
    
    def __getitem__(self,row):
        if(len(self._matrix) == 0):
            raise IndexError("Macierz jest pusta")
        elif( row > (self.size()[0]-1)):
            raise IndexError("Indeks wiersza wychodzi poza zakres macierzy")
        else:
            return self._matrix[row] # dla spojnosci zapisu trzeba podawac indeksy jak w liscie 0,1,2 etc

    def __add__(self,val):
        if(self.size() != val.size()):
            raise ValueError("Wymiary dodawanych macierzy są nierówne")
        
        if( (self.size() == (0,0)) and (val.size() == (0,0)) ):
            return matrix((0,0)) # puste macierze daja pusta macierz
        
        else:
            it = self.size() # wiemy ze maja te same wymiary
            M = matrix(it)
            for i in range (0,it[0]):
                for j in range (0, it[1]):
                    M[i][j] = self._matrix[i][j] + val._matrix[i][j]
            return M
        
    def __mul__(self,val):
        if(self.size() != val.size()[::-1] ): 
            raise ValueError("Wymiary mnozonych macierzy sa niezgodne")
        else:
            it = self.size()
            result_lst = []
  
            for i in range (0,it[0]): # iteruje po wierszach lewej macierzy
                vect = []
                for j in range (0,it[0]): # iteruje kolumnach prawej macierzy
                    sum = 0
                    for k in range(0,it[1]): # kolumnu lewej wiersze prawej
                        sum += self._matrix[i][k] * val._matrix[k][j]
                    vect.append(sum)
                result_lst.append(vect)

            return matrix(result_lst) #uzyty konstruktor z lista
        
    def __eq__(self,val):
        if(self.size() != val.size()):
            return False
        else:
            for i in range(0,self.size()[0]):
                if(self._matrix[i] != val._matrix[i]):
                    return False
            return True

                

def transposition(matrix_in):
    rows,cols = matrix_in.size()
    output = matrix((cols,rows))
    for i in range(rows):
        for j in range(cols):
            output[j][i] = matrix_in[i][j]

    return output

# Funkcje dodane do zadania dodatkowego

def det_2_2(matrix_in):
    if(matrix_in.size() != (2,2)): # bedzie uzywana jako funkcja pomocniczna do liczenia TYLKO macierzy 2x2
        raise ValueError("Błędny wymiar macierzy, oczekiwany 2x2")
    else:
        return matrix_in[0][0]*matrix_in[1][1] - matrix_in[1][0]*matrix_in[0][1]

def chio_method(matrix_in):
    if(matrix_in.size()[0] != matrix_in.size()[1]): # warunek na macierz kwadratowa
        raise ValueError("Macierz musi byc kwadratowa!") 
    
    a11 = matrix_in[0][0]

    if a11 == 0:
        raise ValueError("A11 = 0, niedopuszczalne")
    if matrix_in.size()[0] == 2:
        return det_2_2(matrix_in)
    
    rows,cols = matrix_in.size()
    matrix_out = matrix((rows-1,cols-1))
    for i in range (0, rows-1):
        for j in range (0, cols-1):
            temp_matrix = matrix([
                [matrix_in[0][0],matrix_in[0][j+1]],
                [matrix_in[i+1][0],matrix_in[i+1][j+1]]
            ])
            matrix_out[i][j] = det_2_2(temp_matrix)

    return (1 / (a11 ** (matrix_in.size()[0]-2))) * chio_method(matrix_out)

    
A = matrix([
[5 , 1 , 1 , 2 , 3],
[4 , 2 , 1 , 7 , 3],
[2 , 1 , 2 , 4 , 7],
[9 , 1 , 0 , 7 , 0],
[1 , 4 , 7 , 2 , 2]
] )
print(chio_method(A))           

    

