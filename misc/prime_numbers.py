def is_prime_number(num = 0):
    if num == 0: 
        return False
    if num == 1:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

input = 10
#output = is_prime_number(input)
for i in range(100):
    output = is_prime_number(i)
    if output:
        print(f"{i} is a prime number*")
    else:
        print(f"{i} is not a prime number")

