import sys


def binary_search(array, numbers):
    result_array = []
    for number in numbers:
        left = 0
        right = len(array) - 1
        while left <= right:
            k = left + (right - left) // 2
            if array[k] == number:
                result_array.append(k+1)
                break
            elif array[k] > number:
                right = k - 1
            else:
                left = k + 1
        else:
            result_array.append(-1)
    return result_array


def tests(func):
    tested = [
        [
            ([1, 5, 8, 12, 13], [8, 1, 23, 1, 11]),
            [3, 1, -1, 1, -1]
        ]
    ]
    for i, test in enumerate(tested):
        args, true_result = test
        result = func(*args)
        assert (result == true_result)
        print(f"#{i} passed!")


def time_it(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print('Time spent: {}'.format(time.time()-start_time))
    return wrapper


def main():
    array_size, *array = list(map(int, sys.stdin.readline().split()))
    k, *numbers = list(map(int, sys.stdin.readline().split()))
    result = binary_search(array, numbers)
    print(*result)


@time_it
def test_time(array_size, numbers):
    result = binary_search(array, numbers)
    print(*result)


if __name__ == "__main__":
    # tests(binary_search)
    main()
    # import random
    # array = sorted(random.randint(10**8, 10**9) for _ in range(10**5))
    # numbers = [random.randint(10**8, 10**9) for _ in range(10**5)]
    # test_time(array, numbers)
