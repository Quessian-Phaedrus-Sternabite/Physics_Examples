import matplotlib.pyplot as plt
import numpy as np

Ax = float(input("Please insert acceleration (m/s^2): "))
Vxi = float(input("Please insert velocity at start (m/s): "))
dT = int(input("Please insert how much time elapses (s [integer!!!]): "))
PXi = float(input("Please insert starting position (m): "))


# This method does not use formulae, but rather various loops
def CON_ACC_LOOP(VEL_I, ACC, POS_I, TIME, MODE):
    POS = []
    VEL = []
    ACC_G = []

    for i in TIME:
        VEL_I += ACC
        VEL.append(VEL_I)

        POS_I += VEL_I

        ACC_G.append(ACC)
        POS.append(POS_I)

        print(POS_I)

    if MODE == 1:
        return POS
    elif MODE == 2:
        return VEL
    elif MODE == 3:
        return ACC_G
    else:
        print("ERROR 1: INVALID MODE")


def CON_ACC(VEL_I, ACC, POS_I, TIME, MODE):
    POS = []
    VEL = []
    ACC_G = []
    for i in TIME:
        POS.append(POS_I + (VEL_I * i) + (.5 * (ACC * (i ** 2))))
        VEL.append(VEL_I + (ACC * i))
        ACC_G.append(ACC)
    if MODE == 1:
        return POS
    elif MODE == 2:
        return VEL
    elif MODE == 3:
        return ACC_G
    else:
        print("ERROR 1: INVALID MODE")


# Data for plotting
t = np.arange(1, dT, 1)

x1 = t
x2 = t
x3 = t

y1 = CON_ACC(Vxi, Ax, PXi, t, 1)
y2 = CON_ACC(Vxi, Ax, PXi, t, 2)
y3 = CON_ACC(Vxi, Ax, PXi, t, 3)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.suptitle('Pos, Vel, and Acc Versus Time')

ax1.plot(x1, y1, 'o-')
ax1.set_ylabel('Position (m)')

ax2.plot(x2, y2, 'o-')
ax2.set_ylabel('Velocity (m/s)')

ax3.plot(x3, y3, 'o-')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s/s')

plt.show()

fig.savefig("Graphs.png")
plt.show()