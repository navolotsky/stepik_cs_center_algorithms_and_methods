import sys


def lnis(array):
    if not array:
        return 0, []
    lengths = [1] * len(array)
    for i in range(len(array)):
        for j in range(i):
            if (
                array[j] >= array[i] and
                lengths[j] + 1 > lengths[i]
            ):
                lengths[i] = lengths[j] + 1
    max_len = lengths[0]
    max_len_i = 0
    for i, len_ in enumerate(lengths):
        if len_ > max_len:
            max_len = len_
            max_len_i = i
    indexes = [max_len_i]
    cur_i = max_len_i
    for i in range(max_len_i, -1, -1):
        if (lengths[i] == lengths[cur_i] - 1 and array[i] >= array[cur_i]):
            indexes.append(i)
            cur_i = i
    indexes = [i + 1 for i in reversed(indexes)]
    return max_len, indexes


def main():
    _ = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    length, indexes = lnis(array)
    print(length)
    print(*indexes)


def test():
    assert lnis([5, 3, 4, 4, 2]) == (4, [1, 3, 4, 5])
    assert lnis([3, 6, 7, 12]) == (1, [1])
    assert lnis([3]) == (1, [1])
    assert lnis([]) == (0, [])
    assert lnis([17, 34]) == (1, [1])
    assert lnis([16, 34]) == (1, [1])
    assert lnis([35, 34]) == (2, [1, 2])
    assert lnis([1, 35, 34]) == (2, [2, 3])


def time_test():
    import timeit
    number = 1
    print(timeit.timeit(stmt="lnis(array)",
                        setup="import random; array = [random.randint(0, 10**9) for _ in range(10**4)]", number=number, globals=globals())/number)


if __name__ == "__main__":
    # main()
    # test()
    time_test()
