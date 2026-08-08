import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

tree_nodes = []
rows = []

def maxmin(arr, i, j, level=0):
    if i == j:
        mn = mx = arr[i]
    elif j == i + 1:
        if arr[i] < arr[j]:
            mn, mx = arr[i], arr[j]
        else:
            mn, mx = arr[j], arr[i]
    else:
        mid = (i + j) // 2
        min1, max1 = maxmin(arr, i, mid, level + 1)
        min2, max2 = maxmin(arr, mid + 1, j, level + 1)
        mn = min(min1, min2)
        mx = max(max1, max2)

    tree_nodes.append({"i": i, "j": j, "min": mn, "max": mx, "level": level})
    rows.append([i + 1, j + 1, mn, mx])
    return mn, mx

n = int(input("Enter number of elements: "))
if not 2 <= n <= 20:
    raise ValueError("Enter a number from 2 to 20.")

print("Enter elements:")
arr = list(map(int, input().split()))
if len(arr) != n:
    raise ValueError(f"Enter exactly {n} integers.")

minimum, maximum = maxmin(arr, 0, n - 1)

max_level = max(node["level"] for node in tree_nodes)
fig, (tree_ax, table_ax) = plt.subplots(
    2, 1, figsize=(18, 10), gridspec_kw={"height_ratios": [3, 1]}
)

for node in tree_nodes:
    i, j, level = node["i"], node["j"], node["level"]
    if j - i > 1:
        mid = (i + j) // 2
        x = (i + j) * 2.5
        y = (max_level - level) * 1.45
        child_y = (max_level - level - 1) * 1.45
        tree_ax.plot([x, (i + mid) * 2.5], [y - 0.55, child_y + 0.55], "k-", linewidth=1)
        tree_ax.plot([x, (mid + 1 + j) * 2.5], [y - 0.55, child_y + 0.55], "k-", linewidth=1)

for node in tree_nodes:
    i, j, level = node["i"], node["j"], node["level"]
    x = (i + j) * 2.5
    y = (max_level - level) * 1.45
    values_text = " ".join(map(str, arr[i:j + 1]))
    width = max(6, len(values_text) * 0.40 + 2)
    size = max(8, min(13, 15 - len(values_text) / 10))
    tree_ax.add_patch(Rectangle((x - width / 2, y - 0.55), width, 1.10,
                                facecolor="white", edgecolor="black"))
    tree_ax.text(x, y + 0.23, f"i = {i + 1}      j = {j + 1}",
                 ha="center", va="center", fontsize=size)
    tree_ax.text(x, y, values_text, ha="center", va="center", fontsize=size)
    tree_ax.text(x - width / 2 + 0.20, y - 0.24, f"Min = {node['min']}",
                 ha="left", va="center", fontsize=size)
    tree_ax.text(x + width / 2 - 0.20, y - 0.24, f"Max = {node['max']}",
                 ha="right", va="center", fontsize=size)

tree_ax.set_xlim(-3, (n - 1) * 5 + 3)
tree_ax.set_ylim(-0.8, max_level * 1.45 + 0.8)
tree_ax.axis("off")

table = table_ax.table(cellText=rows, colLabels=["i", "j", "Min", "Max"],
                       cellLoc="center", colLoc="center", bbox=[0.2, 0, 0.6, 1])
table.auto_set_font_size(False)
table.set_fontsize(max(7, 13 - len(rows) // 4))
table_ax.axis("off")

plt.tight_layout()
plt.show()
