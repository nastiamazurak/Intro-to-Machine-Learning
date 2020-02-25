import random
import numpy as np
import time

n = 100; 
m = 100;
matrix_a = [[random.randint(1, 1000) for e in range(n)] for e in range(m)]
print("Matrix A: ")
for a in matrix_a:
    print (a)

matrix_b = [[random.randint(1, 1000) for e in range(n)] for e in range(m)]
print("\n Matrix B: ")
for b in matrix_b:
    print(b);

matrix_c = [[random.randint(0, 0) for e in range(n)] for e in range(m)];
start = time.time()
for i in range (n): 
    for j in range (len(matrix_b[0])):
        for k in range (len(matrix_b)):
            matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][i]
end = time.time()
print("\n Result:")
for c in matrix_c:
    print(c);

print ("\n Time: ", end - start )
#using numpy
print ("\n Using Numpy")
#a = np.random.randint(0, 100, (n,m))
#b = np.random.randint(0, 1000, (n,m))
a = np.array(matrix_a)
b =  np.array(matrix_b)
print ("\n Matrix A: ")
print (a)
print ("\n Matrix B: ")
print (b)
print ("\n Result: ")
start_np = time.time()
c = a.dot(b)
end_np = time.time();
print(c);
print("\n Time: ", end_np - start_np)