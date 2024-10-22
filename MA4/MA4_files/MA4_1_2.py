
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 

    """Approximates the volume of a d-dimensional hypersphere using Monte Carlo."""
    inside_sphere = 0

    # Generate n random points in d dimensions
    for _ in range(n):
        # Generate a random point in d-dimensional space [-1, 1] for each dimension
        point = [r.uniform(-1, 1) for _ in range(d)]
        
        # Use map and lambda to calculate the sum of squares
        distance_squared = sum(map(lambda x: x**2, point))
        
        # Check if the point lies inside the hypersphere (distance from origin <= 1)
        if distance_squared <= 1:
            inside_sphere += 1

    # Volume approximation for the d-dimensional hypersphere
    volume_approx = (2 ** d) * (inside_sphere / n)  # (2^d) because cube side is [-1, 1]
    return volume_approx 

def hypersphere_exact(n,d):
    """Computes the exact volume of a d-dimensional hypersphere with radius 1."""
    volume_exact = (m.pi**(d/2)) / m.gamma(d/2 + 1)
    return volume_exact
     
     
def main():
    n = 100000
    #d = 2
    #sphere_volume(n,d)
    d_values = [2, 11]  # Dimensionality for the task

    for d in d_values:
        approx_vol = sphere_volume(n, d)
        exact_vol = hypersphere_exact(n, d)
        print(f"Approximate volume of a {d}-dimensional hypersphere: {approx_vol}")
        print(f"Exact volume of a {d}-dimensional hypersphere: {exact_vol}")


if __name__ == '__main__':
	main()
