import sys


def min_calc_ops(number):
    ops = {1: 0}
    prevs = {}
    for i in range(1, number):
        for i_x in [i * 3, i * 2, i + 1]:
            if i_x > number:
                continue
            if ops.get(i_x) is None or ops[i] + 1 < ops[i_x]:
                ops[i_x] = ops[i] + 1
                prevs[i_x] = i
    nums = [number]
    if prevs:
        k = prevs[number]
        while k != 1:
            nums.append(k)
            k = prevs[k]
        nums.append(1)
        nums.reverse()
    return ops[number], nums


def main():
    number = int(sys.stdin.readline().rstrip())
    k, nums = min_calc_ops(number)
    print(k)
    print(*nums)


def test():
    assert min_calc_ops(1) == (0, [1])
    assert min_calc_ops(5) == (3, [1, 2, 4, 5])
    assert min_calc_ops(96234) == (
        14, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])


def time_test(number=1):
    import random
    import timeit
    print(timeit.timeit(stmt="min_calc_ops(number)", setup=(
        "number = random.randint(10**4, 10**5)"),
        number=number,
        globals={**globals(), **locals()}
    )/number)


if __name__ == "__main__":
    # main()
    test()
    # time_test(100)
