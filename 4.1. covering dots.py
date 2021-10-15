def covering_dots(segments):
    if not segments:
        return []
    sorted_segments = sorted(segments, key=lambda x: x[-1])
    dots = [sorted_segments[0][-1]]
    for segment in sorted_segments:
        if dots[-1] < segment[0]:
            dots.append(segment[-1])
    return dots


def main():
    n = int(input())
    s = []
    for _ in range(n):
        a, b = map(int, input().split())
        s.append((a, b))
    dots = covering_dots(s)
    print(len(dots))
    print(*dots)


if __name__ == "__main__":
    main()
