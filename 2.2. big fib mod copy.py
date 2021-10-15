def fib_mod_using_pisano_period(n, m):
    if n < 2:
        return n % m
    pp, p = 0, 1
    mods = [0, 1]
    pisano_seq = []
    checked_seq_len = 0
    for _ in range(2, n + 1):
        pp, p = p, (p + pp)
        mod = p % m
        mods.append(mod)
        temp = checked_seq_len + 1
        if len(mods) % temp != 0:
            continue
        else:
            checked_seq_len = temp
        for i in range(checked_seq_len, len(mods)):
            if mods[i] != mods[i % checked_seq_len]:
                break
        else:
            pisano_seq = mods[:checked_seq_len]
            break
    if pisano_seq:
        return pisano_seq[n % len(pisano_seq)]
    else:
        return p % m


def main():
    n, m = map(int, input().split())
    r = fib_mod_using_pisano_period(n, m)
    print(r)


if __name__ == '__main__':
    main()
