import sys


def lnis(array):
    arr_len = len(array)
    predecessors = [None] * arr_len
    found_lnis_indexes = [None] * (arr_len + 1)

    cur_lnis_len = 0
    for i in range(arr_len):
        lo = 1
        hi = cur_lnis_len
        while lo <= hi:
            mid = (lo + hi) // 2
            if array[found_lnis_indexes[mid]] >= array[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        new_lnis_len = lo

        predecessors[i] = found_lnis_indexes[new_lnis_len - 1]
        found_lnis_indexes[new_lnis_len] = i

        if new_lnis_len > cur_lnis_len:
            cur_lnis_len = new_lnis_len

    indexes = []
    k = found_lnis_indexes[cur_lnis_len]
    for _ in range(cur_lnis_len):
        indexes.append(k)
        k = predecessors[k]
    indexes = [i + 1 for i in reversed(indexes)]
    return cur_lnis_len, indexes


def main():
    _ = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    length, indexes = lnis(array)
    print(length)
    print(*indexes)


def test():
    assert lnis([5, 3, 4, 4, 2]) == (4, [1, 3, 4, 5])
    assert lnis([3, 6, 7, 12]) == (1, [4])
    assert lnis([3]) == (1, [1])
    assert lnis([]) == (0, [])
    assert lnis([17, 34]) == (1, [2])
    assert lnis([16, 34]) == (1, [2])
    assert lnis([35, 34]) == (2, [1, 2])
    assert lnis([1, 35, 34]) == (2, [2, 3])


def time_test():
    import timeit
    number = 15
    print(timeit.timeit(stmt="lnis(array)",
                        setup="import random; array = [random.randint(0, 10**9) for _ in range(10**5)]", number=number, globals=globals())/number)


if __name__ == "__main__":
    main()
    # test()
    # time_test()
