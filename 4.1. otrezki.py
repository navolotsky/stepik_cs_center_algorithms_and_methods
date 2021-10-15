def max_independets(segments):
    if not segments:
        return 0, []
    sorted_segments = sorted(segments, key=lambda x: x[-1])
    count = 1
    res = [sorted_segments[0]]
    for segment in sorted_segments:
        if segment[0] < res[-1][-1]:
            continue
        else:
            count += 1
            res.append(segment)
    return count, res


def main():
    n = int(input())
    s = []
    for _ in range(n):
        a, b = map(int, input().split())
        s.append(tuple([a, b]))
    num, res = max_independets(s)
    print(num)
    for x in res:
        print(*x)


if __name__ == "__main__":
    main()
