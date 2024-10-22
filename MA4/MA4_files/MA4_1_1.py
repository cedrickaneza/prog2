

"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    # Generate n random points
    for _ in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        
        # Check if the point is inside the circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    # Approximate pi
    pi_approx = 4 * (inside_circle / n)
    
    # Plotting (optional, but part of the task for visualization)
    plt.figure(figsize=(5, 5))
    plt.scatter(x_inside, y_inside, color='red', s=1, label='Inside Circle')
    plt.scatter(x_outside, y_outside, color='blue', s=1, label='Outside Circle')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Approximation of π for n={n}")
    plt.legend()
    plt.savefig(f"monte_carlo_pi_{n}.png")
    plt.show()

    # Return the approximated value of pi for testing
    return pi_approx


    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
