def add(A,B):
    n=len(A)
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def sub(A,B):
    n=len(A)
    return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]
def strassen(A,B,n):
    if n==2:
        return [[A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]],[A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
    mid=n//2
    A11=[r[:mid] for r in A[:mid]]
    A12=[r[mid:] for r in A[:mid]]
    A21=[r[:mid] for r in A[mid:]]
    A22=[r[mid:] for r in A[mid:]]
    B11=[r[:mid] for r in B[:mid]]
    B12=[r[mid:] for r in B[:mid]]
    B21=[r[:mid] for r in B[mid:]]
    B22=[r[mid:] for r in B[mid:]]
    P=strassen(add(A11,A22),add(B11,B22),mid)
    Q=strassen(add(A21,A22),B11,mid)
    R=strassen(A11,sub(B12,B22),mid)
    S=strassen(A22,sub(B21,B11),mid)
    T=strassen(add(A11,A12),B22,mid)
    U=strassen(sub(A21,A11),add(B11,B12),mid)
    V=strassen(sub(A12,A22),add(B21,B22),mid)
    C11=add(sub(add(P,S),T),V)
    C12=add(R,T)
    C21=add(Q,S)
    C22=add(sub(add(P,R),Q),U)
    C=[]
    for i in range(mid):
        C.append(C11[i]+C12[i])
    for i in range(mid):
        C.append(C21[i]+C22[i])
    return C
def main():
    try:
        n=int(input("Enter size of matrix: "))
        if n<2 or (n&(n-1))!=0:
            raise ValueError("Size must be a power of 2.")
        print("Enter Matrix A:")
        A=[]
        for i in range(n):
            row=input(f"Row {i+1}: ").split()
            if len(row)!=n:
                raise ValueError(f"Row {i+1} must contain {n} elements.")
            A.append(list(map(int,row)))
        print("Enter Matrix B:")
        B=[]
        for i in range(n):
            row=input(f"Row {i+1}: ").split()
            if len(row)!=n:
                raise ValueError(f"Row {i+1} must contain {n} elements.")
            B.append(list(map(int,row)))
        C=strassen(A,B,n)
        print("Result Matrix:")
        for row in C:
            print(*row)
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()