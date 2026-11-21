def largestPrimeFactor(number):
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            number //= divisor
        else:
            divisor += 1
    return number


number = int(input("Find the largest prime factor of: "))
if number < 2:
    print("The number must be 2 or more.")
else:
    print(f"Largest prime factor of {number} = {largestPrimeFactor(number)}")
