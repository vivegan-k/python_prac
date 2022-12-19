def prime_numbers_till_n(n):
    result = []
    for num in range(2, n):
        if num == 2:
            result.append(num)
        else:
            for i in range(2, num):
                isPrime = False
                if num % i == 0:
                    isPrime = True
                    break
            if not isPrime:
                result.append(num)
    return result

print(prime_numbers_till_n(100))
