class PriorityQueue:
    def __init__(self):
        self._list = []

    def __bool__(self):
        return bool(self._list)

    def __len__(self):
        return len(self._list)

    def insert(self, element, priority):
        self._list.append((element, priority))

    def exctract_min(self):
        min_el_ind, min_p = 0, self._list[0][1]
        for i in range(len(self._list)):
            priority = self._list[i][1]
            if priority < min_p:
                min_el_ind, min_p = i, priority
        return self._list.pop(min_el_ind)


def unrefixed_code(s):
    elements_counts = {}
    for ch in s:
        if ch in elements_counts:
            elements_counts[ch] += 1
        else:
            elements_counts[ch] = 1
    queue = PriorityQueue()
    for i, (element, priority) in enumerate(elements_counts.items()):
        queue.insert((element, True, priority), priority)
    nodes = []
    n = len(queue)
    for i in range(n + 1, 2 * n - 1 + 1):
        node1, node1_p = queue.exctract_min()
        node2, node2_p = queue.exctract_min()
        parent, parent_p = (i, False, node1_p + node2_p), node1_p + node2_p
        queue.insert(parent, parent_p)
        nodes.append((node1, ('1', parent)))
        nodes.append((node2, ('0', parent)))
    head, _ = queue.exctract_min()
    nodes.append((head, None))
    char_codes = {}
    for ch, _ in sorted(elements_counts.items(), key=lambda item: item[1]):
        digits = []
        kid = None
        for i in range(len(nodes)):
            k = nodes[i]
            if k[0][1]:
                kid = k
                del nodes[i]
                break
        while True:
            if kid[1] is None:
                break
            for element in nodes:
                if kid[1][1] == element[0]:
                    digits.append(kid[1][0])
                    kid = element
                    break
        char_codes[ch] = ''.join(digits[::-1])
    if len(set(s)) == 1:
        char_codes[s[0]] = '0'
    coded_str = ""
    for ch in s:
        coded_str += char_codes[ch]
    print(len(char_codes), len(coded_str))
    for ch, code in char_codes.items():
        print("{}: {}".format(ch, code))
    print(coded_str)
    return char_codes


def main():
    s = input()
    unrefixed_code(s)


if __name__ == "__main__":
    main()

def main():
    # s = input()
    s = "abacabad"
    s = "beep boop beer!"
    import string
    import random
    s = ''.join(random.choices(string.ascii_lowercase, k=10**4))
    unrefixed_code(s)


if __name__ == "__main__":
    main()
