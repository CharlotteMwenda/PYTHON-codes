set1 = set(map(int, input("Enter the first set of integers separated by spaces: ").split()))
set2 = set(map(int, input("Enter the second set of integers separated by spaces: ").split()))

common_elements = set1.intersection(set2)

print(f"Common elements: {common_elements}")