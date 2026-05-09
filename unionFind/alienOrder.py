def alienOrder(words):
    adj = {c: set() for word in words for c in word}
    for j in range(len(words) - 1):
        w1, w2 = words[j], words[j + 1]
        min_len = min(len(w1), len(w2))
        for i in range(min_len):
            if w1[i] != w2[i]:
                adj[w1[i]].add(w2[i])
                break
    visited = {}
    order = []
    def dfs(c):
        if c in visited:
            return visited[c]
        visited[c] = True
        for nei in adj[c]:
            if dfs(nei):
                return True
        visited[c] = False
        order.append(c)
        return True