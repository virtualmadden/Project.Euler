class Problem2(object):
    def fibonacci(self):
        answer = 0

        prev_val = 0
        next_val = 1

        while next_val < self.upper_limit:
            total = prev_val + next_val

            if total % 2 is 0:
                answer += total

            next_val = prev_val
            prev_val = total

        return answer

    def __init__(self, limit):
        self.upper_limit = limit
