import cmath
"""
This is a program to calculate the roots of a quadratic equation given the coefficients a, b, and c
Author: Benjamin Cox, s1621312
"""

"""
This function calculates the root(s) of the quadratic given a, b, and c
"""
def quadratic_roots(a, b, c):
    numerator_plus = -b + cmath.sqrt(b**2 - 4*a*c) #needs both plus and minus to work
    numerator_minus = -b - cmath.sqrt(b**2 - 4*a*c)
    denominator = 2*a
    if a == 0: #In case of linear equation
        return (-c/b,)
    root1 = numerator_plus / denominator
    root2 = numerator_minus / denominator
    return(root1, root2)


"""
This function takes the input from the user and returns the final result
"""
def main():
    a, b, c = input('Enter values of a, b, c formatted as such: ').split(',')
    a, b, c = float(a), float(b), float(c)
    determinant = b**2 - 4*a*c
    roots = quadratic_roots(a, b, c)
    if len(roots) == 1 or roots[0] == roots[1]: #if linear
        print('Root is at x={0}'.format(roots[0]))
        
    else:
        print('Roots are at x={0}, x={1}'.format(roots[0], roots[1]))
    


main()
