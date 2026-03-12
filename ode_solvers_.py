import numpy as np
import matplotlib as plt

from typing import Callable

def verlet_method_second_order_2D(f,t0,r0,v0,tf,h=0.0001):
    """Método de Verlet para resolver ecuaciones diferenciales de segundo orden en 2D."""
    
    # Inicializamos vectores para guardar la solución
    t = np.arange(start=t0, step=h, stop=tf + h)
    r = np.zeros(shape=(len(t), 2)) #posición
    v = np.zeros_like(r) 
    a = np.zeros_like(r) #aceleración

    # Fijamos las condiciones iniciales :) 
    r[0] = r0
    v[0] = v0
    a[0] = f(t[0],r[0],v[0])

    # Iteramos
    for n in range(len(t) - 1):
        r[n+1]= r[n]+h*v[n] + ((h**2)/2) * a[n]
        a[n+1]= f(t[n+1],r[n+1], v[n+1])
        v[n+1]= v[n] + (h/2)*(a[n]+a[n+1])
        
    return t, r, v