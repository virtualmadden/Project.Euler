class Problem6(object):
    def square_difference(self):
        answer = 0

        for x in self.numbers:
            answer += x

        answer = answer**2

        for x in self.numbers:
            answer -= x**2

        return answer

    def __init__(self, numbers):
        self.numbers = numbers
