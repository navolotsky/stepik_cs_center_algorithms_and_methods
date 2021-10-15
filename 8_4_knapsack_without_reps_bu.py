import sys


def knapsack_without_reps_bu(weight, things):
    if not isinstance(things[0], tuple):
        things = [(t, t) for t in things]
    knapsack = [[0] * (len(things) + 1) for _ in range((weight + 1))]
    for i, (w_i, c_i) in enumerate(things, 1):
        for w in range(1, weight + 1):
            knapsack[w][i] = knapsack[w][i - 1]
            if w_i <= w:
                knapsack[w][i] = max(
                    knapsack[w][i], knapsack[w - w_i][i - 1] + c_i)
    return knapsack[-1][-1]


def main():
    knapsack_max_weight, _ = map(int, sys.stdin.readline().split())
    things_weights = list(map(int, sys.stdin.readline().split()))
    print(knapsack_without_reps_bu(knapsack_max_weight, things_weights))


def test():
    assert knapsack_without_reps_bu(
        10, [(6, 30), (3, 14), (4, 16), (2, 9)]) == 46
    assert knapsack_without_reps_bu(10, [1, 4, 8]) == 9
    assert knapsack_without_reps_bu(
        10, [(4, 16), (2, 9), (6, 30), (3, 14)]) == 46
    assert knapsack_without_reps_bu(10, [1, 8, 4]) == 9
    assert knapsack_without_reps_bu(0, [(1, 0)]) == 0
    assert knapsack_without_reps_bu(0, [1, 2]) == 0
    assert knapsack_without_reps_bu(0, [1]) == 0
    assert knapsack_without_reps_bu(1, [1]) == 1
    assert knapsack_without_reps_bu(1, [(1, 0)]) == 0
    assert knapsack_without_reps_bu(1, [(1, 0), (2, 1)]) == 0
    assert knapsack_without_reps_bu(1, [(1, 0), (1, 5)]) == 5
    assert knapsack_without_reps_bu(1, [1, 2]) == 1
    assert knapsack_without_reps_bu(2, [1, 2]) == 2
    assert knapsack_without_reps_bu(1, [(0, 2), (0, 0)]) == 2
    assert knapsack_without_reps_bu(0, [0, 2]) == 0
    assert knapsack_without_reps_bu(0, [(0, 2)]) == 0


def time_test(number=50):
    import random
    import timeit
    print(timeit.timeit(stmt="knapsack_without_reps_bu(w, things)", setup=(
        "w = 10**4; n = 300; things = list(random.randint(0, 10**5) for _ in range(n))"),
        number=number,
        globals={**globals(), **locals()}
    )/number)


if __name__ == "__main__":
    # main()
    # test()
    time_test()
