from time import sleep
import matplotlib.pyplot as plt
from math import *

from Deriv_Integr_Numerik import euler, rungeKute2_EulerModifié, rungeKute2_PointMilieu

while(1):
    try :
        function_str = input("Svp saissez f(t, y) : dans l'equa-diff [y' = f(t, y)] :\n\n\t f(t, y)] = ")
        f = None
        exec(f"f = lambda t, y : {function_str}")
    except :
        

try : 
    lstPoint = rungeKute2_PointMilieu(0.001, 0, 1, 1000, f)
except : pass

coupleXY = ([el[0] for el in lstPoint], [el[1] for el in lstPoint])
# Dessing de la courbe
plt.plot(*coupleXY)

#Affichage des points
#plt.scatter(*coupleXY)

plt.show()