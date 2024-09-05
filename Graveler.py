import numpy as np
from tqdm import tqdm
from datetime import datetime
start = datetime.now()

best = 231

rolls = 1_000_000
length_of_run = 231

array = np.random.randint(0, 4, size=(rolls, length_of_run), dtype=np.int8)

with tqdm(total=rolls) as pbar:
    for array in array:
        curr = np.count_nonzero(array)
        if curr < best:
            best = curr
        pbar.update()
        if best < 54:
            break

best = 231 - best

print(f"Highest Roll: {best}")
print(f"Number of Roll Sessions: {rolls}")
print(f"Took {datetime.now() - start} seconds to finish.")