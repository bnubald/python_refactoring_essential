class X1:

    @staticmethod
    def m(lower_bound, upper_bound):
        p = 0

        for i in range(lower_bound, upper_bound + 1):
            # Add square of each number in the range
            p += X1.square(i)

        # Return accumulated sum
        return p

    @staticmethod
    def square(k):
        return k * k