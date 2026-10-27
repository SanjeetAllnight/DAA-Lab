INF=999999
def print_matrix(name,A,n,path=False):
    print("\n"+name)
    print("    "+" ".join(f"{j:>5}" for j in range(1,n+1)))
    for i in range(1,n+1):
        print(f"{i:>3} ",end="")
        for j in range(1,n+1):
            v="-" if path and i==j else "INF" if not path and A[i][j]==INF else A[i][j]
            print(f"{v:>5}",end=" ")
        print()
def AllPaths(cost,A,P,n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i][j]=cost[i][j]
            P[i][j]=i if i!=j else 0
    print_matrix("A^0",A,n)
    print_matrix("P^0",P,n,True)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if A[i][k]!=INF and A[k][j]!=INF and A[i][j]>A[i][k]+A[k][j]:
                    A[i][j]=A[i][k]+A[k][j]
                    P[i][j]=P[k][j]
        print_matrix(f"A^{k}",A,n)
        print_matrix(f"P^{k}",P,n,True)
def get_path(i,j,A,P,n):
    if A[i][j]==INF:
        return "No path"
    path=[j]
    while j!=i:
        j=P[i][j]
        if j==0 or len(path)>n:
            return "No path"
        path.append(j)
    return " -> ".join(map(str,path[::-1]))
def main():
    try:
        n=int(input("Enter number of vertices: "))
        if n<=0:
            raise ValueError("Number of vertices must be greater than 0.")
        cost=[[0]*(n+1) for _ in range(n+1)]
        print("Enter cost matrix (use INF for no edge):")
        for i in range(1,n+1):
            row=[None]+input().split()
            if len(row)!=n+1:
                raise ValueError("Each row must contain exactly n values.")
            for j in range(1,n+1):
                cost[i][j]=INF if row[j].upper()=="INF" else int(row[j])
            if cost[i][i]!=0:
                raise ValueError("Diagonal elements must be 0.")
        A=[[0]*(n+1) for _ in range(n+1)]
        P=[[0]*(n+1) for _ in range(n+1)]
        AllPaths(cost,A,P,n)
        if any(A[i][i]<0 for i in range(1,n+1)):
            print("\nNegative-weight cycle detected; shortest paths are undefined.")
            return
        print("\nSrc | Dest | Length | Path")
        print("-"*55)
        for i in range(1,n+1):
            for j in range(1,n+1):
                length="INF" if A[i][j]==INF else A[i][j]
                print(f"{i:>3} | {j:>4} | {str(length):>6} | {get_path(i,j,A,P,n)}")
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()