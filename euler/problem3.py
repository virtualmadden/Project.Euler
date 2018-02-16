import math


class Problem3(object):
    def largest_prime(self):
        answer = 0

        divisor = 2
        new_limit = self.upper_limit

        while new_limit > divisor:
            result = self.upper_limit % divisor

            if result is 0 and self.is_prime(divisor):
                answer = divisor

            new_limit = math.floor(self.upper_limit / divisor)

            divisor += 1

        return answer

    @staticmethod
    def is_prime(divisor):
        if divisor % 2 is 0:
            return False
        else:
            midpoint = math.floor(divisor / 2)

            for x in range(3, midpoint):
                if divisor % x is 0:
                    return False

        return True

    def __init__(self, limit):
        self.upper_limit = limit
