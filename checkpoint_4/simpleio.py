import math
from matplotlib import pyplot

"""
This function plots the graph of logpower against time and labels the axis appropriately
"""
def plot(t_list, logpower_list):
    pyplot.plot(t_list, logpower_list)
    pyplot.xlabel('Time(s)')
    pyplot.ylabel('log(V(t)I(t)')
    pyplot.show()

"""
This function reads the file and prepares the appropriate lists
"""
def readToList(filename):
    volt_list, current_list, logpower_list, t_list = [], [], [], []
    file = open(filename, 'r')
    content = file.readlines() #holds the content of the file
    #print(content)
    for line in content:
        if line[0] == '#': #checks if file line is comment
            print("Skipped comment") 
        else:
            volts, current = line.split(' , ') #splits lines into appropriate data
            volt_list.append(float(volts))
            current_list.append(float(current))

    for i in range(len(volt_list)):
        logpower_list.append(math.log(volt_list[i]*current_list[i])) #calculates logpower for each pair of voltage and current and appends to logpower list
        t_list.append(float(i/25000))
    file.close()
    return (t_list, logpower_list)
            
            
        

def main():
    filename = input("Enter name of file(with extension): ")
    print(filename)
    lists = readToList(filename)
    plot(lists[0], lists[1])

main()


