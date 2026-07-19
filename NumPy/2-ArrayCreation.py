import numpy as np

onesSingleD = np.ones(4)
print(onesSingleD)
print()

onesStr = np.ones((5, 10), dtype=str)
print(onesStr)
print()

zeros = np.zeros((3, 5), int)
print(zeros)
print()

arange = np.arange(0, 101, 25)
print(arange)
print()

linspace = np.linspace(start=25, stop=100, num=4, dtype=str)
print(linspace)
print()

reshape = np.arange(1, 20, step=2).reshape(2, 5)
print(reshape)
print()

identity = np.identity(5)
print(identity)
print()