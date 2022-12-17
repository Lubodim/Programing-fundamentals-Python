number = int(input())
is_prime = True
for prime in range(2, number):
    if number % prime == 0:
        is_prime = False
print(is_prime)
