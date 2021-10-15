class MaxHeap:
    def __init__(self):
        self._container = []

    def _swap(self, i, j):
        t = self._container[i]
        self._container[i] = self._container[j]
        self._container[j] = t

    def _parent_ind(self, i):
        par_ind = (i + 1) // 2
        par_ind -= 1
        return par_ind

    def _sift_up(self, index):
        cur_ind = index
        while cur_ind:
            par_ind = self._parent_ind(cur_ind)
            if self._container[cur_ind] > self._container[par_ind]:
                self._swap(par_ind, cur_ind)
                cur_ind = par_ind
            else:
                break

    def _child_inds(self, i):
        left_ind = (i + 1) * 2
        right_ind = left_ind + 1
        left_ind -= 1
        right_ind -= 1
        return left_ind, right_ind

    def _sift_down(self, index):
        cur_ind = index
        n = len(self._container)
        while cur_ind <= n:
            left_ind, right_ind = self._child_inds(cur_ind)
            s_ind = None
            if left_ind < n and right_ind < n:
                if self._container[left_ind] > self._container[right_ind]:
                    s_ind = left_ind
                else:
                    s_ind = right_ind
            elif left_ind < n:
                s_ind = left_ind
            elif right_ind < n:
                s_ind = right_ind
            else:
                break
            if self._container[cur_ind] > self._container[s_ind]:
                break
            self._swap(s_ind, cur_ind)
            cur_ind = s_ind

    def insert(self, priority):
        self._container.append(priority)
        cur_ind = len(self._container) - 1
        self._sift_up(cur_ind)

    def extract_max(self):
        self._swap(0, -1)
        max_ = self._container.pop()
        self._sift_down(0)
        return max_


def main():
    heap = MaxHeap()
    n = int(input())
    for _ in range(n):
        s = input()
        if s.startswith('Insert'):
            val = int(s.split()[1])
            heap.insert(val)
        elif s.startswith('ExtractMax'):
            print(heap.extract_max())
        else:
            raise ValueError


if __name__ == "__main__":
    main()
