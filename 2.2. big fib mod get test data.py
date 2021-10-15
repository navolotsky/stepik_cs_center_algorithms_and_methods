def fib(n, m):
    if n < 2:
        return n % m
    pp, p = 0, 1
    for _ in range(2, n + 1):
        pp, p = p, p + pp
    return p % m


def main():
    n, m = map(int, input().split())
    r = fib(n, m)
    print(r)


if __name__ == '__main__':
    main()
