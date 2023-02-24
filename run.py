from signal import signal, SIGINT
from time import sleep
from colorama import Fore, Style, Back

from MethodeInterpolation import *
from MethodesDeResolution import *
from MethodesDeResolution2 import *
from Deriv_Integr_Numerik import *
from Polynome import Polynome
from Matrix import Matrix

def sortie(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)

def menu():
    print(Style.BRIGHT + Fore.CYAN + "\t\t\###### MENU ######\n\n\
            1.  Resolution Equation non linéaire.\n\
            2.  Resolution Sysytème d'équation.\n\
            3.  Interpolation Polynomial.\n\
            4.  Equation différentille.")


#signal(SIGINT, sortie)
"""
print(Style.BRIGHT + Fore.CYAN + "\n\n\t\t\t\t  #######BIENVENUE DANS NOTRE APPLICATION D' ANALYSE NUMERIQUE#####  \n\n" + Fore.RESET + Style.RESET_ALL)
print(Fore.YELLOW + "\n################    RESOLUTION D'EQUATIONS NON LINEAIRE   ##################\n" + Fore.RESET)
print()
sol_a = list()
sol_b = list()
sol_c = list()
sol_d = list()
sol_interv = list()
       
f = None
g = None

while(1):
    try :
        function_str_1 = input("Svp saisir la fonction f (La variable est x) : ")
        function_str_2 = input("Svp saisir la fonction g (La variable est x)(Point_Fixe) : ")
        exec(f"f = lambda x : {function_str_1}")
        exec(f"g = lambda x : {function_str_2}")
    except SyntaxError:
        print("Erreur de syntaxe, autrement de saisie.")
    except TypeError:
        print("Erreur de syntaxe, autrement de saisie.")
    except KeyboardInterrupt : 
        print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
        print()
        exit(0)
    else : break
                
        
while(1):
    try :
        x0 = float(input("SVP Veuillez saisir x0 (Pour la méthode du point fixe ou newton)  : "))
        x1 = float(input("SVP Veuillez saisir X1 (Pour la méthode de bissection ou sécante) : "))
        x2 = float(input("SVP veuillez saisir X2 (Pour la méthode de bissection ou sécante) : "))
        EPSILON  = float(input("SVP veillez saisir EPSILON : "))        

        # Structure de controle de la valeur de x1 et x2
        if(x1 == x2) :
            if(f(x1) == 0 or f(x1) < EPSILON) : 
                print(Fore.CYAN)
                print(f"\nX1 = x2, et f({x1} = 0), donc la solution est {x1}.\n"); sol_a.append(x1); print(Fore.RESET)
                break
            else : raise ValueError(Fore.RED +"Mauvais chois de l'intervalle car x1 = x2"+Fore.RESET); continue
        elif(x1 > x2):
            print(Fore.RED+" borne inférieur > borne supérieur, SVP veuillez resaisir :" + Fore.RESET)
            raise ValueError(Fore.RED + "Mauvais chois de l'intervalle car x1 > x2" + Fore.RESET); continue

    except SyntaxError : continue
    except TypeError : print(Fore.RED + "x1 ou x2 mal siasi, veuillerz resaisir" + Fore.RESET); continue
    except KeyboardInterrupt : 
        print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
        print()
        exit(0)
    except : print(Fore.RED + "Mauvais chois de l'intervalle, resisir"+ Fore.RESET);continue
            
    else: 
        sol_interv = balyage(f, x1, x2)
        if sol_interv == []:
            print("\nPas de solution Apparente Après balayage dans l'intervalle fourni.\n")
        else : print(" Intervalles obtenue après balayage. "+Fore.LIGHTMAGENTA_EX,sol_interv, Fore.RESET)
        break

try :
        for bornes in sol_interv :
            sol_a.append(dichotomie(f, bornes[0], bornes[1], EPSILON))
            sol_b.append(secante(f, bornes[0], bornes[1], EPSILON))
            

        print("\n##METHODE BISSECTION##\n")
        #print(dichotomie(f, x1, x2, EPSILON))
        #if sol_interv == []: print("Pas de solution apparente.")
        print(f"\nf(x) = {function_str_1}\n\nFor alpa in {sol_a}, f(alpha) = 0 .")
            
        print("\n##METHODE NEWTON##\n")
        sol_c.append(newton(f, x0, EPSILON))
        print(f"\nf(x) = {function_str_1}\n\nFor alpa in {sol_c}, f(alpha) = 0 .")
            
        print("\n##METHODE SECANTE##\n")
        #print(secante(f, x1, x2, EPSILON))
        #if sol_interv == []: print("Pas de solution apparente.")
        print(f"\nf(x) = {function_str_1}\n\nFor alpa in {sol_b}, f(alpha) = 0 .")

        
        
        #if sol_interv == []: print("Pas de solution apparente.")
        
    
        if 1 :
            for bornes in sol_interv :
                isContractant = isContract(g, bornes[0], bornes[1])
                if(not isContractant):
                    print("g est non contractante, veuillez re-saisir les données correctes")
                    while(not isContractant):
                        function_str_2 = input("Svp saisir la fonction g (La variable est x)(Point_Fixe) : ")
                        exec(f"g = lambda x : {function_str_2}")
                        isContractant = isContract(g, bornes[0], bornes[1])
                    else:
                        sol_d.append(point_fixe(g, bornes[0], EPSILON))
                        #print(sol_d)
                else:
                    sol_d.append(point_fixe(g, bornes[0], EPSILON))
                    #print(sol_d)
            
        print(Fore.YELLOW + "\n##METHODE DU POINT FIXE##\n" + Fore.RESET)
        
    
        sol_d.append(point_fixe(g, x0, EPSILON))
        print(f"\ng(x) = {function_str_2}\n")

        print(f"\nf(x) = {function_str_1}\n\nFor alpa in {sol_d}, f(alpha) = 0 .")
            
except ZeroDivisionError:
        print(Fore.RED+"\nESSAI DE DIVISION PAR ZERO 0.\n"+Fore.RESET)
except KeyboardInterrupt : 
    print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
    print()
    exit(0)
except ValueError:
        print("\nVALEURS DE X HORS DU DOMAINE DE DEFINITION OU MAUVAISE SAISIE.\n")


#######
print(Fore.BLUE+Style.DIM+"\n\nSVP patientez 5s pour la suite ..."+Fore.RESET + Style.RESET_ALL)
sleep(5)
########


print(Fore.YELLOW + "\n################    RESOLUTION DE SYSTEME D'EQUATIONs    ##################\n" + Fore.RESET)

while(1):
    try:
        n = int(input("SVP, saisir le nombre de ligne et de colonnes : "))
        if n < 1 : raise ValueError(" n < 1, Resaisir"); continue
        break
    except KeyboardInterrupt : 
        print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
        print()
        exit(0)
    except :
        print(Fore.RED + "erreur de saisie, saisir un enier" + Fore.RESET)
        continue

print("\nSaisir la matrice A :\n")
arrayA = []
arrayB = []
for i in range(n):
    while(1):
        try : 
            line = input(f"ligne-{i+1} (nombre separée par des espaces) EXP : 4 7 8 3 5 : ")
            if(len(line.split()) != n) :
                print(Fore.RED + "SVP, respecter les dimensions, Veuillez resaisir" + Fore.RESET)
                continue
            arrayA.append([float(i) for i in line.split()])
            break
        except KeyboardInterrupt : 
            print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
            print()
            exit(0)
        except : 
            print(Fore.RED + "erreur de saisie, saisir à nouveau :)" + Fore.RESET)
            continue

# Creation de la Matrix A
m1 = Matrix(arrayA)

while(1):
    try:
        print()
        line = input(f"Saisir la matrice B (nombre separée par des espaces) EXP : 4 7 8 3 5 : ")
        if(len(line.split()) != n) :
            print(Fore.RED + "SVP, respecter les dimensions, Veuillez resaisir" + Fore.RESET)
            continue
        arrayB = [[float(i)] for i in line.split()]
        break
    except KeyboardInterrupt : 
        print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
        print()
        exit(0)
    except:
        print(Fore.RED + "erreur de saisie, saisir à nouveau :)" + Fore.RESET)
        continue

# Creation de la Matrix B
m2 = Matrix(arrayB)
X0  = Matrix(n, 1, True)

print("\n<<<<<<<<<< MATRICE A >>>>>>>>>>\n", m1)
print("\n<<<<<<<<<< MATRICE B >>>>>>>>>>\n", m2)

try:
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE GAUSS    #####################\n" + Fore.RESET)
    print(gauss(A, B))
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE GAUSS-JORDAN    #####################\n" + Fore.RESET)
    print(gaussJordan(A, B))
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE CROUT    #####################\n" + Fore.RESET)
    print(croutResolution(A, B))
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE DOOLITTLE    #####################\n" + Fore.RESET)
    print(doolittleResolution(A, B))
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE THOMAS    #####################\n" + Fore.RESET)
    if (A.isTriDiagonal()) : print(thomasResolution(A, B))
    else : print(Fore.RED + "Impossible d'appliquer l' Algorithme de thomas" + Fore.LIGHTMAGENTA_EX + " car A n'est pas tridiagonal" + Fore.RESET)
except ValueError: print(Fore.RED + "Erreur Survenue" + Fore.RESET)
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)


try  :
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(Fore.YELLOW + "\n#################    METHODE CHOLESKY    #####################\n" + Fore.RESET)
    #print(A.transpose())
    #print(A)
    #print((A.transpose()))
    if (choleskyDecomposition(A, B) == None) : pass
    else : print(choleskyResolution(A, B))
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)
except ValueError: print(Fore.RED + "Matrice non definie positive ou Non symétrique" + Fore.RESET)

try  :
    print(Fore.YELLOW + "\n#################    METHODE JACOBI    #####################\n" + Fore.RESET)
    #if(not A.isDiagonalDominante()): print("Matrice à Diagonal Non Dominante, Mais peut toute fois converger.")
    #else : print("Matrice à Diagonal dominate donc Comvergence Assuréé.")
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(jacobi(A, B, X0))
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)

try  :
    print(Fore.YELLOW + "\n#################    METHODE GAUSS-SEIDEL    #####################\n" + Fore.RESET)
    #if(not A.isDiagonalDominante()): print("Matrice à Diagonal Non Dominante, Mais peut toute fois converger.")
    #else : print("Matrice à Diagonal dominate donc Comvergence Assuréé.")
    A = deepcopy(m1)
    B = deepcopy(m2)
    print(gaussSeidel(A, B, X0))
except ZeroDivisionError : print(Fore.RED + "Présence d'un pivot = 0" + Fore.RESET)
except : print(Fore.RED + "Une erreur survenue ou Impossiblilité de resolution du Système avec cette méthode." + Fore.RESET)



#######

print(Fore.BLUE+Style.DIM+"\n\nSVP patientez 5s pour la suite ..."+Fore.RESET + Style.RESET_ALL)
sleep(5)

##########

"""
print(Fore.YELLOW + "\n################    INTERPOLATION POLYNOMIALE    ##################\n\n" + Fore.RESET)
import matplotlib.pyplot as plt
import numpy as np


lstPoint = []


point = ""


while 1 :
    try : 
        nbPoint = int(input("SVP, Saisir le nombre de point : "))
    except KeyboardInterrupt : 
            print("\n"+Back.WHITE+Fore.BLACK+"SORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
            print()
            exit(0)
    except TypeError :
        print(Fore.RED+"Saisie  Incorrecte,  Resaisir"+Fore.RESET);continue
    except ValueError :
        print(Fore.RED+"Saisie  Incorrecte,  Resaisir"+Fore.RESET);continue
    except :
        print(Fore.RED+"Saisie  Incorrecte,  Resaisir"+Fore.RESET);continue
    else: break

P = Polynome(nbPoint, 0)
Q = Polynome(nbPoint, 0)
R = Polynome(nbPoint, 0)
#S = Polynome(nbPoint, 0)

for i in range(nbPoint):
    while 1 :
        try :
            point = input(f"SVP, veuillez saisir point de collocation Numero-{i+1}(NB sous la forme >>> xi f(xi) ) :  ")
            if(len(point.split()) != 2) :
                print(Fore.RED + "SVP, respecter la notation [xi f(xi)] , Veuillez resaisir" + Fore.RESET)
                continue
            point = point.split()
            point[1] = eval(point[1])
            lstPoint.append(tuple([float(coord) for coord in point]))
        except KeyboardInterrupt : 
            print("\n"+Back.WHITE+Fore.BLACK+"SORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
            print()
            exit(0)
        except : print("\nMauvaise saisi, SVP Resaisir"); continue
        else : break
else :
    # Affichage de la liste des points
    print("\nla liste de point est : \n", lstPoint)

    print(Fore.YELLOW + "\n###############    MATRICE DE VANDERMONDE   #############\n"+Fore.RESET)
    P = matriceVandermonde(lstPoint)
    print(P)

    print(Fore.YELLOW+"\n###############    INTERPOLATION AU SENS DE LAGRANGE   #############\n"+Fore.RESET)
    Q = polynomeLagrange(lstPoint)
    print(Q)

    print(Fore.YELLOW + "\n###############    INTERPOLATION AU SENS DE NEWTONE   #############\n" + Fore.RESET)
    R = polynomeNewtone(lstPoint)
    print(R)

    print(Fore.YELLOW+"\n###############    INTERPOLATION AU SENS DES MOINDES CARRÉES   #############\n" + Fore.RESET)
    while 1 :
        try : 
            n = int(input("SVP, Saisir le degré Du polynome à  votre choix : "))
        except KeyboardInterrupt : 
                print("\n"+Back.WHITE+Fore.BLACK+"SORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
                print()
                exit(0)
        except TypeError :
            print(Fore.RED+"Saisie  Incorrecte,  Resaisir"+Fore.RESET);continue
        except ValueError :
            print(Fore.RED+"Saisie  Incorrecte,  Resaisir"+Fore.RESET);continue
        except :
            print(Fore.RED+"Saisie  Incorrecte,  Resaisir"+Fore.RESET);continue
        else: 
            n+=1
            break

    S = Polynome(n-1, 0) # car a la ligne 342, on a fait n +=1;
    S = interpolationMoindresCarre(lstPoint, n)
    print(S)

    # Saisie  de la fonction
    f = None
    while(1):
        try :
            function_str_1 = input("Svp saisir la fonction f (La variable est x) : ")
            exec(f"f = lambda x : {function_str_1}")
        except SyntaxError:
            print("Erreur de syntaxe, autrement de saisie.")
        except TypeError:
            print("Erreur de syntaxe, autrement de saisie.")
        except KeyboardInterrupt : 
            print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
            print()
            exit(0)
        else : break

    #Xmin = int(input("SVP, Veuillez entrer Xmin"))
    Xmax = int(input("SVP, Veuillez entrer Xmax : "))

    
    # Liste de 1000 point entre -Xmax et Xman
    X = np.linspace(-Xmax, Xmax, 10000)

    Yp = 0
    Yq = 0
    Yr = 0
    Ys = 0


    # evaluation du polynome pour tous les point de X schema de Horner-Ruffoni
    for i in range(P.degree, -1, -1):
        Yp = Yp*X + P[i]

    for i in range(Q.degree, -1, -1):
        Yq = Yq*X + Q[i]

    for i in range(R.degree, -1, -1):
        Yr = Yr*X + R[i]

    for i in range(S.degree, -1, -1):
        Ys = Ys*X + S[i]

    # Calcul de f(x)
    Y  = []
    for x in X:
        Y.append(f(x))

    #Affichage des points
    plt.scatter([el[0] for el in lstPoint], [el[1] for el in lstPoint], color = "orange")
    

    # Dessing de la courbe
    plt.plot(X, Yp, color = "red", label = "vandermonde")
    plt.plot(X, Yq, color = "blue", label = "Lagrange")
    plt.plot(X, Yr, color = "green", label = "newtone")
    plt.plot(X, Ys, color = "yellow", label = "MoindresCarrés")
    plt.plot(X, Y, color = "black", label = "Cf")

    ax = plt.gca() 
    ax.spines['top'].set_color('none') 
    ax.spines['left'].set_position('zero') 
    ax.spines['right'].set_color('none') 
    ax.spines['bottom'].set_position('zero') 
  
    plt.xlim(-Xmax, Xmax) 
    plt.grid(True)
    plt.legend()
    plt.title("Plot The interpolation Polynomes.")
    plt.show()

"""
###########
print(Fore.BLUE+Style.DIM+"\n\nSVP patientez 5s pour la suite ..."+Fore.RESET + Style.RESET_ALL)
sleep(5)
##########

print(Fore.YELLOW + "\n################    INTERPOLATION POLYNOMIALE    ##################\n\n" + Fore.RESET)

while(1):
    try :
        function_str = input("Svp saissez f(t, y) : dans l'equa-diff [y' = f(t, y)] :\n\n\t f(t, y)] = ")
        f = None
        exec(f"f = lambda t, y : {function_str}")
    except SyntaxError:
        print("Erreur de syntaxe, autrement de saisie.")
    except TypeError:
        print("Erreur de syntaxe, autrement de saisie.")
    except KeyboardInterrupt : 
        print("\n"+Back.WHITE+Fore.BLACK+"\nSORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
        print()
        exit(0)
    else : break

t0, y0 = 0, 0
a, b = 0, 0
if 1:
    while 1 :
        try :
            point0 = input(f" Saisir la point de depart (NB sous la forme >>> t0 y0 ) :  ")
            if(len(point0.split()) != 2) :
                print(Fore.RED + "SVP, respecter la notation [t0 y0] , Veuillez resaisir" + Fore.RESET)
                continue
            t0, y0 = tuple([float(coord) for coord in point0.split()])
        except KeyboardInterrupt : 
            print("\n"+Back.WHITE+Fore.BLACK+"SORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
            print()
            exit(0)
        except : print("\nMauvaise saisi, SVP Resaisir"); continue
        else : break
    
    while 1 :
        try :
            interv = input(f" Saisir lintervalle de point (NB sous la forme >>> a b ) :  ")
            if(len(interv.split()) != 2) :
                print(Fore.RED + "SVP, respecter la notation [a b] , Veuillez resaisir" + Fore.RESET)
                continue
            
            a, b = tuple([float(coord) for coord in interv.split()])
        except KeyboardInterrupt : 
            print("\n"+Back.WHITE+Fore.BLACK+"SORTIE DU PROGRAMME"+Back.RESET+Fore.RESET)
            print()
            exit(0)
        except : print("\nMauvaise saisi, SVP Resaisir"); continue
        else : 
            if(a >= b) :
                print(" a >= b, resaisir corretement. de facon que a < b")
                continue
            break

#calul de h et de nombre d'itération
a  = t0
h = abs(a-b)/1000

try : 
    lstPoint1 = euler(h, t0, y0, 1000, f)
    lstPoint2 = rungeKuta2_EulerModifié(h, t0, y0, 1000, f)
    lstPoint3 = rungeKuta2_PointMilieu(h, t0, y0, 1000, f)
    lstPoint4 = rungeKuta4(h, t0, y0, 1000, f)
except : pass

coupleXY1 = ([el[0] for el in lstPoint1], [el[1] for el in lstPoint1])
coupleXY2 = ([el[0] for el in lstPoint2], [el[1] for el in lstPoint2])
coupleXY3 = ([el[0] for el in lstPoint3], [el[1] for el in lstPoint3])
coupleXY4 = ([el[0] for el in lstPoint4], [el[1] for el in lstPoint4])

# Dessing des courbe
plt.plot(*coupleXY1, color = "red", label = "euler")
plt.plot(*coupleXY2, color = "blue", label = "RK2_eulerModifié")
plt.plot(*coupleXY3, color = "green", label = "RK2_PointMilieu")
plt.plot(*coupleXY4, color = "red", label = "RungeKuta4")

#Affichage des points
#plt.scatter(*coupleXY)
plt.legend()
plt.show()

"""