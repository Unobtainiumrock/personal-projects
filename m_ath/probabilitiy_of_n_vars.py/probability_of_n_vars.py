# Given below is an example outlining the general pattern for computing the expectation of a random variable represented as an equation of 
# two (or can be extended to n) random variables.

# Example (sampling with replacement): 
# If we have the random variable Z = X - Y, where X and Y are random variables from the same distribution. Let
# X and Y can both be representative of two randomly sampled (with replacement) people from the same distribution.

# Sample size is two. The random variable Z represents the difference in age between these two random people.

# If not computing expectation by using the linearity of expectation, we can do the folllowing:

# 1) Take the cartesian product of the discrete set x with itself. The discrete set x is the set of possible
# values that the R.V. X can take on.

# For example, if the data set has 4 people let x = [50, 52, 51, 50] be an array containing the ages of each person
# obtained through random sampling.

from itertools import product
import numpy as np

ages = [50, 52, 51, 50]
cartesian_product = list(product(ages, repeat = 2)) # Will be of size n * (n - 1) + n = n^2

# Each integer increment of repeat = k corresponds to sampling with replacement events. In our example we wanted the difference in age between two people.

# If we instead had 3 random variables, we would do repeat = 3

print('Cartesian product of the set with itself:', cartesian_product)
print('Size of cartesian product:', len(cartesian_product))

# print(len(list(product(ages, repeat = 3)))) # In this case, the size of the product is n^k, for when computing on arbitrary repeat sizes.

# 2) Define our R.V function in terms of all our random variables. We could get really creative and generalize it 

def fn(X, Y):# For our specific example
    return np.abs(X - Y)

def general_form(*args):
    # Do whatever you want with a function on an collection of an arandom variables.
    ...

# 3 Build an object containing a mapping of the R.V. function's distinc outputs as proportions of all possible distinct outputs

def mapper(p, f):
    d = {}

# Building counts of distinct variables
    for i in p:
        k = f(i[0], i[1])
        if not k in d:
            d[k] = 1
        else:
            d[k] += 1

# Convert counts of distinc variables into proportions. 
    for k, v in d.items():
        d[k] = v / len(p)

    return d

print(mapper(cartesian_product, fn))