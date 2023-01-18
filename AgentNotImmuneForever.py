'''
Created on Nov 25, 2022

@author: Allen Minch
'''
import numpy as np
import matplotlib.pyplot as plt
import math
import random

#population size
N = 100

#0=susceptible; 1=infected; 2=recovered
# this disease would not have to be the flu, I was just borrowing some code from the in-class exercise we
# did on agent-based models
flu_status = np.zeros(N)
# an array to keep track of the time at which infected individuals in the population recover
time_immune = np.zeros(N)

# Number of people each person in the population is simulated to meet each day (though the actual number
# of people met could be more if some people that a person is not simulated as meeting were simulated as
# meeting the person
m = 3

# probability of recovery over the night
p = 0.15

# time immunity lasts in days
d_R = 15

#days in simulation
time_window = 360

#someone got sick!
flu_status[0] = 1

#initialize arrays
number_healthy = np.zeros(time_window)
number_sick = np.zeros(time_window) 
number_recovered = np.zeros(time_window)
for day in range(time_window):
    #first thing in the morning, we count who's sick
    number_healthy[day] = sum(flu_status == 0)
    number_sick[day] = sum(flu_status == 1)
    number_recovered[day] = sum(flu_status == 2)

    #we'll assume it takes a day to become infectious
    #and you can't recover during the first day.
    flu_status_new = flu_status.copy()

    #day time: meet & transmit virus :/ 
    for i in range(N):
        for j in range(m):
            individual_1 = i
            individual_2 = int(math.floor(N*random.random()))
            if (flu_status[individual_1] == 1) and (flu_status[individual_2] == 0):
                flu_status_new[individual_2] = 1
            elif(flu_status[individual_1] == 0) and (flu_status[individual_2] == 1):
                flu_status_new[individual_1] = 1
  
    #night time: sleep & recover, or become susceptible again after being recovered if immunity is up
    for i in range(N):
        if (flu_status[i] == 1):
            if random.random() < p:
                flu_status_new[i] = 2
                time_immune[i] = day + 1
        elif (flu_status[i] == 2):
            if (time_immune[i] == day - d_R):
                flu_status_new[i] = 0

    flu_status = flu_status_new.copy()

# Plot S(t), I(t), and R(t) over time window
plt.figure()
p0,=plt.plot(number_healthy,'ko-')
p1,=plt.plot(number_sick,'bo-')
p2,=plt.plot(number_recovered,'ro-')
plt.legend([p0,p1,p2],["S(t)","I(t)","R(t)"])
plt.xlabel('Time (days)')
plt.ylabel('Number')
plt.title("m = 3, p = 0.15, d_R = 15")
plt.xlim(0,360)
# running means of the number of individuals in each category (would have the purpose of estimating the
# expected long-run number of people in each of these categories)
print(np.mean(number_healthy))
print(np.mean(number_sick))
print(np.mean(number_recovered))
#plt.ylim(0,100)
plt.show()