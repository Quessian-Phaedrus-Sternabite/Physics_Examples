import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants

G = 6.67408e-11
msun = 1988500e24
m = msun

au = 149597870.700e3 # AU to m
v_factor = 1731460  # As velocities given in AU/day so conversion needed -> m/s

# Position of earth - data from JPL

x_pos = 1.168490293769851E-01 * au
y_pos = 9.773086489128535E-01 * au
z_pos = -4.581805315603911E-05 * au

x_vel = -1.737065829712975E-02 * v_factor
y_vel = 1.978209219640221E-03 * v_factor
z_vel = 6.491444436868095E-07 * v_factor


def f_grav(t, y):
    x1, x2, x3, v1, v2, v3 = y
    dydt = [v1, v2, v3, -x1 * G * m / (x1 ** 2 + x2 ** 2 + x3 ** 2) ** (3 / 2),
            -x2 * G * m / (x1 ** 2 + x2 ** 2 + x3 ** 2) ** (3 / 2),
            -x3 * G * m / (x1 ** 2 + x2 ** 2 + x3 ** 2) ** (3 / 2)]
    return dydt


year = 31557600.e0  # seconds in 365.25 days
tEnd = 1.0 * year

domain = (0, tEnd)
init = [x_pos, y_pos, z_pos, x_vel, y_vel, z_vel]
ans = solve_ivp(fun=f_grav, t_span=domain, y0=init)

plt.plot(ans['y'][0], ans['y'][1])
plt.plot([0.], [0.], 'o')

plt.show()