import math
"""
This is a program that will take the volume of a sphere in millimetres from the user and return the radius and surface area in metres
"""
volume_milli = float(input('Enter Volume in mm: ')) #Take input
volume_metre = volume_milli / 1e6 #Convert to metres
radius_metre = (volume_metre / (4/3 * math.pi))**(1/3) #calculate radius from volume
surface_metre = 4 * math.pi * radius_metre**2 #calculate surface from radius
print('Radius = ', radius_metre, 'm') #print radius
print('Surface Area = ', surface_metre, 'm^2') #print surface area
