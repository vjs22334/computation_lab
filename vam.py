from collections import defaultdict

costs  = {'W': {'A': 4, 'B': 6, 'C': 8, 'D': 13, 'E': 0},
          'X': {'A': 13, 'B': 11, 'C': 10, 'D': 8, 'E': 0},
          'Y': {'A': 14, 'B': 4, 'C': 10, 'D': 13, 'E': 0},
          'Z': {'A': 9, 'B': 11, 'C': 13, 'D': 8, 'E': 0}}
demand = {'A': 25, 'B': 35, 'C': 105, 'D': 20, 'E': 15}
cols = sorted(demand.iterkeys())

supply = {'W': 50, 'X': 70, 'Y': 30, 'Z': 50}
res = dict((k, defaultdict(int)) for k in costs)
g = {}
for x in supply:
    g[x] = sorted(costs[x].iterkeys(), key=lambda g: costs[x][g])
for x in demand:
    g[x] = sorted(costs.iterkeys(), key=lambda g: costs[g][x])



while g:
    d = {}
    for x in demand:
        d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else costs[g[x][0]][x]
    s = {}
    for x in supply:
        s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]]) if len(g[x]) > 1 else costs[x][g[x][0]]
    f = max(d, key=lambda n: d[n])
    t = max(s, key=lambda n: s[n])
    t, f = (f, g[f][0]) if d[f] > s[t] else (g[t][0], t)
    v = min(supply[f], demand[t])
    res[f][t] += v
    demand[t] -= v
    if demand[t] == 0:
        for k, n in supply.iteritems():
            if n != 0:
                g[k].remove(t)
        del g[t]
        del demand[t]
    supply[f] -= v
    if supply[f] == 0:
        for k, n in demand.iteritems():
            if n != 0:
                g[k].remove(f)
        del g[f]
        del supply[f]

cost = 0
print "transporatation matrix"
print(res)
for g in sorted(costs):
    for n in cols:
        y = res[g][n]
        cost += y * costs[g][n]

print "\n\nTotal Cost = ", cost