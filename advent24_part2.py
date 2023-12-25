with open("input24.txt") as fin:
    pos = {}
    vel = {}
    count = 0
    for i,line in enumerate(fin):
        count += 1
        [posi , velo] = line.strip("\n").split(" @ ")
        pos[i] = [int(j) for j in posi.split(", ")]
        vel[i] = [int(j) for j in velo.split(", ")]

from math import sqrt

def why(x):
    Ay = (vx2*(x1-x)-vx1*(x2-x))*(x1-x3) - (vx3*(x1-x)-vx1*(x3-x))*(x1-x2)
    By = (x1-x3)*(y1*vx1*(x2-x) - vy1*(x1-x)*(x2-x) - y2*vx2*(x1-x) + vy2*(x2-x)*(x1-x)) + \
        (vx2*(x1-x)-vx1*(x2-x))*(y1*(x3-x)-y3*(x1-x)) - \
        (x1-x2)*(y1*vx1*(x3-x) - vy1*(x1-x)*(x3-x) - y3*vx3*(x1-x) + vy3*(x3-x)*(x1-x)) - \
        (vx3*(x1-x)-vx1*(x3-x))*(y1*(x2-x)-y2*(x1-x))
    Cy = (y1*vx1*(x2-x) - vy1*(x1-x)*(x2-x) - y2*vx2*(x1-x) + vy2*(x2-x)*(x1-x))*(y1*(x3-x)-y3*(x1-x)) - \
        (y1*vx1*(x3-x) - vy1*(x1-x)*(x3-x) - y3*vx3*(x1-x) + vy3*(x3-x)*(x1-x))*(y1*(x2-x)-y2*(x1-x))

    return  (-By - sqrt(By**2 -4*Ay*Cy))/(2*Ay)

def zee(x):
    Az = (vx2*(x1-x)-vx1*(x2-x))*(x1-x3) - (vx3*(x1-x)-vx1*(x3-x))*(x1-x2)
    Bz = (x1-x3)*(z1*vx1*(x2-x) - vz1*(x1-x)*(x2-x) - z2*vx2*(x1-x) + vz2*(x2-x)*(x1-x)) + \
        (vx2*(x1-x)-vx1*(x2-x))*(z1*(x3-x)-z3*(x1-x)) - \
        (x1-x2)*(z1*vx1*(x3-x) - vz1*(x1-x)*(x3-x) - z3*vx3*(x1-x) + vz3*(x3-x)*(x1-x)) - \
        (vx3*(x1-x)-vx1*(x3-x))*(z1*(x2-x)-z2*(x1-x))
    Cz = (z1*vx1*(x2-x) - vz1*(x1-x)*(x2-x) - z2*vx2*(x1-x) + vz2*(x2-x)*(x1-x))*(z1*(x3-x)-z3*(x1-x)) - \
        (z1*vx1*(x3-x) - vz1*(x1-x)*(x3-x) - z3*vx3*(x1-x) + vz3*(x3-x)*(x1-x))*(z1*(x2-x)-z2*(x1-x))

    return (-Bz - sqrt(Bz**2 -4*Az*Cz))/(2*Az)

def f(x):
    Ay = (vx2*(x1-x)-vx1*(x2-x))*(x1-x3) - (vx3*(x1-x)-vx1*(x3-x))*(x1-x2)
    By = (x1-x3)*(y1*vx1*(x2-x) - vy1*(x1-x)*(x2-x) - y2*vx2*(x1-x) + vy2*(x2-x)*(x1-x)) + \
        (vx2*(x1-x)-vx1*(x2-x))*(y1*(x3-x)-y3*(x1-x)) - \
        (x1-x2)*(y1*vx1*(x3-x) - vy1*(x1-x)*(x3-x) - y3*vx3*(x1-x) + vy3*(x3-x)*(x1-x)) - \
        (vx3*(x1-x)-vx1*(x3-x))*(y1*(x2-x)-y2*(x1-x))
    Cy = (y1*vx1*(x2-x) - vy1*(x1-x)*(x2-x) - y2*vx2*(x1-x) + vy2*(x2-x)*(x1-x))*(y1*(x3-x)-y3*(x1-x)) - \
        (y1*vx1*(x3-x) - vy1*(x1-x)*(x3-x) - y3*vx3*(x1-x) + vy3*(x3-x)*(x1-x))*(y1*(x2-x)-y2*(x1-x))


    Az = (vx2*(x1-x)-vx1*(x2-x))*(x1-x3) - (vx3*(x1-x)-vx1*(x3-x))*(x1-x2)
    Bz = (x1-x3)*(z1*vx1*(x2-x) - vz1*(x1-x)*(x2-x) - z2*vx2*(x1-x) + vz2*(x2-x)*(x1-x)) + \
        (vx2*(x1-x)-vx1*(x2-x))*(z1*(x3-x)-z3*(x1-x)) - \
        (x1-x2)*(z1*vx1*(x3-x) - vz1*(x1-x)*(x3-x) - z3*vx3*(x1-x) + vz3*(x3-x)*(x1-x)) - \
        (vx3*(x1-x)-vx1*(x3-x))*(z1*(x2-x)-z2*(x1-x))
    Cz = (z1*vx1*(x2-x) - vz1*(x1-x)*(x2-x) - z2*vx2*(x1-x) + vz2*(x2-x)*(x1-x))*(z1*(x3-x)-z3*(x1-x)) - \
        (z1*vx1*(x3-x) - vz1*(x1-x)*(x3-x) - z3*vx3*(x1-x) + vz3*(x3-x)*(x1-x))*(z1*(x2-x)-z2*(x1-x))

    y =  (-By - sqrt(By**2 -4*Ay*Cy))/(2*Ay)
    z = (-Bz - sqrt(Bz**2 -4*Az*Cz))/(2*Az)

    equation = (z*(x1-x) + z1*(x2-x) - z*(x2-x) - z2*(x1-x)) * \
            (y*vx2*(x1-x) + y1*vx1*(x2-x) - vy1*(x1-x)*(x2-x) - y*vx1*(x2-x) - y2*vx2*(x1-x) + vy2*(x2-x)*(x1-x)) \
            - (y*(x1-x) + y1*(x2-x) - y*(x2-x) - y2*(x1-x)) * \
            (z*vx2*(x1-x) + z1*vx1*(x2-x) - vz1*(x1-x)*(x2-x) - z*vx1*(x2-x) - z2*vx2*(x1-x) + vz2*(x2-x)*(x1-x))

    return equation

from scipy.optimize import fsolve
from sympy import Abs
import warnings
warnings.filterwarnings("ignore")

for i in range(count - 2):
    y1 = pos[i][1]
    y2 = pos[i+1][1]
    y3 = pos[i+2][1]
    x1 = pos[i][0]
    x2 = pos[i+1][0]
    x3 = pos[i+2][0]
    z1 = pos[i][2]
    z2 = pos[i+1][2]
    z3 = pos[i+2][2]
    vx1 = vel[i][0]
    vx2 = vel[i+1][0]
    vx3 = vel[i+2][0]
    vy1 = vel[i][1]
    vy2 = vel[i+1][1]
    vy3 = vel[i+2][1]
    vz1 = vel[i][2]
    vz2 = vel[i+1][2]
    vz3 = vel[i+2][2]

    for j in range(200000000000000 , 400000000000000 , 1000000000000):
        initial_guess = j
        try:
            root = fsolve(f, initial_guess)
            if Abs(root[0] - round(root[0])) < 0.001:
                if Abs(why(round(root[0])) - round(why(round(root[0])))) < 0.001 and Abs( zee(round(root[0])) - round(zee(round(root[0])))) < 0.001 and 200000000000000 <= root[0] and root[0]  <= 400000000000000:
                    sol = round(root[0]) + round(why(root[0])) + round(zee(root[0]))
                    print("potential solution")
                    print(sol)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
