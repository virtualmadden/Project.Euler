class Problem5(object):
    def smallest_multiples(self):
        answer = 0

        # First value that is divisible by 20 and 19.
        result = 380

        while answer == 0:
            if self.divisible(result):
                answer = result

            # Minimum increment given data set.
            result += 380

        return answer

    def divisible(self, result):
        for x in self.divisors:
            if result % x is not 0:
                return False

        return True

    def __init__(self, divisors):
        self.divisors = divisors
