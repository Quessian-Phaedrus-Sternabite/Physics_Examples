import numpy as np
import math
import scipy.constants as sc
import matplotlib.pyplot as plt

i = 0
it = .1

class body():
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass


class gravity():
    def __init__(self, gx, gy):
        self.gx = gx
        self.gy = gy


def GRAV(x1, y1, x2, y2, m1, m2):
    dx = np.sqrt(abs(x2 - x1))
    dy = np.sqrt(abs(y2 - y1))
    d = np.sqrt(dx ** 2 + dy ** 2)

    theta = math.atan(dy / dx)

    g = sc.G * ((m1 + m2) / d ** 2)

    gx = g * math.cos(theta)
    gy = g * math.sin(theta)
    grav = gravity(gx, gy)
    return grav


et = 10 # milliseconds

m1 = body(0, 0, 0, 0, 1000000000)
m2 = body(100, 100, 0, 0, 10000000)

m1_pos_x = []
m1_pos_y = []
m2_pos_x = []
m2_pos_y = []

m1_vel_x = []
m1_vel_y = []


while(i < et):
    grav = GRAV(m1.x, m1.y, m2.x, m2.y, m1.mass, m2.mass)

    print(f'mass 1 x: {m1.x}')

    if m1.x < m2.x:
        gx1 = grav.gx/m1.mass
        gx2 = -grav.gx/m2.mass
    elif m1.y < m2.y:
        gy1 = grav.gy/m1.mass
        gy2 = -grav.gy/m2.mass
    elif m1.x > m2.x:
        gx1 = -grav.gx/m1.mass
        gx2 = grav.gx/m2.mass
    elif m1.y > m2.y:
        gy1 = -grav.gy/m1.mass
        gy2 = grav.gy/m2.mass
    else:
        break

    # Mass 1 X
    x1f = m1.x + (m1.vx * it) + (.5 * grav.gx * (it ** 2))
    vx1f = m1.vx + grav.gx * it
    
    m1_pos_x.append(x1f)

    m1.x = x1f
    m1.vx = vx1f

    # Mass 1 Y
    y1f = m1.y + (m1.vy * it) + (.5 * grav.gy * (it ** 2))
    vy1f = m1.vy + grav.gy * it

    m1_pos_y.append(y1f)

    m1.y = y1f
    m1.vy = vy1f

    # Mass 2 X
    x2f = m2.x + (m2.x * it) + (.5 * grav.gx * (it ** 2))
    vx2f = m2.vx + grav.gx * it

    m2_pos_x.append(x2f)

    m2.x = x2f
    m2.vx = vx2f

    # Mass 2 Y
    y2f = m2.y + (m2.y * it) + (.5 * grav.gy * (it ** 2))
    vy2f = m2.vy + grav.gy * it

    m2_pos_y.append(y2f)

    m2.y = y2f
    m2.vy = vy2f

    i += it

# Data for plotting


fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Gravity Sim ')

ax1.plot(m1_pos_x, m1_pos_y)
ax1.set_ylabel('y (m)')
ax1.grid()

ax2.plot(m2_pos_x, m2_pos_y)
ax2.set(xlabel='x (m)', ylabel='y (m)')

ax2.grid()

fig.savefig("test.png")
plt.show()
