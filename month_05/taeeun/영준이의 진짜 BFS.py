from collections import deque
def build_lca(N, parent1):
    LOG = N.bit_length()
    anc = [parent1] + [[0]*(N+1) for _ in range(LOG-1)]
    for k in range(1, LOG):
        prev = anc[k-1]
        anc[k] = [0] + [prev[prev[v]] for v in range(1, N+1)]
    return anc

def lca(u, v, depth, anc):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    bit = 0
    while diff:
        if diff & 1:
            u = anc[bit][u]
        diff >>= 1
        bit += 1
    if u == v:
        return u
    for bit in range(len(anc)-1, -1, -1):
        if anc[bit][u] != anc[bit][v]:
            u = anc[bit][u]
            v = anc[bit][v]
    return anc[0][u]

def dist(u, v, depth, anc):
    w = lca(u, v, depth, anc)
    return depth[u] + depth[v] - 2*depth[w]


def bfs_collect(root, N, adj):
    q = deque([root])
    visited = [False]*(N+1)
    visited[root] = True

    order = []
    depth = [0]*(N+1)
    parent1 = [0]*(N+1)         
    while q:
        cur = q.popleft()
        order.append(cur)
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                depth[nxt]  = depth[cur] + 1
                parent1[nxt] = cur
                q.append(nxt)
    return order, depth, parent1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))

    adj = [[] for _ in range(N+1)]
    for i, par in enumerate(p, start=2):
        adj[par].append(i)
        adj[i].append(par)

    order, depth, parent1 = bfs_collect(1, N, adj)
    anc = build_lca(N, parent1)

    ans = 0
    prev = order[0]
    for cur in order[1:]:
        ans += dist(prev, cur, depth, anc)
        prev = cur

    print(f'#{tc} {ans}')