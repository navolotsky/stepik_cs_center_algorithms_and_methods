import sys


def max_stairs_sum_td(stairs):
    sums = {}

    def mss(i):
        if i == 0:
            return stairs[i]
        elif i == 1:
            return max(stairs[i], stairs[i] + mss(i - 1))
        s_i = sums.get(i)
        if s_i is None:
            s_i = stairs[i] + max(mss(i - 1), mss(i - 2))
            sums[i] = s_i
        return s_i
    return mss(len(stairs) - 1)


def main():
    _ = sys.stdin.readline()
    stairs = list(map(int, sys.stdin.readline().split()))
    print(max_stairs_sum_td(stairs))


def test():
    assert max_stairs_sum_td([1, 2]) == 3
    assert max_stairs_sum_td([2, -1]) == 1
    assert max_stairs_sum_td([-1, 2, 1]) == 3
    assert max_stairs_sum_td([-5, -3, -1]) == -4
    assert max_stairs_sum_td([-1, -3, -1]) == -2
    assert max_stairs_sum_td([-1, 1, -1]) == 0
    assert max_stairs_sum_td([-98]) == -98


def time_test(number=1):
    import random
    import timeit
    import gc
    print(timeit.timeit(stmt="max_stairs_sum_td(stairs)", setup=(
        "stairs = list(random.randint(-10**4, 10**4) for _ in range(10**2))"),
        number=number,
        globals={**globals(), **locals()}
    )/number)


if __name__ == "__main__":
    main()
    # test()
    # time_test(100)
