import multiprocessing
import time
from numpy.random import Generator, PCG64
import numpy as np

number_of_runs = 10_000_000
number_of_reps = 100


number_of_concurrent = multiprocessing.cpu_count()
args = [0 for _ in range(0, number_of_runs)]

rng = Generator(PCG64())
def count_values(_):
    return np.count_nonzero(rng.integers(4, size=231) == 0)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    Pool = multiprocessing.Pool(processes = number_of_concurrent)
    res = 0
    start = time.time()
    for _ in range(number_of_reps):
        res = max(res, max(Pool.map(count_values, args)))
    end = time.time()

    print("Highest Ones Roll:", res)
    print("Number of Roll Sessions:", number_of_runs)
    print("Time Taken(seconds):", end - start)