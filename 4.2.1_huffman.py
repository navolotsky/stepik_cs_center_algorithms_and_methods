from collections import Counter


class PriorityQueue:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def insert(self, element, priority):
        self._list.append((element, priority))

    def extract_min(self):
        min_el_ind, min_p = 0, self._list[0][1]
        for i in range(len(self._list)):
            priority = self._list[i][1]
            if priority < min_p:
                min_el_ind, min_p = i, priority
        return self._list.pop(min_el_ind)


class Node:
    def __init__(self, label, value, parent_label=None, parent_edge_label=None,
                 kids_labels=None):
        self.label = label
        self.value = value
        self.parent_label = parent_label
        self.parent_edge_label = parent_edge_label
        self.kids_labels = kids_labels


def unrefixed_code(s):
    chars_counts = Counter(s)
    queue = PriorityQueue()
    for char, frequency in chars_counts.items():
        node = Node(char, frequency)
        queue.insert(node, frequency)

    def get_graph():
        n = len(queue)
        nodes = []
        for i in range(n + 1, 2 * n - 1 + 1):
            node1, node1_priority = queue.extract_min()
            node2, node2_priority = queue.extract_min()
            parent_priority = node1_priority + node2_priority
            parent = Node(
                i, parent_priority, kids_labels=[node1.label, node2.label])
            node1.parent_label = parent.label
            node1.parent_edge_label = '1'
            node2.parent_label = parent.label
            node2.parent_edge_label = '0'
            queue.insert(parent, parent_priority)
            nodes.append(node1)
            nodes.append(node2)
        head, _ = queue.extract_min()
        nodes.append(head)
        return nodes

    def get_char_codes():
        char_codes = {}
        for char, _ in sorted(chars_counts.items(), key=lambda item: item[1]):
            digits = []
            childless = None
            for i in range(len(nodes)):
                node = nodes[i]
                if node.kids_labels is None:
                    childless = node
                    del nodes[i]
                    break
            ancestor = childless
            while True:
                if ancestor.parent_label is None:
                    break
                for node in nodes:
                    if ancestor.parent_label == node.label:
                        digits.append(ancestor.parent_edge_label)
                        ancestor = node
                        break
            char_codes[char] = ''.join(digits[::-1])
        return char_codes

    if len(set(s)) == 1:
        char_codes = {s[0]: '0'}
    else:
        nodes = get_graph()
        char_codes = get_char_codes()

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
