import heapq
def Bound(cp, cw, k, p, w, m):
    b = cp
    c = cw
    for i in range(k + 1, len(p)):
        c = c + w[i]
        if c < m:
            b = b + p[i]
        else:
            return b + (1 - (c - m) / w[i]) * p[i]
    return b

def UBound(cp, cw, k, p, w, m):
    b = cp
    c = cw
    for i in range(k + 1, len(p)):
        if c + w[i] <= m:
            c = c + w[i]
            b = b + p[i]
    return b

def knapsack(p, w, m):
    n = len(p)
    items = sorted(
        zip(p, w),
        key=lambda x: x[0] / x[1],
        reverse=True
    )
    p = [x[0] for x in items]
    w = [x[1] for x in items]
    best_profit = 0
    best_items = []
    pq = []
    heapq.heappush(pq, (-Bound(0, 0, -1, p, w, m),0, 0, -1, []))
    while pq:
        neg_bound, cp, cw, k, selected = heapq.heappop(pq)
        if -neg_bound <= best_profit:
            continue
        if k == n - 1:
            continue
        i = k + 1
        if cw + w[i] <= m:
            new_cp = cp + p[i]
            new_cw = cw + w[i]
            new_selected = selected + [i]
            if new_cp > best_profit:
                best_profit = new_cp
                best_items = new_selected
            ub = UBound(new_cp, new_cw, i, p, w, m)
            if ub > best_profit:
                b = Bound(new_cp, new_cw, i, p, w, m)
                heapq.heappush(pq, (-b, new_cp, new_cw, i, new_selected))
        ub = UBound(cp, cw, i, p, w, m)
        if ub > best_profit:
            b = Bound(cp, cw, i, p, w, m)
            heapq.heappush(pq, (-b, cp, cw, i, selected))
    print("\nMaximum Profit:", best_profit)
    print("Selected Items:", best_items)
n = int(input("Enter number of objects: "))
p = list(map(int, input("Enter profits: ").split()))
w = list(map(int, input("Enter weights: ").split()))
m = int(input("Enter knapsack capacity: "))
knapsack(p, w, m)