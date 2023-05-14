class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, n):
        self.root = self._build(0, n)

    def _build(self, start, end):
        node = Node(start, end)
        if start == end:
            return node
        mid = (start + end) // 2
        node.left = self._build(start, mid)
        node.right = self._build(mid+1, end)
        return node

    def update(self, node, i, j, val):
        if node.start == i and node.end == j:
            node.sum += val
            return
        mid = (node.start + node.end) // 2
        if j <= mid:
            self.update(node.left, i, j, val)
        elif i > mid:
            self.update(node.right, i, j, val)
        else:
            self.update(node.left, i, mid, val)
            self.update(node.right, mid+1, j, val)
        node.sum = node.left.sum + node.right.sum

    def query(self, node):
        if node.start == node.end:
            return [node.start, node.end, node.sum]
        if node.left.sum >= node.right.sum:
            return self.query(node.left)
        else:
            return self.query(node.right)

def findTheRange(n, receptions):
    tree = SegmentTree(n)
    for reception in receptions:
        i, j, val = reception
        tree.update(tree.root, i, j, val)
    return tree.query(tree.root)

if __name__ == '__main__':
    n = 5
    receptions = [[2, 4, 5], [1, 3, 6], [2, 4, 7]]
    result = findTheRange(n, receptions)
    print(result)
