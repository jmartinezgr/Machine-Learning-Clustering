import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

valor = (2.2,1/2.3)

def modelo(beta,gamma):
    N = 3.2e6             # poblacion total N de medellin
    I0, R0 = 1, 0         # Valores iniciales de personas Infectadas (I0) y personas que se recuperaron (R0)
    S0 = N - I0 - R0      # El resto de la población    , S0 son las personas que están sujetos a infección inicialmente.

    t = np.linspace(0, 40, 40)       # Puntos en la gráfica (En días)
    # Las ecuaciones diferenciales del modelo SIR

    def deriv(y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N    
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

# Vector de las condiciones iniciales
    y0 = S0, I0, R0
    # Resolver el sistema de ecuaciones diferenciales, en la secuencia de días que ya definimos
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    return (ret.T)

#Para la parte de las gráficas:
fig, ax = plt.subplots()

#Calculamos los valor de S,I y r a partir de β y γ
modelos = modelo(*valor)

#Graficamos la poblacion suceptible en funcion del tiempo
ax.plot(np.linspace(0,40,40), modelos[0],label = 'Suceptible')
#Graficamos la poblacion suceptible en funcion del tiempo
ax.plot(np.linspace(0,40,40), modelos[1],label = 'Infectious')
#Graficamos la poblacion suceptible en funcion del tiempo

#Modificamos aspectos visuales
ax.plot(np.linspace(0,40,40), modelos[2],label = 'Recovered')
ax.set_title(label='Modelo SIR', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.xlabel("Días", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.ylabel('Población')
ax.legend(loc = 'center right')

#Graficamos
plt.show()