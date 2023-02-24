from copy import deepcopy
from math import sqrt
from re import M
from Matrix import Matrix

def matriceAugmented(A:Matrix, B:Matrix)->Matrix: 
    aM = Matrix([A[i]+B[i] for i in range(A.lines)]) #Matrice augmentée
    return aM

def matriceDetached(AM: Matrix)->Matrix:
    A = Matrix([l[:-1] for l in AM])
    B = Matrix([[l[-1]] for l in AM])
    return [A, B]

def rang(A: Matrix) -> int :
    #B = Matrix([[0] for i in range(A.lines)])
    triangulation(A)
    r = A.lines -  A.datas.count([0]*A.colones)
    
    return r

def choix_pivot(M: Matrix, i: int, N: Matrix = None):
    """Permet de choisir un pivot, et de permuter convenablement les lignes.
    retourner le numero de ligne convenable pour le pivot
    """
    #O = []
    k = i+1
    if(M[i][i] == 0) :
        
        while(k < M.lines and M[k][i] == 0) : k+=1
        
        if(k == M.lines) : pass
        else : M.permuteLines(i, k) 

        if(isinstance(N, Matrix)) :
            if(k == M.lines) : pass
            elif(k < M.lines) : N.permuteLines(i, k)
            
        return M[i][i]
    
    return M[i][i]

def elemntaryOperationLi(M: Matrix, i, j):
    for k in range(M.colones):
        M[i][k] -= (M[i][k]/M[j][j])*M[j][k]

def triangulation(A: Matrix, B: Matrix = Matrix([[0]])):

    n = A.lines

    # Configurer le cas où la matrice B n'a pas éte fournie
    if(B.datas == [[0]]): B = Matrix([[0] for i in range(n)])

    pivot = choix_pivot(A, 0, B)
    """""
    # NB : ça fonctionne  :::::::::::::::
    for k in range(n-1):
        for i in range(k+1, n):
            c = A[i][k]/A[k][k]
            B[i][0] -= c*B[k][0] 
            A[i][k] = 0
            for j in range(k+1, n):
                A[i][j]-= c*A[k][j]"""

    #aM = Matrix([A[i]+B[i] for i in range(A.lines)]) #Matrice augmentée

    for j in range(1, n):

        for i in range(j, n):
            a = A[i][j-1]/pivot
            #print("a = ", a)
            A.operationSurLigne(i, j-1, -a)
            B.operationSurLigne(i, j-1, -a)
            #print("Etapes : ", A)


        pivot = choix_pivot(A, j, B)
        #print(A)
    # return [A, B]
    
    #detachement = matriceDetached(aM)
    #A = detachement[0]
    #B = detachement[1]

    #return aM


def gauss(A:Matrix, B:Matrix) -> Matrix:
    n = A.lines
    
    X = Matrix(n, 1, True)
    triangulation(A, B)

    X[n-1][0] = B[n-1][0]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sS = 0
        for j in range(i, n):
            sS += A[i][j]*X[j][0]

        X[i][0] = (B[i][0] - sS)/A[i][i]

    return X

    
"""
    if(A.isDiagonal()) : 
        for i in range(n):
            X[i][0] = B[i][0]/A[i][i]
        return X

    elif(A.isSuperior()):
 
    elif(A.isInferior()):
        X[0][0] = B[0][0]/A[0][0]
        for i in range(1, n):
            sS = 0
            for j in range(0, i):
                sS += A[i][j]*X[j][0]

            X[i][0] = (B[i][0] - sS)/A[i][i]
            
        return X

    
    #aM = Matrix([A[i]+B[i] for i in range(A.lines)]) #Matrice augmentée
"""   
            
    
def gaussJordan(A:Matrix, B:Matrix) -> Matrix:

    n = A.lines
    aM = matriceAugmented(A, B)
    #print(aM)

    for j in range(n):
        pivot = choix_pivot(aM, j)
        aM.mul_a_line_by_scalar(j, 1/pivot)
        for i in range(n):
            if j!=i : 
                aM.operationSurLigne(i, j, -aM[i][j])

    return Matrix([[el[-1]] for el in aM])


def croutDecomposition(A: Matrix, B: Matrix):

    n = A.lines
    """Effeectue une decomposition de crout sur la matrice A"""
    L  = Matrix(n, False)
    U = Matrix(n, True)
    #O = []
    
    choix_pivot(A, 0, B)
            
    for i in range(n):
        L[i][0] = A[i][0]#;print(L, U)

    for i in range(1, n):
        U[0][i] = A[0][i]/L[0][0]
        

    for i in range(1, n-1):
        L[i][i] = A[i][i]
        for k in range(i): L[i][i] -= L[i][k]*U[k][i]

        for j in range(i+1, n):
            L[j][i] = A[j][i] 
            U[i][j] = A[i][j]
            for k in range(i): 
                L[j][i] -= L[j][k]*U[k][i]
                U[i][j] -= L[i][k]*U[k][j]


            #Lii = choix_pivot(A, i, B)
            
            U[i][j] /= L[i][i]

    
    L[n-1][n-1] = A[n-1][n-1]
    for k in range(n-1):L[n-1][n-1] -= L[n-1][k]*U[k][n-1]
    #print(L, U)

    return L, U

def choleskyDecomposition(A: Matrix, B: Matrix):

    if(A.transpose().datas != A.datas ):
        print("Matrice non symetrique, Impossible avec Cholesky")
        return None

    n = A.lines
    """Effeectue une decomposition de crout sur la matrice A"""
    L = Matrix(n, False)
    U = Matrix(n, False)
    #O = []


    A00 = choix_pivot(A, 0, B)
            
    L[0][0] = sqrt(A00)

    for i in range(1, n):
        L[i][0] = A[i][0]/L[0][0]
        

    for j in range(1, n):
        Ajj = choix_pivot(A, j, B)
        L[j][j] = Ajj
        for k in range(j): L[j][j] -= L[j][k]**2
        L[j][j] = sqrt(L[j][j])

        for i in range(j+1, n):
            L[i][j] = A[i][j] 
            for k in range(j): 
                L[i][j] -= L[i][k]*L[j][k]


            Ljj = choix_pivot(A, j, B)
            
            L[i][j] /= L[j][j]

    U = L.transpose()
    
    #L[n-1][n-1] = A[n-1][n-1]
    #for k in range(n-1):L[n-1][n-1] -= L[n-1][k]*U[k][n-1]
    #print(L, U)

    return L, U

def doolittleDecomposition(A: Matrix, B: Matrix):
    n = A.lines
    L = Matrix(n, False)
    U = Matrix(n, False)
    #O = []
    
    A00 = choix_pivot(A, 0, B)
    for i in range(n):
        for j in range(n):
            U[i][j] = A[i][j]  #U is the same as a but without answers (a --> augmented matrix,  U --> not augmented)
            if i == j:
                L[i][j] = 1  #diagonals = 1
            else:
                L[i][j] = 0

    # Forward Elimination
    for i in range(n):
        for j in range(i + 1, n):
            ratio = U[j][i] / U[i][i]
            L[j][i] = ratio  #lower triangular matrix containing ratios

            for k in range(n):  #eliminate (to construct an upper triangular matrix)
                U[j][k] = U[j][k] - ratio * U[i][k]

    return L, U

def thomasDecomposition(A: Matrix, B: Matrix):
    n = A.lines
    L = Matrix(n, False)
    U = Matrix(n, False)
    
    U[0][0] = A[0][0]

    for i in range(n-1): U[i][i+1] = A[i][i+1]

    for i in range(n):
        L[i][i] = 1
        if(i >= 1): 
            L[i][i-1] = A[i][i-1]/U[i-1][i-1]
            U[i][i] = A[i][i] - L[i][i-1]*A[i-1][i]

    return L, U


def LUResolution(L: Matrix, U: Matrix, B: Matrix, n: int):

    Y = Matrix(n, 1, True)
    X = Matrix(n, 1, True)
    #O = []
    #for i, j in O: B.permuteLines(i, j)
    
    Y[0][0] = B[0][0]/L[0][0]
    for i in range(1, n):
        sS = 0
        for j in range(0, i):
            sS += L[i][j]*Y[j][0]

        Y[i][0] = (B[i][0] - sS)/L[i][i]
            
    #triangulation(A, B)

    X[n-1][0] = Y[n-1][0]/U[n-1][n-1]
    for i in range(n-2, -1, -1):
        sS = 0
        for j in range(i, n):
            sS += U[i][j]*X[j][0]

        X[i][0] = (Y[i][0] - sS)/U[i][i]
            #print(X[i][0])
    #return [round(el[0]) for el in X]
    return X


def doolittleResolution(A: Matrix, B: Matrix):
    n = A.lines
    L, U = doolittleDecomposition(A, B)
    return LUResolution(L, U, B, n)

def croutResolution(A: Matrix, B: Matrix):
    n = A.lines
    L, U = croutDecomposition(A, B)
    return LUResolution(L, U, B, n)

def choleskyResolution(A: Matrix, B: Matrix):
    n = A.lines
    L, U = choleskyDecomposition(A, B)
    return LUResolution(L, U, B, n)

def thomasResolution(A: Matrix, B: Matrix):
    n = A.lines
    Y = Matrix(n, 1, True)
    X = Matrix(n, 1, True)

    L, U = thomasDecomposition(A, B)

    Y[0][0] = B[0][0]

    for i in range(1, n): 
        Y[i][0] = B[i][0] - L[i][i-1]*Y[i-1][0]

    X[n-1][0] = Y[n-1][0]/U[n-1][n-1]

    for i in range(n-2, -1, -1): 
        X[i][0] = (Y[i][0] - U[i][i+1]*X[i+1][0])/U[i][i]

    return X




def convergence(X: Matrix, A: Matrix, B: Matrix, epsilon: float = 0.0000000001) -> bool:
    if(all([abs(i[0])< epsilon for i in (B - A*X).datas])) : 
        return True
    return False

def jacobi(A: Matrix, B: Matrix, X0: Matrix):
    n = A.lines
    X = X0
    k = 1000
    #m = k
    A1 = deepcopy(A);B1 = deepcopy(B)
    try : 
        while(not convergence(X, A, B) and k>=0):
            for i in range(n):
                X[i][0] = B[i][0]
                for j in range(n):
                    if j!=i : X[i][0]-= A[i][j]*X[j][0]

                Aii = choix_pivot(A, i, B)

                X[i][0] /= Aii
            k-=1
        else :
            if(k == -1) : print("Nombre maximum d'itération atteinte. Donc divergence Assurée"); return None
            #else : print(f"\nSolution Trouvée en: {m-k} intérations\n")
        return X
    except ZeroDivisionError :
        triangulation(A1, B1)
        return jacobi(A1, B1, X)
    except RecursionError :
        print("Impossibililté de resolution.")
        return None        

def gaussSeidel(A: Matrix, B: Matrix, X0: Matrix):
    n = A.lines
    X = X0
    k = 1000
    #m = k
    #A1 = deepcopy(A);B1 = deepcopy(B)
    try : 
        while(not convergence(X, A, B) and k>=0):
            for i in range(n):
                X[i][0] = B[i][0]
                for j in range(n):
                    if j<i : X[i][0]-= A[i][j]*X[j][0]
                    if j>i : X[i][0]-= A[i][j]*X[j][0]
                    #X[i][0]-= A[i][j]*X[j][0]
                    #X[i][0] -= A[i][j]*X[j][0]
                #for j in range(i, n):

                Aii = choix_pivot(A, i, B)
                X[i][0] /= Aii
            k-=1
        else :
            if(k == -1) : print("Nombre maximum d'itération atteinte. Donc divergence Assurée"); return None
            #else : print(f"\nSolution Trouvée en: {m-k} intérations\n")
        return X

    except ZeroDivisionError :
        print("La méthode rencontre une division par zéro, ")
        #triangulation(A1, B1)
        #return gaussSeidel(A1, B1, X)
    except RecursionError :
        print("Impossibililté de resolution.")
        return None


"""
if __name__ == "__main__" :
    m1 = Matrix([[ 2, -1,  0], 
                 [-1, -1, -1],
                 [ 0,  3,  1]])
    m2 = Matrix([[16],
                 [5],
                 [9]])

    ma1 = deepcopy(m1)
    ma2 = deepcopy(m2)

    print(gauss(ma1, ma2))
    ma1 = deepcopy(m1)
    ma2 = deepcopy(m2)

    print(croutResolution(ma1, ma2))

    ma1 = deepcopy(m1)
    ma2 = deepcopy(m2)

    L, U = thomasDecomposition(ma1, ma2)

    #print(L, U)

    #print(L*U)

    print(thomasResolution(ma1, ma2))
"""

if __name__ == "__main__" :
    m = Matrix([[0, -1, 3],
                [1, 1, -1],
                [1, -1, 5]])

    print(rang(m))