import collections
import itertools
import math
import statistics

# Counter
from collections import Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count.most_common(2))     # [('apple', 3), ('banana', 2)]

# Defaultdict
from collections import defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")

# Named tuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)

# itertools
from itertools import permutations, combinations
print(list(permutations([1, 2, 3], 2)))
print(list(combinations([1, 2, 3], 2)))

# math
print(math.factorial(5))        # 120
print(math.gcd(48, 18))         # 6
print(math.isqrt(17))           # 4 (integer square root)

# statistics
data = [2, 3, 4, 5, 6, 7, 8]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.stdev(data))
