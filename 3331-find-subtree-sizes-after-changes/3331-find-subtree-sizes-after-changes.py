class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = [-1] * n
        last = [-1] * 26

        def dfs(node, ancestor):
            ch = ord(s[node]) - ord('a')

            previous = last[ch]

            new_parent[node] = previous if previous != -1 else ancestor

            last[ch] = node

            for child in children[node]:
                dfs(child, node)

            last[ch] = previous

        dfs(0, -1)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        def calculate_size(node):
            size = 1

            for child in new_children[node]:
                size += calculate_size(child)

            ans[node] = size
            return size

        calculate_size(0)

        return ans