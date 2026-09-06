import random
import timeit


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def normal_multiply(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    m = n // 2

    A11, A12 = [r[:m] for r in A[:m]], [r[m:] for r in A[:m]]
    A21, A22 = [r[:m] for r in A[m:]], [r[m:] for r in A[m:]]

    B11, B12 = [r[:m] for r in B[:m]], [r[m:] for r in B[:m]]
    B21, B22 = [r[:m] for r in B[m:]], [r[m:] for r in B[m:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    return [C11[i] + C12[i] for i in range(m)] + \
           [C21[i] + C22[i] for i in range(m)]


def generate_matrix(n):
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]


sizes = [32, 64, 128, 256, 512]
runs = 3

normal_times = []
strassen_times = []

for n in sizes:
    A = generate_matrix(n)
    B = generate_matrix(n)

    normal_times.append(
        timeit.timeit(lambda: normal_multiply(A, B), number=runs) / runs
    )

    strassen_times.append(
        timeit.timeit(lambda: strassen(A, B), number=runs) / runs
    )


print("\nExecution Time (seconds)\n")
print(f"{'Method':<25}" + "".join(f"{'n='+str(n):<15}" for n in sizes))
print("-" * 100)

print(f"{'Normal Multiplication':<25}" +
      "".join(f"{t:<15.6f}" for t in normal_times))

print(f"{'Strassen Multiplication':<25}" +
      "".join(f"{t:<15.6f}" for t in strassen_times))