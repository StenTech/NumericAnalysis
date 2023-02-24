from typing import List, Tuple
from Matrix import Matrix
import MethodesDeResolution2 as mtd
from Polynome import Polynome


def matriceVandermonde(listPoint : List[Tuple])  ->Polynome:
    n = len(listPoint)
    arrayInterpo = [[el[0]**i for i in range(n)] for el in listPoint]
    Xi = Matrix(arrayInterpo)
    fXi = [[el[1]] for el in listPoint]
    A = mtd.croutResolution(Xi, fXi)
    return Polynome([el[0] for el in A.datas])


def polynomeLagrange(listPoint : List[Tuple]) -> Polynome:
    n = len(listPoint) - 1
    P = Polynome(n, 0)
    X = [el[0] for el in listPoint]
    fX = [el[1] for el in listPoint]
    for i in range(n+1):
        Oi = Polynome(0, 1)
        for j in range(n+1):
            if(j != i): Oi *= Polynome([-X[j]/(X[i]-X[j]), 1/(X[i]-X[j])])

        P += fX[i]*Oi
                
    return P

def k_emeDifferenceDivisee(listPoint : List[Tuple]) -> float:
    """Calcule la k-ième difference divisee des points dans lstPoint"""
    l = listPoint[:]
    n = len(listPoint)
    if (n == 1) : return listPoint[0][1]
    else: 
        return ((k_emeDifferenceDivisee(l[1:]) - k_emeDifferenceDivisee(l[:-1]))
                /(l[-1][0] - l[0][0]))

def polynomeNewtone(listPoint : List[Tuple]) -> Polynome : 
    n = len(listPoint)
    A = [0]*n
    for i in range(n):
        #print()
        A[i] = k_emeDifferenceDivisee(listPoint[:i+1])
    #print(A)
    P = Polynome(n-1, 0)
    P[0] = A[0]
    for i in range(1, n):
        X = Polynome([A[i]])
        for j in range(i):
            X *= Polynome([-listPoint[j][0], 1])
        P += X
    return P

def interpolationMoindresCarre(listPoint: List[Tuple], n: int) -> Polynome :
    #n = len(listPoint)
    p = n-1
    #P = Matrix([[0]*n]*n)
    P = Matrix(n, False) #[[0 for i in range(n)] for j in range(n)]
    B = Matrix(n, 1, True)
    for i in range(n):
        for j in range(n):
            c = 0
            for k in range(n):
                c += (listPoint[k][0])**(2*p-j-i)
            #if(i <= j) : 
            P[i][j] = c
            P[j][i] = c
    
    for i in range(n):
        c = 0
        for k in range(n):
            c += (listPoint[k][0]**(p-i))*listPoint[k][1]
        B[i][0] = c

    #print(P);print(B)
    #print("P = ", P)
    
    A = mtd.choleskyResolution(P, B)
    A = Polynome([el[0] for el in A[::-1]])
    return A #None
    


#if __name__ == "__main__" :
    #print(interpolationMoindresCarre([(-3, -28), (-2, -9), (-1, -2), (0, -1), (1, 0), (2, 7), (3, 26)]))