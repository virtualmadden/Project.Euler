import math


class Problem7(object):
    def primes(self):
        answer = 0

        prime_count = 0

        x = 1

        while prime_count < self.limit:
            if self.is_prime(x):
                prime_count += 1
                answer = x

            x += 2

        return answer

    @staticmethod
    def is_prime(potential_prime):
        divisor = 3

        new_limit = math.floor(potential_prime / divisor)

        while new_limit >= divisor:
            if potential_prime % divisor is 0:
                return False

            divisor += 2

            new_limit = math.floor(potential_prime / divisor)

        return True

    def __init__(self, limit):
        self.limit = limit
