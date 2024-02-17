# Joe, Eric, Cristian, David
#EE 347
#Lab 2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import axes3d

def PF_corrector(P_l, Q_l):
    PF_new = 1
    Q_new = (P_l / PF_new) * np.sin(np.arccos(PF_new))
    Q_c = Q_new - Q_l
    Q_cr = np.round(Q_c * 4) / 4
    PF_check = np.cos(np.arctan((Q_cr + Q_l) / P_l))
    #print(PF_check)
    return Q_cr

good_input = 0
while good_input != 1:
    print('P_l in MW = ', end='')
    P_l = float(input())
    print('Q_l in MW = ', end='')
    Q_l = float(input())
    if (1 <= P_l) and (P_l <= 10) and (0 <= Q_l) and (Q_l <= 10):
        good_input = 1

Q_cr = PF_corrector(P_l, Q_l)
print('Q_cr = ', Q_cr)

##########Plot##############
P_array = np.arange(1, 10, .25)
Q_array = np.linspace(0, 10, len(P_array))

Qcr_array = np.zeros((len(P_array), len(P_array)))
for i, P in enumerate(P_array):
    for j, Q in enumerate(Q_array):
        Qcr_array[[j],[i]] = PF_corrector(P, Q)
print(Qcr_array)
# Plot the surface.
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.contourf(P_array, Q_array, Qcr_array, 40, cmap=cm.coolwarm)


# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel('P')
ax.set_ylabel('Q')
ax.set_zlabel('Qc')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
