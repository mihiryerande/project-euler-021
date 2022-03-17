# Problem 21:
#     Amicable Numbers
#
# Description:
#     Let d(n) be defined as the sum of proper divisors of n
#       (numbers less than n which divide evenly into n).
#     If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
#       and each of a and b are called amicable numbers.
#
#     For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
#       therefore d(220) = 284.
#     The proper divisors of 284 are 1, 2, 4, 71 and 142;
#       so d(284) = 220.
#
#     Evaluate the sum of all the amicable numbers under 10000.

from math import floor, sqrt


def main(n):
    """
    Returns the sum of all amicable numbers less than `n`,
      and a list of the actual amicable pairs.

    Args:
        n (int): Natural number

    Returns:
        Sum of amicable numbers less than `n`,
          and list of amicable pairs.
    """
    assert type(n) == int and n > 0

    # Maintain mapping of numbers to divisor sums as an array
    # Include 1 at beginning, and skip while accumulating
    div_sums = [1 for _ in range(n-1)]
    div_sums[0] = 0

    # Iterate through possible pairs of factors and accumulate at relevant multiples
    mid = floor(sqrt(n-1))
    for f1 in range(2, mid+1):  # Lower divisor
        for f2 in range(f1, n//f1):  # Upper divisor
            m = f1 * f2  # Multiple
            div_sums[m-1] += f1
            div_sums[m-1] += f2
        # Don't double-count divisor f1 for its square
        div_sums[f1**2-1] -= f1

    # Collect amicable pairs, using lower of the pair
    am_sum = 0
    am_pairs = []
    for a in range(1, n):
        b = div_sums[a-1]
        if n > b > a == div_sums[b-1]:
            am_sum += a
            am_sum += b
            am_pairs.append((a, b))
    return am_sum, am_pairs


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    amicable_sum, amicable_pairs = main(num)
    print('Sum of all amicable numbers less than {}:'.format(num))
    print('  {}'.format(amicable_sum))
    print('Amicable pairs less than {}:'.format(num))
    print('  {}'.format('\n  '.join(map(lambda p: '{} ⇔ {}'.format(p[0], p[1]), amicable_pairs))))
