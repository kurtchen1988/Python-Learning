import random
li = [random.random() for i in range(100000)]
%timeit li.sort()