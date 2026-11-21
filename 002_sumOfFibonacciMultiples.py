def fibonacciMultiplesSum(divisor, limit):
    total = 0
    a, b = 1, 2
    while a <= limit:
        if a % divisor == 0:
            total += a
        a, b = b, a + b
    return total


divisor = int(input("Add the Fibonacci terms divisible by: "))
limit = int(input("Terms up to (and including): "))
if divisor < 1:
    print("The divisor must be 1 or more.")
else:
    total = fibonacciMultiplesSum(divisor, limit)
    print(f"Sum of the Fibonacci terms divisible by {divisor} that do not exceed {limit} = {total}")
