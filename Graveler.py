import numpy as np
from tqdm import tqdm
from datetime import datetime
start = datetime.now()

best = 231

repeats = 100
rolls = 10_000_000
length_of_run = 231

for _ in range(repeats):
    array = np.random.randint(0, 4, size=(rolls, length_of_run), dtype=np.int8)


    
    curr = np.min(np.count_nonzero(array, axis = 1))
    if curr < best:
        best = curr
        if best < 54:
            break

best = 231 - best

print(f"Highest Roll: {best}")
print(f"Number of Roll Sessions: {rolls * repeats}")
print(f"Took {datetime.now() - start} seconds to finish.")