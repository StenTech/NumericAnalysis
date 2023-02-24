import numpy as np
import matplotlib.pyplot as plt
import MethodeInterpolation as mtd
from Polynome import Polynome

#lstPoint = [(0, 1), (1, 2), (2, 9), (3, 28)]
#lstPoint = [(2, 1), (3, -1), (-1, 2), (4, 3)]
#lstPoint = [(1, 2), (3, 7), (4, -1)]
#lstPoint = [(2, 1), (0, -1), (5, 10), (3, -4)]
#print(tuple("2, 9".split(", ")))
lstPoint = []



point = ""
print("\nPour quitter la boucle de saisie entrer : 0\nPour Quitter saisir : << exit >> ")
while point != "0":
    try :
        point = input("SVP, veuillez saisir un point de collocation (NB sous la forme >>> xi f(xi) ) :  ")
        if(point.lower() == "exit") : break
        lstPoint.append(tuple([float(coord) for coord in point.split()]))
    except : print("\nMauvaise saisi, SVP Resaisir")
    pass
else :
    # Affichage de la liste des points
    lstPoint = lstPoint[:-1]
    print("\nla liste de point est : \n", lstPoint)

    print("\n###############    MATRICE DE VANDERMONDE   #############\n")
    print(mtd.matriceVandermonde(lstPoint))

    print("\n###############    INTERPOLATION AU SENS DE LAGRANGE   #############\n")
    P = mtd.polynomeLagrange(lstPoint)
    print(P)

    print("\n###############    INTERPOLATION AU SENS DE NEWTONE   #############\n")
    print(mtd.polynomeNewtone(lstPoint))

    print("\n###############    INTERPOLATION AU SENS DES MOINDES CARRÉES   #############\n")
    P = mtd.interpolationMoindresCarre(lstPoint)
    print(mtd.interpolationMoindresCarre(lstPoint))

    #Xmin = int(input("SVP, Veuillez entrer Xmin"))
    Xmax = int(input("SVP, Veuillez entrer Xmax : "))

    
    # Liste de 1000 point entre -Xmax et Xman
    X = np.linspace(-Xmax, Xmax, 1000)

    Y = 0

    # evaluation du polynome pour tous les point de X
    for i in range(P.degree, -1, -1):
        Y = Y*X + P[i]


    """
    f = fr'\$f(x) = {P[0]} + {P[1]}*x'
    for i in range(2, P.degree+1): f+= fr'{P[i]}*x^{i}'
    f+=fr'$'"""


    #Affichage des points
    plt.scatter([el[0] for el in lstPoint], [el[1] for el in lstPoint])
    
    # Dessing de la courbe
    plt.plot(X, Y)
    plt.title("Plot The interpolation Polynome.")
    plt.show()