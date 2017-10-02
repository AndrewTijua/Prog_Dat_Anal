import numpy as np
import sys
import math
from matplotlib import pyplot

def kinetic_energy_ratio(final_velocity, initial_velocity):
    return (final_velocity**2) / (initial_velocity**2)

def drag_acc(norm_d_coeff, velocity):
    return (-1 * norm_d_coeff * (velocity ** 2)) + (np.array([0, -9.81]))

def plot(theta_list, ke_rat_list):
    x_list = theta_list
    y_list = ke_rat_list
    pyplot.plot(x_list, y_list)
    pyplot.xlabel('Theta')
    pyplot.ylabel('Ratio of Initial to Final E_k')

def find_final_velocity(timestep, norm_d_coeff, init_speed, theta, init_position = np.array([0,0])):
    init_velocity = np.array([init_speed * math.cos(theta), init_speed * math.sin(theta)])
    velocity = init_velocity
    position = init_position
    posit_list = [init_position]
    while position[1] >= 0:
        position = position + (timestep * velocity)
        velocity = velocity + (timestep * drag_acc(norm_d_coeff, velocity))
        posit_list.append(position)
    
    return np.linalg.norm(velocity)
def main():
    try:
        init_speed = float(sys.argv[1])
        norm_d_coeff = float(sys.argv[2])
        timestep = float(sys.argv[3])
    except:
        init_speed = float(input("Initial speed: "))
        norm_d_coeff = float(input("Normalised drag coefficient: "))
        timestep = float(input("Timestep: "))
    try:
        init_position = np.array(sys.argv[4])
    except:
        init_position = np.array([0,0])

    theta_list = []
    ke_rat_list = []
    for theta in range(10,90,10):
        final_velocity = find_final_velocity(timestep, norm_d_coeff, init_speed, theta, init_position)
        ke_rat = kinetic_energy_ratio(final_velocity, init_speed)
        theta_list.append(theta)
        ke_rat_list.append(ke_rat)
    plot(theta_list, ke_rat_list)
    pyplot.show()
main()
