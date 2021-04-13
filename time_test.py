from timeit import *
from Main import *


print(euclid_algorithm(4181, 6765))
print(min(repeat("euclid_algorithm(40902, 24140)", number=1, repeat=3, globals=globals())))
print(min(repeat("euclid_algorithm(4181, 6)", number=1, repeat=3, globals=globals())))
print(min(repeat("euclid_algorithm(1, 1)", number=1, repeat=3, globals=globals())))
