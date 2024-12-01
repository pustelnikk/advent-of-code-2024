import sys

left = []
right = []

for line in sys.stdin:
    if line.strip(): 
        col1, col2 = map(int, line.split())
        left.append(col1)
        right.append(col2)

left.sort()
right.sort()

sum = 0

for i,v in enumerate(left):
    sum += abs(v-right[i])

print(f"The sum is: {sum}")

