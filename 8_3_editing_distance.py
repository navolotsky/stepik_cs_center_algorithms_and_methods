import sys


def editing_distance(before, after):
    n = len(before)
    m = len(after)
    prev = list(range(m + 1))
    cur = [None] * (m + 1)
    for i in range(1, n + 1):
        cur[0] = i
        for j in range(1, m + 1):
            cur[j] = min(
                prev[j] + 1,
                cur[j - 1] + 1,
                prev[j - 1] + (1 if before[i - 1] != after[j - 1] else 0)
            )
        prev, cur = cur, prev
    return prev[-1]


def test():
    assert editing_distance('short', 'ports') == 3
    assert editing_distance('distance', 'editing') == 5


def time_test():
    import timeit
    import random
    import string
    number = 1000
    print(
        timeit.timeit(
            stmt="editing_distance(before, after)",
            setup=(
                "import random;"
                "before=''.join(random.SystemRandom().choices(string.ascii_lowercase, k=10**2));"
                "after=''.join(random.SystemRandom().choices(string.ascii_lowercase, k=10**2))"),
            globals={**globals(), **locals()},
            number=number
        )/number
    )


def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    print(editing_distance(a, b))


if __name__ == "__main__":
    main()
    # test()
    # time_test()
