"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be a positive integer")
    
    prime_list = []
    num = 2  # Start with the first prime number
    
    while len(prime_list) < number_of_primes:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    
    return prime_list
