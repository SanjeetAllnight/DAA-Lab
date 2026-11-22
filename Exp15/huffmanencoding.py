def Huffman(x):
    freq = {}
    for ch in x:
        freq[ch] = freq.get(ch, 0) + 1
    Q = [[f, ch, None, None] for ch, f in freq.items()]
    while len(Q) > 1:
        Q.sort(key=lambda T: T[0])
        T1 = Q.pop(0)
        T2 = Q.pop(0)
        T = [T1[0] + T2[0], None, T1, T2]
        Q.append(T)
    def display(T, code=""):
        if T[1] is not None:
            print(repr(T[1]), ":", code if code else "0")
        else:
            display(T[2], code + "0")
            display(T[3], code + "1")
    display(Q[0])
x = input("Enter sentence: ")
Huffman(x)