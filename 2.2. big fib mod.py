def fib_mod_using_pisano_period(n, m):
    if n < 2:
        return n % m
    ppm, pm = 0, 1 % m
    mods = [0, 1]
    pisano_seq = []
    for _ in range(2, n + 1):
        ppm, pm = pm, (pm + ppm) % m
        mods.append(pm)
        if ppm == 0 and pm == 1:
            pisano_seq = mods[:-2]
            break
    if pisano_seq:
        return pisano_seq[n % len(pisano_seq)]
    else:
        return pm


def main():
    n, m = map(int, input().split())
    r = fib_mod_using_pisano_period(n, m)
    print(r)


if __name__ == '__main__':
    main()
