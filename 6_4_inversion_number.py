import collections
import sys


def inversion_number(array):
    def merge(left, right):
        nonlocal inversion_counter
        merged = []
        i, j = 0, 0
        left_len = len(left)
        right_len = len(right)
        while i < left_len and j < right_len:
            if left[i] > right[j]:
                inversion_counter += left_len - i
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
        if i >= left_len:
            merged.extend(right[j:])
        else:
            merged.extend(left[i:])
        return merged

    inversion_counter = 0

    if len(array) <= 1:
        return inversion_counter

    q = collections.deque([el] for el in array)
    auxiliary_q = collections.deque()

    while q:
        left = q.popleft()
        right = q.popleft()
        auxiliary_q.append(merge(left, right))
        if len(q) == 1:
            auxiliary_q.append(q.popleft())
            q, auxiliary_q = auxiliary_q, q
        elif not q and len(auxiliary_q) != 1:
            q, auxiliary_q = auxiliary_q, q

    return inversion_counter


def main():
    _ = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    print(inversion_number(array))


if __name__ == "__main__":
    main()
