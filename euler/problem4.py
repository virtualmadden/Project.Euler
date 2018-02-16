class Problem4(object):
    def palindrome(self):
        answer = 0

        for x in range(self.lower_bound, self.upper_bound):
            for y in range(self.lower_bound, self.upper_bound):
                result = x * y

                if self.is_palindrome(result) and result > answer:
                    answer = result

        return answer

    @staticmethod
    def is_palindrome(result):
        int_string = str(result)
        int_string_reverse = int_string[::-1]

        if int_string == int_string_reverse:
            return True

        return False

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
