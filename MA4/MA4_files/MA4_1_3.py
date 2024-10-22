
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import time
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter as pc

# Function to approximate the volume of a d-dimensional hypersphere
def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    inside_sphere = 0
    for _ in range(n):
        point = [r.uniform(-1, 1) for _ in range(d)]
        distance_squared = sum(map(lambda x: x**2, point))
        if distance_squared <= 1:
            inside_sphere += 1
    volume_approx = (2 ** d) * (inside_sphere / n)
    return volume_approx

def hypersphere_exact(n,d):
    return

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    with ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, n // np, d) for _ in range(np)]
        results = [f.result() for f in futures]
    
    # Average the results from each process
    avg_volume = sum(results) / len(results)
    return avg_volume

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    chunk_size = n // np
    with ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, chunk_size, d) for _ in range(np)]
        results = [f.result() for f in futures]
    
    # Aggregate the results from each process
    total_volume = sum(results) / len(results)
    return total_volume

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 8

    # Sequential version running in a loop
    print("Running sequential version...")
    start = pc()
    for y in range(np):
        sphere_volume(n, d)
    stop = pc()
    seq = stop - start
    print(f"Time for sequential version: {seq} seconds")

    # Parallel version 1
    print("Running parallel version 1...")
    start = pc()
    sphere_volume_parallel1(n, d, np)
    stop = pc()
    par1 = stop - start
    print(f"Time for parallel version 1: {par1} seconds")

    # Parallel version 2
    print("Running parallel version 2...")
    start = pc()
    sphere_volume_parallel2(n, d, np)
    stop = pc()
    par2 = stop - start
    print(f"Time for parallel version 2: {par2} seconds")

    for y in range (10):
        sphere_volume(n,d)


if __name__ == '__main__':
	main()
