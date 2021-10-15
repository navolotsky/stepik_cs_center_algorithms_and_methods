import sys


def knapsack_without_reps_td(weight, things):
    if not isinstance(things[0], tuple):
        things = [(t, t) for t in things]
    knapsack = {}

    def knapsack_wo_reps_td(w, i):
        v = knapsack.get((w, i))
        if v is not None:
            return v
        if w == 0 or i == 0:
            return 0
        w_i, c_i = things[i - 1]
        if w_i > w:
            knapsack[(w, i)] = knapsack_wo_reps_td(w, i - 1)
        else:
            knapsack[(w, i)] = max(
                knapsack_wo_reps_td(w, i - 1),
                knapsack_wo_reps_td(w - w_i, i - 1) + c_i
            )
        return knapsack[(w, i)]

    return knapsack_wo_reps_td(weight, len(things))


def main():
    knapsack_max_weight, _ = map(int, sys.stdin.readline().split())
    things_weights = list(map(int, sys.stdin.readline().split()))
    print(knapsack_without_reps_td(knapsack_max_weight, things_weights))


def test():
    assert knapsack_without_reps_td(10, [1, 4, 8]) == 9
    assert knapsack_without_reps_td(
        10, [(6, 30), (3, 14), (4, 16), (2, 9)]) == 46
    assert knapsack_without_reps_td(
        10, [(4, 16), (2, 9), (6, 30), (3, 14)]) == 46
    assert knapsack_without_reps_td(10, [1, 8, 4]) == 9
    assert knapsack_without_reps_td(0, [(1, 0)]) == 0
    assert knapsack_without_reps_td(0, [1, 2]) == 0
    assert knapsack_without_reps_td(0, [1]) == 0
    assert knapsack_without_reps_td(1, [1]) == 1
    assert knapsack_without_reps_td(1, [(1, 0)]) == 0
    assert knapsack_without_reps_td(1, [(1, 0), (2, 1)]) == 0
    assert knapsack_without_reps_td(1, [(1, 0), (1, 5)]) == 5
    assert knapsack_without_reps_td(1, [1, 2]) == 1
    assert knapsack_without_reps_td(2, [1, 2]) == 2
    assert knapsack_without_reps_td(1, [(0, 2), (0, 0)]) == 2
    assert knapsack_without_reps_td(0, [0, 2]) == 0
    assert knapsack_without_reps_td(0, [(0, 2)]) == 0


def time_test(number=500):
    import random
    import timeit
    import gc
    print(timeit.timeit(stmt="knapsack_without_reps_td(w, things)", setup=(
        "gc.enable(); w = 10**4; n = 300; things = list(random.randint(0, 10**5) for _ in range(n))"),
        number=number,
        globals={**globals(), **locals()}
    )/number)


if __name__ == "__main__":
    # main()
    test()
    # time_test()
