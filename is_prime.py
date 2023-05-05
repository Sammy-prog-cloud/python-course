def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def get_primes(max_number):
    list_of_primes = []
    for num_1 in range(2, max_number):
        if is_prime(num_1):
            list_of_primes.append(num_1)
    return list_of_primes


max_num_to_check = int(input('Search for primes up to : '))
list_of_primes = get_primes(max_num_to_check)
for prime in list_of_primes:
    print(prime)

