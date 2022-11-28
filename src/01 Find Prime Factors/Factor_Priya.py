def findPrimeFactorOf(number):
    divisor = 2
    factors = []
    while (divisor <= number):
        if(number % divisor == 0):
            factors.append(divisor)
            number //= divisor
        else:
            divisor +=1
    return factors

print(findPrimeFactorOf(130))

