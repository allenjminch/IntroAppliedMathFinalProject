'''
Created on Nov 23, 2022

@author: Allen Minch
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# set the parameters beta, gamma, and lambda in the extended differential equation model
beta = 0.01
gamma = 0.6
lamb = 1.8

# dS/dt, dI/dt, and dR/dt for extended model
def deriv (x,t):
    S = x[0] # S
    I = x[1] # I
    R = x[2] # R
    dSdt = -beta * S * I + lamb * R # dS/dt
    dIdt = beta * S * I - gamma * I # dI/dt
    dRdt = gamma * I - lamb * R # dR/dt
    return np.array([dSdt, dIdt, dRdt])

time =np.linspace (0, 180, 10000) # interval of 10000 equally spaced time points for running the simulation
xinit =np.array ([99,1,0]) # initial conditions for S, I, and R, respectively
x= odeint(deriv ,xinit , time ) # solves the system of differential equations numerically over the time range above
# producing an n x 3 matrix where n is the number of time points, the first column is S, second column is I, and third
# column is R
plt.figure()
p0 ,= plt.plot (time ,x [: ,0]) # plots S(t) with time by taking the first column of x 
p1 ,= plt.plot (time ,x [: ,1]) # Plots I(t) with time by taking the second column of x
p2 ,= plt.plot (time ,x [: ,2]) # Plots R(t) with time by taking the third column of x
plt.legend([p0 ,p1 ,p2 ],["S(t)","I(t)","R(t)"]) # makes a legend for the plot
plt.title("beta = 0.01, gamma = 0.6, lambda = 1.8")
plt.xlabel('t ( Days )') # label on x-axis
plt.ylabel('Population') # label on y-axis
print("Long run S = {0}, Long run I = {1}, Long run R = {2}".format(x[:, 0][-1], x[:, 1][-1], x[:, 2][-1]))
plt.show() # display the plot