def max_cost_of_stolen(max_weight, things):
    sorted_things = sorted(things, key=lambda x: x[0] / x[1], reverse=True)
    max_cost = 0
    weight_left = max_weight
    for cost, weight in sorted_things:
        if weight_left > weight:
            max_cost += cost
            weight_left -= weight
        else:
            max_cost += cost * weight_left / weight
            break
    return max_cost


def main():
    n, max_weight = map(int, input().split())
    s = []
    for _ in range(n):
        a, b = map(int, input().split())
        s.append((a, b))
    max_cost = max_cost_of_stolen(max_weight, s)
    print(max_cost)


if __name__ == "__main__":
    main()
