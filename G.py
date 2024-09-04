import random
import multiprocessing
import time

number_of_runs = 1_000_000_000

number_of_concurrent = multiprocessing.cpu_count()
args = [0 for _ in range(0, number_of_runs)]

def count_values(_):
    # Generate 231 random integers between 1 and 4
    rolls = [random.randint(1, 4) for _ in range(231)]
    
    # Count occurrences of each value
    counts = {value: rolls.count(value) for value in range(1, 5)}
    
    # Return the counts
    return max(counts.values())

if __name__ == '__main__':
    multiprocessing.freeze_support()
    Pool = multiprocessing.Pool(processes = number_of_concurrent)

    start = time.time()
    res = max(Pool.map(count_values, args))
    end = time.time()
    
    print("Highest Ones Roll:", res)
    print("Number of Roll Sessions:", number_of_runs)
    print("Time Taken(seconds):", end - start)