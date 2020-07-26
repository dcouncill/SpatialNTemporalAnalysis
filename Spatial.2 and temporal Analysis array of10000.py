from numpy import random
import numpy as arr
from collections import Counter
arr = random.randint(10000, size = 10000)
print(Counter(arr))

import timeit
Trial_Once= """from numpy import random
import numpy as arr
from collections import Counter
arr = random.randint(10000, size = 10000)
print(Counter(arr)) """
print(timeit.timeit(Trial_Once, number = 10000))

import os
import psutil
process = psutil.Process(os.getpid())
print(process.memory_info()[0])
