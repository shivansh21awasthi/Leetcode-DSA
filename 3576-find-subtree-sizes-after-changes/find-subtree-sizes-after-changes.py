class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = defaultdict(list)
        for node in range(1, n):
            tree[parent[node]].append(node)

        new_parent = parent[:]
        last = [-1] * 26

        def rewire(node: int) -> None:
            idx = ord(s[node]) - 97
            old = last[idx]
            if old != -1:
                new_parent[node] = old
            last[idx] = node
            for child in tree[node]:
                rewire(child)
            last[idx] = old

        rewire(0)

        new_tree = defaultdict(list)
        for node in range(1, n):
            new_tree[new_parent[node]].append(node)

        ans = [0] * n

        def subtree_size(node: int) -> int:
            size = 1
            for child in new_tree[node]:
                size += subtree_size(child)
            ans[node] = size
            return size

        subtree_size(0)
        return ans