class SquareCalculator:

    @staticmethod
    def sum_of_squares(lower_bound, upper_bound):
        accumulated_sum = 0

        for i in range(lower_bound, upper_bound + 1):
            accumulated_sum += i * i

        return accumulated_sum

