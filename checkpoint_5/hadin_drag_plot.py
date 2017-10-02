import numpy as np
import sys
import math
from matplotlib import pyplot

def kinetic_energy_ratio(init_velocity, final_velocity):
    return (init_velocity**2) / (final_velocity**2)

def drag_force(norm_d_coeff, velocity):
    return (-1 * norm_d_coeff * (velocity ** 2)) + (np.array([0, -9.81]))

def plot(posit_list, theta):
    x_list = [p[0] for p in posit_list]
    y_list = [p[1] for p in posit_list]
    pyplot.plot(x_list, y_list, label = "Theta = {0}".format(str(theta)))
    pyplot.xlabel('x position')
    pyplot.ylabel('y position')

def make_position_list(timestep, norm_d_coeff, init_speed, theta, init_position = np.array([0,0])):
    init_velocity = np.array([init_speed * math.cos(theta), init_speed * math.sin(theta)])
    velocity = init_velocity
    position = init_position
    posit_list = [init_position]
    while position[1] >= 0:
        position = position + (timestep * velocity)
        velocity = velocity + (timestep * drag_force(norm_d_coeff, velocity))
        posit_list.append(position)
    print("Range = ", position[0])
    return posit_list

def main():
    try:
        init_speed = float(sys.argv[1])
        theta = math.radians(float(sys.argv[2]))
        norm_d_coeff = float(sys.argv[3])
        timestep = float(sys.argv[4])
    except:
        init_speed = float(input("Initial speed: "))
        theta = math.radians(float(input("Theta: ")))
        norm_d_coeff = float(input("Normalised drag coefficient: "))
        timestep = float(input("Timestep: "))
    try:
        init_position = np.array(sys.argv[5])
    except:
        init_position = np.array([0,0])

    
    posit_list = make_position_list(timestep, norm_d_coeff, init_speed, theta, init_position)
    plot(posit_list, theta)
    pyplot.show()

main()
