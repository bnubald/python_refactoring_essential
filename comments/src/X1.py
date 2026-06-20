class X1:

    @staticmethod
    def m(lower_bound, upper_bound):
        accumulated_sum = 0

        for i in range(lower_bound, upper_bound + 1):
            # Add square of each number in the range
            accumulated_sum += X1.square(i)

        return accumulated_sum

    @staticmethod
    def square(value):
        return value * value