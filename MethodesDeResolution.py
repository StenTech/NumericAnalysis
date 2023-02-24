from math import *


#Verifie si la fonction g est contractante ou pas.
def isContract(g, x1, x2) -> bool:
    step = abs(x1-x2)/100
    if(step >= 0.1) : step = 0.1
    x = x1
    h = 10e-10
    while(abs(derive(g, x, h)) < 1 and x <= x2):
        x+=step
        if(abs(derive(g, x, h)) > 1): break
    else:
        if(abs(derive(g, x2, h)) > 1): return False
        return True
    
    return False


#Méthode de dichotomie
def balyage(f, x1, x2):
    #try :
        step = abs(x1-x2)/10
        if(step >= 0.1) : step = 0.1
        lst_interv = list()
        a, b = x1, x1+step
        while(b <= x2):
            try:
                if(f(a)*f(b)<0): 
                    lst_interv.append((a,b))
                #temp = a
                a = b
                b = a + step
            except:
                a = b
                b = a + step
        else:     
            b = x2
            try:
                if(f(a)*f(b)<0): 
                    lst_interv.append((a,b))
            except: pass
        
        return lst_interv



def dichotomie(f, x1:float, x2:float, epsilon:float) -> float:
    try:
        if f(x1)*f(x2) > 0:  # On vérifie l'encadrement de la fonction
            raise ValueError("Mauvais choix de x1 ou x2.")
        elif f(x1)*f(x2) == 0:
            if(f(x1)==0): return x1
            else : return x2
        else:
            solution = (x1 + x2)/2.
            while abs(x1 - x2) > epsilon:
                if f(solution) == 0.:
                    return solution
                elif f(x1)*f(solution) > 0:
                    x1 = solution
                else:
                    x2 = solution
                solution = (x1 + x2)/2
            return solution
    except:
        raise ValueError("Mauvais choix de l'encadrement")

######################################
#Méthode de newton
def newton(f, a, epsilon):
    delta = 1
    h = 10e-6
    for i in range(1000):
        if delta < epsilon: return solution
        df_a = derive(f, a, h)
        #print(df_a, end=' ')
        if(df_a == 0.0): raise ZeroDivisionError("f'(x) = 0, mauxvais choix de x0. doit resaisir")
        solution = -f(a)/df_a + a
        delta = abs(solution - a)
        a = solution
        #print(solution)
        
    print("\nNombre d'itération Maximale atteint sans reponse.\nAucune solution ou Mauvais choix de X0\n")


def derive(f, a, h):

    return (f(a+h/2) - f(a-h/2))/h
        
#print( newton( , lambda x: 0.3*x**2-1 ) )
#print(newton(lambda x: 0.1*x**3-x+1, 0 , 0.001))

##################################################
#Méthode de la sécante
def secante(f, a, b, epsilon):
    for i in range(1000):
        solution = b - ( b - a ) * f(b) / ( f(b) - f(a) )
        if abs(solution - b) <= epsilon : return solution
        else:
            a, b = b, solution

########################################
#Méthode de point fixe :
def point_fixe(g, x0, epsilon):
    x = 0
    n = 1000
    while (n>=0):
        try:
            x = g(x0)
            #print(x)

            if abs(x - x0) <= epsilon:
                return x
                
            x0 = x
            n-=1
        except OverflowError:
            print("Depassement de Limites. Autrement dit il y a divergence.")
            break

    else:
        if n == -1 :
            print("\nDIVERGENCE : MAUVAIS CHOIX DE g\n")

    print("Aucun point fixe")
    return None