import signal
from copy import deepcopy
from colorama import Fore

import numpy as np


from Matrix import Matrix 
import MethodesDeResolution as method




def sortie(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)

signal.signal(signal.SIGINT, sortie)

print(Fore.YELLOW + "\n################    RESOLUTION DE SYSTEME D'EQUATIONs    ##################\n" + Fore.RESET)

while(1):
    try:
        n = int(input("SVP, saisir le nombre de ligne et de colonnes : "))
        break
    except:
        print(Fore.RED + "erreur de saisie, saisir un enier" + Fore.RESET)
        continue

signal.signal(signal.SIGINT, sortie)

print("\nSaisir la matrice A :\n")
arrayA = []
arrayB = []
for i in range(n):
    while(1):
        try : 
            line = input(f"ligne-{i+1} (nombre separée par des espaces) EXP : 4 7 8 3 5 : ")
            arrayA.append([float(i) for i in line.split()])
            break
        except : 
            print(Fore.RED + "erreur de saisie, saisir à nouveau :)" + Fore.RESET)
            continue

# Creation de la Matrix A
m1 = Matrix(arrayA)

print("\nSaisir la matrice B (nombre separée par des espaces) EXP : 4 7 8 3 5 : ")
while(1):
    try:
        line = input(f" B : ")
        arrayB.append([float(i) for i in line.split()])
        break
    except:
        print(Fore.RED + "erreur de saisie, saisir à nouveau :)" + Fore.RESET)
        continue

# Creation de la Matrix B
m2 = Matrix(arrayB)
X0  = Matrix(n, 1, True)

"""
def JacobiSolve(A, b, Eps):
    import numpy as np
    n = len(b)
    x0, x = np.zeros((n, 1), 'float'), np.ones((n, 1), 'float')
    while np.linalg.norm(x-x0, np.inf) >= Eps:
        x0 = x.copy()
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if j != i:
                    x[i][0] -= A[i][j]*x0[j]
                x[i][0] /= A[i][i]
    return x"""
#m = Matrix.Matrix(6)

"""
m1 = Matrix.Matrix([[ 2, -1,  1], 
                    [-1, -1, -1],
                    [ 3,  3,  1]])
m2 = Matrix.Matrix([[16],
                    [5],
                    [9]])

matrice1 = Matrix.Matrix([[3, 5, 1], 
                          [1, 7, 3],
                          [2, 0, -1],])
matrice2 = Matrix.Matrix([[0],
                          [0],
                          [0],])
"""
"""
    elif(A.isInferior()):
        X[0][0] = B[0][0]/A[0][0]
        for i in range(1, n):
            sS = 0
"""
"""
m1 = Matrix([[0, 1, 2, 3, 4, 1, 0], 
                     [1, 0, 1, 2, 3, 1, 1],
                     [2, 1, 0, 1, 2, 1, 2],
                     [3, 2, 1, 0, 1, 1, 3],
                     [4, 3, 2, 1, 0, 1, 4],
                     [1, 1, 1, 1, 1, 0, 0],
                     [0, 1, 2, 3, 4, 0, 0]])

m2 = Matrix([[0],
                     [1],
                     [1],
                     [2],
                     [2],
                     [0],
                     [0]])
X0  = Matrix(m1.lines, 1, True)
"""


"""

matrice3 = Matrix.Matrix([[2,   -1,  -1], 
                          [0, -4, 2],
                          [6,   -3,  1],])

matrice2 = Matrix.Matrix([[16],
                          [5],
                          [9]])

"""

#matrice1.permuteLines(0, 3);matrice1.permuteLines(1, 2)
#matrice2.permuteLines(0, 3);matrice2.permuteLines(1, 2)

#print(matrice1)
#matrice1.mul_a_line_by_scalar(2, 8)

#matrice1.permuteLines(0, 1) 

#matrice1.sumLines(2, 3)

#matrice1.operationSurLigne(2, 3, -1)

#print(matrice1)
#print(matrice1)
#print(matrice2)
"""
m1 = Matrix([[4, 1, 1], 
                    [1, 4, 1],
                    [1, 1, 4]])
m2 = Matrix([[6],
                    [6],
                    [6]])
X0  = Matrix(m1.lines, 1, True)
"""
"""
m1 = deepcopy(ma1)
m2 = deepcopy(ma2)

# 
#method.triangulation(matrice1, matrice2)

#print(method.gaussJordan(matrice1, matrice2))

#print(method.croutDecomposition(matrice1))
#print(method.croutResolution(matrice1, matrice2))

#print(method.matriceAugmented(matrice1, matrice2))




 
#print(matrice2)
#C = method.doolittleResolution(matrice1, matrice2)

#X = method.choleskyResolution(matrice1, matrice2)

#print(X)
#print(C)
#print(m1*C)
#print(m2)
#
#print(matrice1)
#print(method.gauss(m1, m2))
#print(matrice1.transpose())
#print(matrice2.transpose())
#L, U, O = method.choleskyDecomposition(matrice1)
#C = method.croutResolution(ma1, ma2)
#print(method.gauss(m1, m2))
C = method.gaussSeidel(ma1, ma2, Matrix.Matrix([[0], [0], [0]]))
#C = method.gaussSeidel(ma1, ma2, Matrix.Matrix([[0], [0], [0], [0], [0], [0], [0]]))
#C = method.jacobiLUD(ma1, ma2, Matrix.Matrix([[0], [0], [0]]))
#C = JacobiSolve(np.array(ma1.datas), np.array(ma2.datas), 10e-1)
#print(L, U)
#print(ma1)
#print(ma2)
#method.choix_pivot(ma1, 0, ma2)
#print(ma1)
#print(ma2)
#print(method.gaussSeidel(m1, m2, Matrix.Matrix([[0], [0], [0]])))
print(C)
#print(m1*C)
#print(m2)
#print(m1*X)
"""
"""

print(matrice1)

print(matrice2)
""
Sm = matrice1 - matrice2

#print(Sm)
#print(matrice1.__dir__()[7])
print(Sm)

matrice3 = Matrix.mulByScalar(matrice1, 2)

matrice4 = Matrix.Matrix(3, 2, False)
mc = matrice1*matrice4

print((matrice1.lines, matrice1.colones), (matrice2.lines, matrice2.colones))
print(mc)

#matrice4 = Matrix
print(-matrice3)

"""
"""

m1 = Matrix.Matrix([[1, 2, 3], 
                    [4, 5, 6],
                    [7, 8, 9]])

method.triangulation(m1, Matrix.Matrix([[0] for i in range(3)]))
print(m1)
print(method.rang(m1))
"""
#print(np.linalg.matrix_rank(matrice1))

#print(method.rang(matrice1))
print("\n<<<<<<<<<< MATRICE A >>>>>>>>>>\n", m1)
print("\n<<<<<<<<<< MATRICE B >>>>>>>>>>\n", m2)

try:
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE GAUSS    #####################\n" + Fore.RESET)
    print(method.gauss(A, B))
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE GAUSS-JORDAN    #####################\n" + Fore.RESET)
    print(method.gaussJordan(A, B))
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE CROUT    #####################\n" + Fore.RESET)
    print(method.croutResolution(A, B))
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE DOOLITTLE    #####################\n" + Fore.RESET)
    print(method.doolittleResolution(A, B))
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE CHOLESKY    #####################\n" + Fore.RESET)
    #print(A.transpose())
    #print(A)
    if (method.choleskyDecomposition(A, B) == None) : pass
    else : print(method.choleskyResolution(A, B))
except ValueError: print(Fore.RED + "Matrice non definie positive ou Non symétrique" + Fore.RESET)

try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE JACOBI    #####################\n" + Fore.RESET)
    print(method.jacobi(A, B, X0))
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    if(not A.isDiagonalDominante()): raise ValueError("La matrice n'est pas diagonale dominante, donc la méthode peut être diverger")
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE GAUSS-SEIDEL    #####################\n" + Fore.RESET)
    print(method.gaussSeidel(A, B, X0))
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

 