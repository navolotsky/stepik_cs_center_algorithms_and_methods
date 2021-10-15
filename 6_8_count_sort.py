import sys


def count_sort(array):
    min_num = max_num = array[0]
    for a in array:
        if a < min_num:
            min_num = a
        elif a > max_num:
            max_num = a
    result = [0] * len(array)
    aux = [0] * (max_num - min_num + 1)
    offset = 0 - min_num
    for a in array:
        aux[a + offset] += 1
    for i in range(1 + min_num + offset, 1 + max_num + offset):
        aux[i] += aux[i - 1]
    for a in reversed(array):
        result[aux[a + offset] - 1] = a
        aux[a + offset] -= 1
    return result


def main():
    _ = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    print(*count_sort(array))


if __name__ == "__main__":
    main()
