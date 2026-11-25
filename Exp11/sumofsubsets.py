n = 5
m = 162
w = [18, 54, 72, 90, 108]
x = [0] * (n + 2)
def SumOfSub(s, k, r):
  global x, w, n, m
  x[k] = 1
  if s + w[k] == m:
    print(f"Subset found: {x[1:n+1]}")
  elif s + w[k] + w[k + 1] <= m:
    SumOfSub(s + w[k], k + 1, r - w[k])
  if (s + r - w[k] >= m) and (s + w[k + 1] <= m):
    x[k] = 0
    SumOfSub(s, k + 1, r - w[k])
if __name__ == "__main__":
  total_sum = sum(w)
  SumOfSub(0, 1, total_sum)