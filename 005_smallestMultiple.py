def smallestMultiple(start, end):
    multiple = 1
    for i in range(start, end + 1):
        candidate = multiple
        while candidate % i != 0:
            candidate += multiple
        multiple = candidate
    return multiple


start, end = map(int, input("Range of numbers (two numbers, space separated): ").split())
if start < 1 or end < start:
    print("Enter two whole numbers where 1 <= first <= second.")
else:
    print(f"Smallest number divisible by every number from {start} to {end} = {smallestMultiple(start, end)}")
