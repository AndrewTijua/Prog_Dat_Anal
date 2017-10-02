import numpy as np
import sys
import math
from matplotlib import pyplot
"""
This program is the one that plots the kinetic energy ratios for many theta
"""


def kinetic_energy_ratio(init_velocity, final_velocity):
    #gives kinetic energy ratio between final and initial
    return (final_velocity ** 2) / (init_velocity ** 2) 
'''
def drag_force(norm_d_coeff, velocity):
#Calculates the acceleration due to drag as a vector
    return (-1 * norm_d_coeff * (velocity ** 2)) + (np.array([0, -9.81]))
'''
def drag_force(norm_d_coeff, velocity):
    #gives the drag force as a vector
    vel_mag = np.linalg.norm(velocity)
    drag_force = [0,0]
    drag_force[0] = -1 * norm_d_coeff * vel_mag * velocity[0]
    drag_force[1] = -1 * norm_d_coeff * vel_mag * velocity[1] - 9.81
    return np.array(drag_force)
    

def plot(x_list, y_list):
    #Plots the graph of theta against EK ratio, gives sensible axis labels
    pyplot.plot(x_list, y_list)
    pyplot.xlabel('Theta')
    pyplot.ylabel('Ek_f / Ek_i')
    pyplot.title('Plot of kinetic energies and initial angles')

def find_final_velocity(timestep, norm_d_coeff, init_speed, theta, init_position = np.array([0,0])):
    #Performs time integration
    init_velocity = np.array([init_speed * math.cos(theta), init_speed * math.sin(theta)]) #turns the 'polar' velocity into a cartesian vector
    velocity = init_velocity #initialises variables
    position = init_position
    posit_list = [init_position]
    while position[1] >= 0: #stops when object hits ground
        position = position + (timestep * velocity)
        velocity = velocity + (timestep * drag_force(norm_d_coeff, velocity)) #updates position and velocity vectors
        posit_list.append(position)
    return (np.linalg.norm(velocity), position[0]) #returns a tuple of the final velocity and the range

def main():
    try:
        init_speed = float(sys.argv[1]) #attempts command line inputs
        norm_d_coeff = float(sys.argv[2])
        timestep = float(sys.argv[3])
    except:
        init_speed = float(input("Initial speed: ")) #incase improper CLAs
        norm_d_coeff = float(input("Normalised drag coefficient: "))
        timestep = float(input("Timestep: "))
    try:
        init_position = np.array(sys.argv[4])
    except:
        init_position = np.array([0,0])
    
    thetas = []
    ke_rats = []
    for theta in range(0, 90, 1): #this loop appends the Ek ratio and theta to lists
        thetas.append(theta)
        vel = find_final_velocity(timestep, norm_d_coeff, init_speed, math.radians(theta), init_position)[0]
        ke_rats.append(kinetic_energy_ratio(init_speed, vel))
    
    plot(thetas, ke_rats) #plots ratios against thetas
    pyplot.show()

main()
