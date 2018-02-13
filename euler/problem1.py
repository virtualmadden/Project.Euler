class Problem1(object):
    def multiples(self):
        answer = 0

        for x in range(0, self.upper_limit):
            if x % 3 is 0:
                answer += x
            elif x % 5 is 0:
                answer += x

        return answer

    def __init__(self, limit):
        self.upper_limit = limit
