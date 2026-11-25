n = int(input("Enter the value of n: "))
x = [0] * (n + 1)
found = False
def Place(k, i):
    for j in range(1, k):
        if (x[j] == i) or (abs(x[j] - i) == abs(j - k)):
            return False
    return True
def NQueens(k, n):
    global x, found
    for i in range(1, n + 1):
        if Place(k, i):
            x[k] = i
            if k == n:
                found = True
                return True
            if NQueens(k + 1, n):
                return True
    return False
NQueens(1, n)
if found:
    print("\nFirst Solution:")
    for r in range(1, n + 1):
        row = ["-"] * n
        row[x[r] - 1] = "Q"
        print("  [ " + " ".join(row) + " ]")
    print("  Array:", x[1:n+1])
else:
    print("No solution exists")