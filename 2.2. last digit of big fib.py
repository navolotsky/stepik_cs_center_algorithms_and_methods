def last_fib_digit(n):
    if n < 2:
        return n
    pp, p = 0, 1
    for _ in range(2, n + 1):
        pp, p = p, (p + pp) % 10
    return p


def main():
    n = int(input())
    r = last_fib_digit(n)
    print(r)


if __name__ == '__main__':
    main()
