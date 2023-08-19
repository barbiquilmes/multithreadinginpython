import time
import os
import random
import numpy as np
from threading import Barrier, Thread

matrix_size = 500

matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]
random.seed(42)
rand = random.Random()
work_start = Barrier(matrix_size + 1)
work_complete = Barrier(matrix_size + 1)

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = 3 #rand.randint(-5, 5)

def work_out_row(row):
    #print(f'ROW: Before true, row {row}')
    while True:
        #print(f'ROW: before wait work_start, row {row}')
        work_start.wait()
        #print(f'ROW: after wait work_start, row {row}')
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
        #print(f'ROW: before wait work_complete, row {row}')
        work_complete.wait()
        #print(f'ROW: after wait work_complete, row {row}')


for row in range(matrix_size):
    #print('ITER: before 31 ' + str(row))
    Thread(target=work_out_row, args=([row])).start()
    #print('ITER: after 31 ' + str(row))

start = time.time()
for t in range(10):
    #print(f"\nRange {t}\n")
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size for r in range(matrix_size)]
    #print('GRAL: Before Gral work_start')
    work_start.wait()
    #print('GRAL: After Gral work_start')
    work_complete.wait()
    #print('GRAL: After Gral work_complete')
    time.sleep(0.5)
end = time.time()
print("Done, time taken", end - start)
print(np.sum(result))
os._exit(1)