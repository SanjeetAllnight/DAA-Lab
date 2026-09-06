import random
import time
import timeit
from tabulate import tabulate


def merge(a, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2

        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(a, left, right)


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
        merge_sort(data.copy())
        t1 = time.time() - start

        t2 = timeit.timeit(
            lambda: merge_sort(data.copy()),
            number=1
        )

        row.append(f"{t1:.6f}/{t2:.6f}")

    table.append(row)


print(tabulate(
    table,
    headers=["Type", 1000, 2500, 5000, 7500, 10000],
    tablefmt="grid"
))