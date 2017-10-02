import numpy as np
import sys
import math
from matplotlib import pyplot

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
    
    return posit_list

def many_angles(timestep, norm_d_coeff, init_speed, theta_start, theta_end, theta_steps = 4, init_position = np.array([0,0])):
    many_lists = []
    for i in np.linspace(theta_start, theta_end, theta_steps):
        many_lists.append((make_position_list(timestep, norm_d_coeff, init_speed, i, init_position), i))
    return many_lists

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
        init_position = np.array(sys.argv[7])
        theta_start = theta
        theta_end = np.array(sys.argv[5])
        theta_steps = float(sys.argv[6])
    except:
        init_position = np.array([0,0])

    
    try:
        for i in many_angles(timestep, norm_d_coeff, init_speed, theta_start, theta_end, theta_steps, init_position):
            plot(i[0], i[1])
        pyplot.show()
    except:
        posit_list = make_position_list(timestep, norm_d_coeff, init_speed, theta, init_position)
        plot(posit_list, theta)
        pyplot.show()
main()
