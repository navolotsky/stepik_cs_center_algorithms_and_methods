def fib(n):
    if n < 2:
        return n
    pp, p = 0, 1
    for i in range(2, n+1):
        pp, p = p, p + pp
    return p


def main():
    n = int(input())
    r = fib(n)
    print(r)


if __name__ == '__main__':
    main()
