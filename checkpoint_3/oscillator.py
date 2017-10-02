import math
from matplotlib import pyplot


"""
This function calculates the displacement of the oscillator given omega_zero, gamma and time
"""
def shm(omega_zero, gamma, t):
    a = 1
    if gamma > 2*omega_zero:#over damped
        p = math.sqrt(((gamma ** 2)/4) - omega_zero ** 2)
        b = gamma / (2 * p)
        return math.exp(-(gamma*t)/2) * (a * math.cosh(p*t) + b * math.sinh(p*t))

    if gamma == 2*omega_zero: #crit damped
        b = gamma / 2
        return math.exp(-(gamma*t)/2)*(a + b * t)

    if gamma < 2*omega_zero: #under damped
        omega = math.sqrt((omega_zero ** 2) - ((gamma ** 2)/4))
        b = gamma / (2 * omega)
        return math.exp(-(gamma*t)/2) * (a * math.cos(omega*t) + b * math.sin(omega*t))

"""
Labels the axis and plots the graph of displacement against time
"""
def plot(displacement_list, t_list): 
    pyplot.plot(t_list, displacement_list)
    pyplot.ylabel('Displacement (m)')
    pyplot.xlabel('Time (s)')
    pyplot.title('Displacement of damped oscillator')
    pyplot.show() #Displays plot
    
"""
This function takes in the values from the user and computes the lists for plotting
"""
def main():
    omega_zero, gamma, num_points = input('Enter omega_zero, gamma, number of points to plot formatted as prior: ').split(', ')
    omega_zero, gamma, num_points = float(omega_zero), float(gamma), int(num_points) #initialise and cast variables
    time_max = (5*math.pi) / omega_zero
    t_list = [] #Time list
    displacement_list = [] #Displacement list

    for i in range(num_points): #Calculates and creates lists of displacements and time
        t_list.append((time_max / num_points)*i)
        displacement_list.append(shm(omega_zero, gamma, t_list[i])) 
        
    plot(displacement_list, t_list)#Shows the plot of displacement against time
                                 
        
main()
