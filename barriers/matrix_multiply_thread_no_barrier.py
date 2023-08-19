import time
import random
from threading import Barrier, Thread
import numpy as np

matrix_size = 500
# matrix_a = [[3, 1, -4],
#            [2, -3, 1],
#            [5, -2, 0]]
# matrix_b = [[1, -2, -1],
#            [0, 5, 4],
#            [-1, -2, 3]]
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]
random.seed(42)
# rand = random.Random()

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = 3 #rand.randint(-5, 5)

def multiply_m(row, matrix_size):
    for col in range(matrix_size):
        for i in range(matrix_size):
            result[row][col] += matrix_a[row][i] * matrix_b[i][col]

start = time.time()
for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size for r in range(matrix_size)]
    threads = []
    for row in range(matrix_size):
        t = Thread(target=multiply_m, args=(row, matrix_size))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

#     for row in range(matrix_size):
#         print(matrix_a[row], matrix_b[row], result[row])
#     print()
end = time.time()
print("Done, time taken", end - start)
print(np.sum(result))

# I compare this one with: matrix_multiply_for_comparison.py
# This way I am not using barriers, cause I am accessing the same array at the same time but always on different indexes.
# This runs faster.
# I would be expecting a different result, cause it could be that 2 threads read the array at nearly the same time,
# and so only one of those 2 got saved, but the sum of the results is the same ...
# It also happened to me that in top the %cpu being used was way up 100% ... how that could be?
# If every thread is accessing only 1 processor. This only for the  matrix_multiply_for_comparison.py script
# (Around 600% of the cpu), but for the matrix_multiply_thread_no_barrier.py this didn't happen, the cpu remain around 100%.
