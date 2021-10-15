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


if __name__ == "__main__":
    main()
