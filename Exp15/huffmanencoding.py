import heapq

class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

def Huffman(x):
    f = {}

    for c in x:
        f[c] = f.get(c, 0) + 1

    Q = []

    for c in f:
        heapq.heappush(Q, (f[c], c, Node(c, f[c])))

    while len(Q) > 1:
        f1, c1, T1 = heapq.heappop(Q)
        f2, c2, T2 = heapq.heappop(Q)

        T = Node(c1 + c2, f1 + f2)
        T.left = T1
        T.right = T2

        heapq.heappush(Q, (T.freq, T.ch, T))

    return Q[0][2]

def printCodes(root, code=""):
    if root.left is None and root.right is None:
        print(root.ch, ":", code)
        return

    printCodes(root.left, code + "0")
    printCodes(root.right, code + "1")


x = input("Enter string: ")

root = Huffman(x)

print("Huffman Codes:")
printCodes(root)