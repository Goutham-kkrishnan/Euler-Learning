def largestPalindromeProduct(n):
    start = 10 ** (n - 1)
    end = 10 ** n
    largest = 0
    for a in range(end - 1, start - 1, -1):
        if a * a <= largest:
            break
        for b in range(a, start - 1, -1):
            product = a * b
            if product <= largest:
                break
            if str(product) == str(product)[::-1]:
                largest = product
    return largest


n = int(input("Number of digits in each factor: "))
if n < 1:
    print("The number of digits must be 1 or more.")
else:
    print(f"Largest palindrome made from two {n}-digit numbers = {largestPalindromeProduct(n)}")
