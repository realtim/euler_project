#!/usr/bin/env python
# -*- coding=utf-8 -*-

import itertools

# definition taken from wikipedia
# check numbers up to the square root of n
# (checking only primes is enough actually but we don't have a list of primes)
def isPrime(n):
    if n % 2 == 0:
        return False

    # Reduce number of iterations by skipping even numbers (they are nonprime anyway)
    for x in xrange(3,int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True	

# find the greatest pandigital prime number
def greatest_pandigital_prime_number():
    powers_of_ten = [ 10**n for n in xrange(0,9) ]
    last_digits_of_a_nonprime = set([0,2,4,5,6,8])

    # iterate pandigital numbers from long to short, from big to small, return first prime number
    for max_digits in xrange(9,1,-1):

        # iterator of biggest pandigital number of max_digits digits
        biggest_number_iterator = xrange(max_digits, 0, -1)

        # divisible by 3 (nonprime)
        # https://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_3_or_9
        if sum(biggest_number_iterator) % 3 == 0:
            continue

        # iterate permutations of digits from biggest to smallest
        for digits_tuple in itertools.permutations(biggest_number_iterator):

            # divisible by 2 or 5 (nonprime)
            # https://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_2
            # https://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_5
            if digits_tuple[-1] in last_digits_of_a_nonprime:
                continue

            # generate number from digits
            number = 0
            for i, x in enumerate(digits_tuple):
                number += powers_of_ten[max_digits-i-1]*x

            if isPrime(number):
                return number

print "the greatest pandigital prime number is: ", greatest_pandigital_prime_number()
