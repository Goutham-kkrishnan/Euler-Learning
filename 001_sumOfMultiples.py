def multiples_a_and_b(a, b, number):
    def sumOfMultiples(divisor):
        n= (number-1)//divisor
        return divisor * n * (n + 1) // 2
    return sumOfMultiples(a) + sumOfMultiples(b) - sumOfMultiples(a*b)
    


a, b = map(int, input("Enter Two numbers (space separated): ").split())
limit = int(input("Enter the Limit"))
sum = multiples_a_and_b(a,b,)
print(f"Sum of multiples of {a} and {b} below {limit} = {sum}")