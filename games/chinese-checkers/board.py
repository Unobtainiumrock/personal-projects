import numpy as np

# class Node(object):
#     def __init__(self):
#         self.top_left = None
#         self.top_right = None
#         self.left = None
#         self.right = None
#         self.bottom_left = None
#         self.bottom_right = None

# Triangular iteration

triangle = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

for i in np.arange(10):
    print(i)
    print('===')
    for j in np.arange(i + 1):
        print(j)
    print('===')
