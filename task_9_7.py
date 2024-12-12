def is_prime(func):
    def wrapper(a, b, c):
        d = a + b + c
        k = True
        for i in range(2, d - 1):
            if d % i == 0:
                k = False
        if k:
            print('Простое')
        else:
            print('Составное')
        return d

    return wrapper


@is_prime
def sum_three(a, b, c):
    d = a + b + c
    return d


result = sum_three(2, 3, 6)
print(result)
