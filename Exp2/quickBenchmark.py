import random
import time
import timeit
from tabulate import tabulate

def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quick_sort(a, low, p - 1)
        quick_sort(a, p + 1, high)


def generate_data(t, n):
    if t == "Integers":
        return [random.randint(1, 100000) for _ in range(n)]
    elif t == "Floating Point":
        return [random.uniform(1, 100000) for _ in range(n)]
    elif t == "Alphabets":
        return [random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n)]
    else:
        return [''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)) for _ in range(n)]


sizes = [1000, 2500, 5000, 7500, 10000]
types = ["Integers", "Floating Point", "Alphabets", "Strings"]

table = []

for t in types:
    row = [t]

    for n in sizes:
        data = generate_data(t, n)

        start = time.time()
        quick_sort(data.copy(), 0, n - 1)
        t1 = time.time() - start

        t2 = timeit.timeit(
            lambda: quick_sort(data.copy(), 0, n - 1),
            number=1
        )

        row.append(f"{t1:.6f}/{t2:.6f}")

    table.append(row)

print(tabulate(
    table,
    headers=["Type", 1000, 2500, 5000, 7500, 10000],
    tablefmt="grid"
))