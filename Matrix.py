

import math
from typing import overload
from multipledispatch import dispatch


class Matrix(): #Définition d'une Classe qui représente les matrices
    """
    # Classe décrivant un Matrice[L][C] :
    - lines                : le nombre de lignes
    - colons               : le nombre de colonnes
    - dimension            : La dimension de la matrice
    - datas                : Le tableau 2D, de taille LXC 
    - numberMaxLenght      : La longueur Maximal des nombres dans la matrice
    """
    
    """
    @overload
    def __init__(self, L: int, C: int, null: bool = False) -> None: ...
        
    @overload 
    def __init__(self, n: int, nullOrId: bool = None) -> None: ... 

    @overload
    def __init__(self, array: list) -> None: ..."""
    
    
    @dispatch(int, int, bool)
    def __init__(self, L: int, C: int, null: bool = False) -> None:

        """
        - L : le nombre de lignes
        - C : le nombre de colonnes
        - si null = True ?? Renvoi une matrice nulle de taille LXC ...

        """

        #La matrice est 0-indexed

        #print("\nCREATION DE LA MATRICE\n")
        #numberMaxLen = 1(self.datas)
        self.lines = L
        self.colones = C
        self.dimension = (L, C)
        self.datas = [[0 for i in range(C)] for j in range(L)] #initialisation des donné de la matrice à 0.

        if(null == False):
            print("\nSAISIE DES DONNEES\n")
            print(
"""\nSaisir les lignes de façons que les données de chaques
ligne soient séparées au moins par un espaces.
EX : 3 4 6 -7 10\n"""
)

            for i in range(L):
                ligne = input(f"SVP : Saisir la ligne-{i+1} : ")
                ligne = ligne.split()
                max_len = max([len(num) for num in ligne])
                self.datas[i] = [float(j) for j in ligne]

                # Détermination itérative de 
                #if(numberMaxLen <= max_len) : numberMaxLen = max_len(self.datas)


            print("####\nSAISIE TERMINEE : MATRICE CRÉÉE AVEC SUCCES\n####")

    @dispatch(int, bool)
    def __init__(self, n: int, nullOrId: bool = None) -> None:
        """Permettra de créer une matrice une matrice carrées : 
        - L : le nombre de lignes = n
        - C : le nombre de colonnes = n
        - si nullOrID = True ?? Renvoi une matrice identité de taille LXC...
        - sinon si nullOrID = True ?? Renvoie une matrice carré nulle.
        - sinon Si eaucune valeur fourni pour nullOrID ?? Processus de création par défaut.
        """

        #La matrice est 0-indexed

        #print("\nCREATION DE LA MATRICE CARRÉE \n")
        #numberMaxLen = 1(self.datas)
        self.lines = n
        self.colones = n
        self.dimension = (n, n)
        self.datas = [[0 for i in range(n)] for j in range(n)] #initialisation des donné de la matrice à 0.

        
        if (nullOrId) :
            #numberMaxLen = 1(self.datas)
            for i in range(n):
                self[i][i] = 1

    
    @dispatch(list)
    def __init__(self, array: list):
        self.lines = len(array)
        self.colones = len(array[0])
        self.dimension = (self.lines, self.colones)
        self.datas = array
        #numberMaxLen = numberMaxLen(array)(self.datas)

    @dispatch(int)
    def __init__(self, n) -> None:
        
        print("\nSAISIE DES DONNEES\n")
        print(
"""\nSaisir les lignes de façons que les données de chaques
ligne soient séparées au moins par un espaces.
EX : 3 4 6 -7 10\n"""
)

        for i in range(n):
            ligne = input(f"SVP : Saisir la ligne-{i+1} : ")
            ligne = ligne.split()
            max_len = max([len(num) for num in ligne])
            self.datas[i] = [float(j) for j in ligne]

                # Détermination itérative de 
                #if(numberMaxLen <= max_len) : numberMaxLen = max_len(self.datas)
            print("####\nSAISIE TERMINEE : MATRICE CARRÉE CRÉÉE AVEC SUCCES\n####")
        
    
    def __repr__(self) -> str:
        """Une Représentation de la matrice sous forme visuelle."""
        #represent = "\n" + "\n".join(["  ".join([str(i) for i in []])]) #Effort de Représenter la matrice sous forme de tableau 2D
        represent = "\n"
        max_len = numberMaxLen(self.datas)
        for line in self.datas:
            line = [f"{str(i):>{max_len}}" for i in line]
            line = "  ".join(line)
            represent += line
            represent+="\n"

        return represent


    def __str__(self) -> str:
        """Permet d'afficher la matrice sous forme de tableau 2D."""
        #represent = "\n" + "\n".join(["  ".join([str(i) for i in []])]) #Effort de Représenter la matrice sous forme de tableau 2D
        represent = "\n"
        max_len = numberMaxLen(self.datas)
        for line in self.datas:
            line = [f"{str(i):>{max_len}}" for i in line]
            line = "  ".join(line)
            represent += line
            represent+="\n"

        return represent

    def __getitem__(self, index): 
        """Cette méthode spéciale est appelée quand on fait objet[index] Elle redirige vers self.datas[index] : (0-indexed mode)"""
        #index-=1
        return self.datas[index]

    def __setitem__(self, index, value):
        """Cette méthode est appelée quand on écrit objet[index] = valeur. On redirige vers self.datas[index] = valeur (0-indexed mode)"""
        #index-=1
        self.datas[index] = value
    
    def __add__(self, B):
        return sumMatrix(self, B)

    def __neg__(self):
        return mulByScalar(self, -1)

    def __sub__(self, B) :
        return self + mulByScalar(B, -1)
    
    def __rmul__(self, scalar):
        return mulByScalar(self, scalar)
    
    def __mul__(self, B):
        return productMatrix(self, B)

    def transpose(self):
        AT = Matrix(self.colones, self.lines, True)
        for i in range(self.colones):
            for j in range(self.lines):
                AT[i][j] = self[j][i]
                
        return AT
    
    def isDiagonalDominante(self):
        """Strictement dominante"""
        return all([(2*self[i][i] - sum(line)) > 0 for i,line in enumerate(self)])
        
    def isDiagonal(self) -> bool:
        diagonal = []
        #isDiagNonNull = any(diagonal) # Verifie si la diagonale est nulle ou pas
       # if(not isDiagNonNull) : return isDiagNonNull
        for i in range(self.lines):
            for j in range(self.colones):
                if(i!=j and self[i][j]!=0):
                    return False
                elif(i==j):
                    diagonal.append(self[i][j])

        return any(diagonal)
    
    def isTriDiagonal(self):
        triDiagonal = []
        if self.lines > 2 :
            #isDiagNonNull = any(diagonal) # Verifie si la diagonale est nulle ou pas
            # if(not isDiagNonNull) : return isDiagNonNull
            for i in range(self.lines):
                for j in range(self.colones):
                    if((abs(i-j) >1 ) and self[i][j]!=0):
                        return False
                    elif(abs(i-j) <= 1):
                        triDiagonal.append(self[i][j])

            return any(triDiagonal)

        return False

    def isSuperior(self):
        for i in range(self.lines):
            for j in range(self.colones):
                if(i>j and self[i][j]!=0) : return False

        return True


    def isInferior(self):
        for i in range(self.lines):
            for j in range(self.colones):
                if(i<j and self[i][j]!=0) : return False

        return True

    def mul_a_line_by_scalar(self, i:int, a:float): 
        """effectue l'operation suivante sur la matrice courante:\
            Li <-- a*Li

            i : numero de ligne(0-indexed mode)
        """
        self[i] = [a*numb for numb in self[i]]


    def permuteLines(self, i: int ,j:int):
        """effectue l'operation suivante sur la matrice courante :\
            Li <-- Lj
        """
        #print(i, j)
        self[i], self[j] = self[j], self[i]
        
        
    def sumLines(self, i: int, j: int):
        """effectue l'operation suivante sur la matrice courante :\
            Li <-- Li + Lj
        """
        self[i] = [numI + numJ for numI, numJ in zip(self[i], self[j])]
        
    def sumLinesFromOtherMatrix(self, i: int, B ,j: int, ):
        """Attionne la ligne j de B à la ligne i d la matrie courante : \
            self[i] += B[j]
        """
        self[i] = [numI + numJ for numI, numJ in zip(self[i], B[j])]


    def operationSurLigne(self, i: int , j: int, a : float):
        """Permet d'effectuer des operations elementaire sur les lignes d'une matrice\
            i : numero de la ligne sur la quelle la modification  est effectuée
            j : numero de la logne qui intervien dans l' operation elementaire
            a : Ce nombre intervient aussi dans l'oepration :\
                    Li <-- Li + a*Lj
        """
        temp = mulLineByScalar(self, j, a)
        self.sumLinesFromOtherMatrix(i, temp, j)
        


def sumMatrix(A: Matrix, B: Matrix) -> Matrix:
    """Retourne une matrice somme de A matrice et de la matrice courante. A.sumMatrix(B) = A+B"""
    L = A.lines 
    C = A.colones
    if(L == B.lines and C == B.colones):
            #S = Matrix(L, C)
            S = Matrix(L, C, True)
            for i in range(L):
                #somme.datas[i] = [sum(s) for s in zip(A.datas[i], B.datas[i])]
                S[i] = [sum(s) for s in zip(A[i], B[i])]
                
            return S
            
    else :
        raise ValueError("Impossible de cette somme de matrice Car Matrices de taille différente.")

def mulByScalar(A: Matrix, scalar : float) -> Matrix:
    """Effectue la multiplication de A par le scalaire <scalar>."""
    scalarProduct = Matrix(A.lines, A.colones, True)

    i = 0
    for ligne in A :
        scalarProduct.datas[i] = [scalar*data for data in ligne]
        i+=1

    return scalarProduct


def productMatrix(A: Matrix, B: Matrix):
    """Effectue le produit de deux matrice A et B"""
    if(A.colones == B.lines):
        P = Matrix(A.lines, B.colones,True)
        for i in range(A.lines):
            for j in range(B.colones):
                for k in range(A.colones):
                    P[i][j]+=(A[i][k]*B[k][j])
    
        return P

    else:
        raise ValueError("Impossible d'effecuter ce produit de matrice Car A.colones != B.lines.")



def numberMaxLen(array : list) -> int:
    """Cette Méthode static retourne une liste contenant L nombre représentant chacun
        le nombre Maximal de chiffre des chiffre de chaque colonnes.
    """
    maxi = 0
    maxi_len = 0
    l = len(array)
    c = len(array[0])

    for line in array:
        maxi = max([len(str(i)) for i in line])
        if(maxi_len < maxi) : maxi_len = maxi

    return maxi_len

def mulLineByScalar(M: Matrix, i:int, a:float)->Matrix: 
        """effectue l'operation suivante sur la matrice courante:\
            Li <-- a*Li

            i : numero de ligne(0-indexed mode)
        """
        Mtemp = Matrix(M.lines, M.colones, True)
        Mtemp[i] = [a*numb for numb in M[i]]
        
        return  Mtemp
