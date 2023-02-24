from typing import List, Tuple


def euler(h :float, t0 :float, y0 :float, n :int, f) -> List[Tuple[float, float]]:
    ensemble_sol = [(t0, y0)]
    for i in range(n):
        y0 += h*f(y0,t0)
        t0 += h

        ensemble_sol.append((t0, y0))
    
    return ensemble_sol

def rungeKuta2_EulerModifié(h :float, t0 :float, y0 :float, n :int, f) -> List[Tuple[float, float]]: 
    ensemble_sol = [(t0, y0)]
    for i in range(n):
        yy = y0 + h*f(t0, y0)
        y0 += (h/2)*(f(t0, y0) + f(t0+h, yy))
        t0 += h
        
        ensemble_sol.append((t0, y0))

    return ensemble_sol


def rungeKuta2_PointMilieu(h :float, t0 :float, y0 :float, n :int, f) -> List[Tuple[float, float]]: 
    ensemble_sol = [(t0, y0)]
    for i in range(n):
        k1 = h*f(t0, y0)
        y0 += h*f(t0 + h/2, y0 + k1/2)
        t0 += h
        
        ensemble_sol.append((t0, y0))

    return ensemble_sol


def rungeKuta4(h :float, t0 :float, y0 :float, n :int,f) -> List[Tuple[float, float]]: 

    ensemble_sol = [(t0, y0)]
    for i in range(n):
        k1 =h*f(t0, y0)
        k2 =h*f(t0+h/2, y0 + k1/2)
        k3 =h*f(t0+h/2, y0 + k2/2)
        k4 =h*f(t0+h, y0 + k3)
        y0 += (1/6)*(k1 + 2*k2+ 2*k3 + k4)
        t0 += h

        ensemble_sol.append((t0, y0))

    return ensemble_sol