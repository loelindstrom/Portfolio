import tkinter as tk
import random
import numpy as np

x = np.zeros((20,10))

x[1,6] = 1
x[2,7] = 1
x[3,8] = 1

rows, columns = np.where(x == 1)
print(rows)
print(columns)

print(list(range(0, 6, 2)))
print(list(range(1, 6, 2)))

t1 = [1,2,3]
t2 = [7,8,9]

t3 = [(2, 2), (2, 8)]
for pair in t3:
    if pair not in zip(t1, t2):
        print(pair, "Not inside")
    else:
        print(pair, "Inside")


