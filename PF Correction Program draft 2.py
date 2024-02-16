# Joe, Eric, Cristian, David
#EE 347
#Lab 2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import axes3d

#This function takes any value for P and Q and returns PF_new, Qc needed to correct to PF_new and PF old.
def findQbyStep(Q, P, PF_old):
    Q_old = Q
    PF_new = PF_old
    Q_c = 0
    Q_new = Q_old + Q_c                      #Qc = Q_new - Q_old
    Qc_counter = 0                           #records the number of Qc that were used to correct power factor.
    while (PF_new < 0.95) or (PF_new > 1.0):
        Q_c = Q_c - .25                       #-0.25 here defines the step value of Q_c
        Qc_counter = Qc_counter + 1
        Q_new = Q_old + Q_c
        PF_new = np.cos(np.arctan(Q_new / P))
    Q_c = Q_new - Q_old
    if (P / PF_old) > 10:  # Check if |S| > 10 MVA, if true, set Qc, PF_new and PF_old to not a number.
        Q_c = float('nan')
        PF_new = float('nan')
        PF_old = float('nan')
    return PF_new, Q_c, PF_old

########### Initialize arrays that will hold values #########
P_array = np.linspace(1, 10, 30)    #Changing the number of steps in the array for P,
                                    #changes the resolution of the final plot.
Q_array = np.linspace(0, 10, len(P_array))
Qc_array = np.zeros((len(P_array), len(P_array)))
PF_oldArray = np.zeros((len(P_array), len(P_array)))
PF_newArray = np.zeros((len(P_array), len(P_array)))
# Step through each array to find PF_old, PF_ new for
for i, P in enumerate(P_array):
    for j, Q in enumerate(Q_array):
        #print('P = ', P, 'Q = ', Q)
        #PF_oldArray[[j],[i]] = np.cos(np.arctan(Q/P))
        PF_newArray[[j],[i]], Qc_array [[j],[i]], PF_oldArray[[j],[i]]= findQbyStep(Q, P, np.cos(np.arctan(Q/P)))


P_array, Q_array = np.meshgrid(P_array, Q_array)

##########Plot##############
# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.7))
# =============
# First subplot
# =============
# set up the axes for the first plot
ax = fig.add_subplot(2, 2, 1, projection='3d')

surf = ax.plot_surface(P_array, Q_array, PF_oldArray, cmap=cm.coolwarm,    # plot first plot
                       linewidth=0, antialiased=False)
ax.set_zlim(0, 1.0)
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel('P (MW)')
ax.set_ylabel('Q (MVAR)')
ax.set_zlabel('PF')
ax.set_title('PF old')
ax.view_init(elev=30, azim=45)
fig.colorbar(surf, shrink=0.3, aspect=10)

# ==============
# Second subplot
# ==============
# set up the axes for the second plot
ax = fig.add_subplot(2, 2, 2, projection='3d')

surf = ax.plot_surface(P_array, Q_array, PF_newArray, cmap=cm.coolwarm,    # plot second plot
                        linewidth=0, antialiased=False)
ax.set_zlim(0.8, 1.0)
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel('P (MW)')
ax.set_ylabel('Q (MVAR)')
ax.set_zlabel('PF')
ax.set_title('PF new')
ax.view_init(elev=30, azim=45)
fig.colorbar(surf, shrink=0.3, aspect=10)

# ==============
# Third subplot
# ==============
# set up the axes for the second plot
ax = fig.add_subplot(2, 2, 3, projection='3d')

surf = ax.plot_surface(P_array, Q_array, Qc_array, cmap=cm.coolwarm,  # Plot third plot
                        linewidth=0, antialiased=False)
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel('P (MW)')
ax.set_ylabel('Q (MVAR)')
ax.set_zlabel('Qc (MVAR)')
ax.set_title('Qc')
ax.view_init(elev=30, azim=45)
fig.colorbar(surf, shrink=0.3, aspect=10)

plt.show()
