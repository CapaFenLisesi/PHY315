# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate mixed mode of oscillation
of two spring-coupled mass problem. Plots normal modes.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup plotting space
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(2,1,1)
ax3 = fig.add_subplot(3,1,1)
fig.subplots_adjust(hspace=.45)

# Set physical parameters
# k - spring constant (newton/meter)
# m -  mass (kg)
# A - amplitude (meter)

k   = 100 
m   = 20
A   = 0.175

# Set derived parameters
# w1        - angular frequency of first normal mode (radian/second)
# w2        - angular frequency of second normal mode (radian/second)

w1 = np.sqrt(k/m)
w2 = np.sqrt(3.*k/m)

# Function to return coordinate of center of first mass
def X1(t):
    global w1, A
    return 1. + A*np.cos(w1*t) + A*np.cos(w2*t)

# Function to return coordinate of center of second mass
def X2(t):
    global w2, A
    return 2. + A*np.cos(w1*t) - A*np.cos(w2*t)

# Function to return first normal coordinate 
def N1(t):

    return (X1(t)+X2(t)-3.)/2.

# Function to return second normal coordinate
def N2(t):

    return (X1(t)-X2(t)+1.)/2.

# Function to return coordinates of mass corners
def position(x):
    x1 = x - 0.15
    x2 = x + 0.15
    y1 = 0.25 
    y2 = -0.25

    p1 = [x1, y2]
    p2 = [x2, y2]
    p3 = [x2, y1]
    p4 = [x1, y1]
    
    return [p1, p2, p3, p4]

# Simulation parameters
# counter - current time
# xt      - time
# x1      - coordinate of center of first mass
# x2      - coordinate of center of second mass

counter =  0
xt      = [0]
x1      = [0]
x2      = [0]

def animate(i):
    global counter, xt, x1, x2, A
    ax3.clear()

    # Generate mass-spring animation plot
    plt.subplot(311)
    plt.xlim(0., 3.)
    plt.ylim(-1., 1.)
    plt.xlabel("Position (m)")
    plt.title(R"$k = 100\,{\rm N/m}\,\,\,m = 20\,{\rm kg}\,\,\,\hat{\eta}_1=\hat{\eta}_2= 0.175\,{\rm m}$", size="large")
    
    # Get coordinates of first mass corners
    p11 = [position(X1(counter))[0][0], position(X1(counter))[0][1]]
    p21 = [position(X1(counter))[1][0], position(X1(counter))[1][1]]
    p31 = [position(X1(counter))[2][0], position(X1(counter))[2][1]]
    p41 = [position(X1(counter))[3][0], position(X1(counter))[3][1]]

    x = [p11[0], p21[0], p31[0], p41[0], p11[0]]
    y = [p11[1], p21[1], p31[1], p41[1], p11[1]]

    # Plot first mass
    plt.plot(x, y, lw=3, color="blue")

    # Plot center of first mass
    data_x = [X1(counter)]
    data_y = [0.]
    plt.plot(data_x, data_y, 'o', color="black")

    # Get coordinates of second mass corners
    p12 = [position(X2(counter))[0][0], position(X2(counter))[0][1]]
    p22 = [position(X2(counter))[1][0], position(X2(counter))[1][1]]
    p32 = [position(X2(counter))[2][0], position(X2(counter))[2][1]]
    p42 = [position(X2(counter))[3][0], position(X2(counter))[3][1]]

    x = [p12[0], p22[0], p32[0], p42[0], p12[0]]
    y = [p12[1], p22[1], p32[1], p42[1], p12[1]]

    # Plot second mass
    plt.plot(x, y, lw=3, color="blue")

    # Plot center of second mass
    data_x = [X2(counter)]
    data_y = [0.]
    plt.plot(data_x, data_y, 'o', color="black")

    # Plot springs
    linex = [0., p11[0]]
    liney = [0, 0]
    plt.plot(linex, liney, color="red", ls=":", lw=5)
    linex = [p12[0], p21[0]]
    plt.plot(linex, liney, color="red", ls=":", lw=5)
    linex = [p22[0], 3.]
    plt.plot(linex, liney, color="red", ls=":", lw=5)

    # Generate eta_1 plot
    plt.subplot(312)
    xt.append(counter)
    x1.append(N1(counter))
    plt.ylabel("$\eta_1$ (m)")
    plt.xlabel("Time (s)")
    plt.xlim(0,15)
    plt.ylim(-A-0.1, A+0.1)
    plt.plot(xt, x1, lw=1, color="green")
    plt.plot([0,15], [0,0], lw=0.5, color="black")

    # Generate eta_2 plot
    plt.subplot(313)
    x2.append(N2(counter))
    plt.ylabel("$\eta_2$ (m)")
    plt.xlabel("Time (s)")
    plt.xlim(0, 15)
    plt.ylim(-A-0.1, A+0.1)
    plt.plot(xt, x2, lw=1, color="green")
    plt.plot([0,15], [0,0], lw=0.5, color="black")

    dt = 0.075
    counter += dt
        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()
