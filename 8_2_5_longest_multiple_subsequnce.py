import sys


def lis_with_div(array):
    if not array:
        return 0
    length = len(array)
    lis_lengths = [1] * length
    for i in range(length):
        for j in range(i):
            if (
                array[i] % array[j] == 0 and
                lis_lengths[j] + 1 > lis_lengths[i]
            ):
                lis_lengths[i] = lis_lengths[j] + 1
    ans = lis_lengths[0]
    for l in lis_lengths:
        if l > ans:
            ans = l
    return ans


def main():
    _ = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    result = lis_with_div(array)
    print(result)


def test():
    assert lis_with_div([3, 6, 7, 12]) == 3
    assert lis_with_div([3]) == 1
    assert lis_with_div([]) == 0
    assert lis_with_div([17, 34]) == 2
    assert lis_with_div([16, 34]) == 1


def time_test():
    import timeit
    number = 100
    print(timeit.timeit(stmt="lis_with_div(array)",
                        setup="import random; array = [random.randint(1, 2*10**9) for _ in range(10**3)]", number=number, globals=globals())/number)


if __name__ == "__main__":
    # main()
    # test()
    time_test()
