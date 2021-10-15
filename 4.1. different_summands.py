def different_summands(number):
    n = 1
    while True:
        if n >= number - (n + 1) * n / 2:
            n -= 1
            break
        n += 1
    tail = int(number - ((n + 1) * n / 2))
    summands = list(range(1, n + 1))
    summands.append(tail)
    return summands


def new_different_summands(number):
    n = int((-3 + (9 + 8 * number) ** (1 / 2)) / 2)
    if (number - n) * 2 <= (n + 1) * n:
        n -= 1
    tail = int(number - ((n + 1) * n / 2))
    summands = list(range(1, n + 1))
    summands.append(tail)
    return summands


def main():
    num = int(input())
    summands = new_different_summands(num)
    print(len(summands))
    print(*summands)


def test(repeats):
    import random
    used = set()
    for _ in range(repeats):
        while True:
            N = random.randrange(1, 10**9)
            if N not in used:
                used.add(N)
            break
        print(N)
        summands = new_different_summands(N)
        assert N == sum(summands)
        print(*summands)


def timeit(repeats=100):
    import random
    import time
    total_time_old = 0
    total_time_new = 0

    for _ in range(repeats):
        N = random.randrange(1, 10**9)
        start = time.time()
        different_summands(N)
        total_time_old += time.time() - start
        start = time.time()
        new_different_summands(N)
        total_time_new += time.time() - start
    print(
        f'old average {total_time_old/repeats}, new average {total_time_new/repeats}')


if __name__ == "__main__":
    # test(1000)
    main()
