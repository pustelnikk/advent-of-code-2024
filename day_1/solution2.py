import sys
from collections import Counter
left = []
right = []

for line in sys.stdin:
    if line.strip(): 
        col1, col2 = map(int, line.split())
        left.append(col1)
        right.append(col2)

freq = Counter(right)

score = sum(x * freq.get(x,0) for x in left)
print(f"Similarity score: {score}")