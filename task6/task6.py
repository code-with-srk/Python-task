# Read the number of elements in the tuple
n = int(input())

# Read the space-separated integers and convert them to a tuple
t = tuple(map(int, input().split()))

# Compute and print the hash of the tuple
print(hash(t))
