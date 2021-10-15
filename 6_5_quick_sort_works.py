import collections
import random
import sys


def quick_sort(array, l=None, r=None):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    def partition(l, r):
        m = random.randint(l, r)
        x = array[m]
        swap(l, m)
        j = l
        for i in range(l + 1, r + 1):
            if array[i] <= x:
                j += 1
                swap(j, i)
        swap(l, j)
        return j

    def qs(array, l, r):
        while l < r:
            m = partition(l, r)
            if r - m > m - l:
                qs(array, l, m - 1)
                l = m + 1
            else:
                qs(array, m + 1, r)
                r = m - 1

    def partition3(l, r):
        m = random.randint(l, r)
        x = array[m]
        swap(l, m)
        j = l
        for i in range(l + 1, r + 1):
            if array[i] <= x:
                j += 1
                swap(j, i)
        k = l - 1
        for i in range(l, j + 1):
            if array[i] < x:
                k += 1
                swap(k, i)
        return k + 1, j

    def qs3(array, l, r):
        while l < r:
            k, m = partition3(l, r)
            if r - m > k - l:
                qs3(array, l, k - 1)
                l = m + 1
            else:
                qs3(array, m + 1, r)
                r = k - 1
        return array

    if l is None:
        l = 0
    if r is None:
        r = len(array) - 1

    # result = qs(array, l, r)
    result = qs3(array, l, r)

    return array


def points_in_segments(segments, points):
    before_point = [seg[1] for seg in segments]
    after_point = [seg[0] for seg in segments]
    quick_sort(before_point)
    quick_sort(after_point)

    segments_number_for_point = [len(segments)] * len(points)

    seg_len = len(segments)
    seg_len_end = seg_len - 1
    for i, point in enumerate(points):
        l = 0
        r = seg_len_end
        while True:
            m = (l + r) // 2
            if m < seg_len_end and before_point[m] < point <= before_point[m + 1]:
                segments_number_for_point[i] -= m + 1
                break
            elif before_point[m] >= point:
                if l > r:
                    break
                r = m - 1
            elif m < seg_len_end and point > before_point[m + 1]:
                if l > r:
                    segments_number_for_point[i] -= seg_len
                    break
                l = m + 1
            elif m == seg_len_end and point > before_point[m]:
                segments_number_for_point[i] -= seg_len
                break
            else:
                break

    for i, point in enumerate(points):
        l = 0
        r = seg_len_end
        while True:
            m = (l + r) // 2
            if m < seg_len_end and after_point[m] <= point < after_point[m + 1]:
                segments_number_for_point[i] -= seg_len_end - m
                break
            elif after_point[m] > point:
                if l > r:
                    segments_number_for_point[i] -= seg_len
                    break
                r = m - 1
            elif m < seg_len_end and point >= after_point[m + 1]:
                if l > r:
                    break
                l = m + 1
            else:
                break

    return segments_number_for_point

def true_algo(segments, points):
    segments_number_for_point_true = []
    for point in points:
        counter = 0
        for a, b in segments:
            if a <= point <= b:
                counter += 1
        segments_number_for_point_true.append(counter)
    return segments_number_for_point_true

def main():
    n, _ = map(int, sys.stdin.readline().split())
    segments = [tuple(map(int, sys.stdin.readline().split()))
                for _ in range(n)]
    points = list(map(int, sys.stdin.readline().split()))
    print(*points_in_segments(segments, points))

def tests():
    n, _ = 2, 3
    tests = [
        [
            [(0, 5), (7, 10)],
            [1, 6, 11],
            [1, 0, 0]
        ],
        [
            [(1, 8), (2, 10), (3, 11), (6, 9)],
            [5, 0, 7, 4],
            [3, 0, 4, 3]
        ],
        [
            [(1, 8), (2, 10), (7, 7), (3, 11), (6, 9)],
            [5, 0, 7, 4],
            [3, 0, 5, 3]
        ],
        [
            [(-1, 3)],
            [-1],
            [1]
        ]
    ]
    for i, (*args, true_result) in enumerate(tests):
        if true_result is None:
            import copy
            true_result = true_algo(*copy.deepcopy(args))
            print(f"True result for #{i}: {true_result}")

        result = points_in_segments(*args)
        assert true_result == result, (f"#{i}", result)
        print(f"test #{i} passed!")

def random_tests(how_much=1, max_number=5*10**4):
    import copy
    for _ in range(how_much):
        segments = []
        points = []
        start = 1
        # max_number = 5*10**4
        # start = max_number - 1
        # max_number = 500
        for i in range(start, max_number+1):
            a = random.randint(-10, 10)
            b = random.randint(a, 10)
            segments.append((a, b))
            # points.append(10**8)
            points.append(random.randint(-10, 10))

            args = segments, points
                
        true_result = true_algo(*copy.deepcopy(args))
        print(f"True result for #{i}: {true_result}")

        result = points_in_segments(*args)
        assert true_result == result, (f"#{i}", result)
        print(f"test #{i} passed!")

if __name__ == "__main__":
    # main()
    # tests()
    random_tests(max_number=4, how_much=100000)
