import numpy as np
import sys
import math
from matplotlib import pyplot

"""
This program is the one that plots the trajectory for one particle
"""

def kinetic_energy_ratio(init_velocity, final_velocity):
#Calcualtes kinetic energy ratio
    return (init_velocity**2) / (final_velocity**2)
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

def plot(posit_list, theta):
#Plots the given lists to a graph and labels it
    x_list = [p[0] for p in posit_list]
    y_list = [p[1] for p in posit_list]
    pyplot.plot(x_list, y_list, label = "Theta = {0}".format(str(theta)))
    pyplot.xlabel('x position')
    pyplot.ylabel('y position')
    pyplot.title('Projectile trajectory')

def make_position_list(timestep, norm_d_coeff, init_speed, theta, init_position = np.array([0,0])):
#Performs the time integration
    '''
    I really wish I was allowed to use scipy integrators for this but i am probably pushing it by using numpy
    '''

    init_velocity = np.array([init_speed * math.cos(theta), init_speed * math.sin(theta)]) #Turns the initial speed into a vector so easier operations can be performed on it
    velocity = init_velocity
    position = init_position
    posit_list = [init_position] #initialises posit_list to contain first position
    while position[1] >= 0: #stops when object hits ground
        velocity = velocity + (timestep * drag_force(norm_d_coeff, velocity)) #updates position and velocity
        position = position + (timestep * velocity)
        
        posit_list.append(position)
    #print("Range = ", position[0])
    return posit_list

def main():
    try:
        init_speed = float(sys.argv[1]) #takes input from commandline
        theta = math.radians(float(sys.argv[2]))
        norm_d_coeff = float(sys.argv[3])
        timestep = float(sys.argv[4])
    except:
        init_speed = float(input("Initial speed: ")) #unless it doesnt
        theta = math.radians(float(input("Theta: ")))
        norm_d_coeff = float(input("Normalised drag coefficient: "))
        timestep = float(input("Timestep: "))
    try:
        init_position = np.array(sys.argv[5])
    except:
        init_position = np.array([0,0])

    
    posit_list = make_position_list(timestep, norm_d_coeff, init_speed, theta, init_position)
    plot(posit_list, theta)
    #pyplot.axis('equal') #gives equal x and y axis
    pyplot.show() #shows graphs

main()
