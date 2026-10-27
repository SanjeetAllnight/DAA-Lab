INF=999999
def FGraph(G,k,n,p):
    cost=[INF]*(n+1)
    d=[0]*(n+1)
    cost[n]=0
    print("\nForward Approach")
    print(f"cost[{n}] = 0")
    for j in range(n-1,0,-1):
        for r in range(j+1,n+1):
            if G[j][r]!=INF and cost[r]!=INF and G[j][r]+cost[r]<cost[j]:
                cost[j]=G[j][r]+cost[r]
                d[j]=r
        print(f"cost[{j}] =",cost[j] if cost[j]!=INF else "INF","d["+str(j)+"] =",d[j] if d[j]!=0 else "_")
    if cost[1]==INF:
        print("No path exists.")
        return INF
    p[1]=1
    p[k]=n
    for j in range(2,k):
        p[j]=d[p[j-1]]
    print("Minimum Cost =",cost[1])
    print("Path =", " -> ".join(map(str,p[1:k+1])))
    return cost[1]
def BGraph(G,k,n,p):
    bcost=[INF]*(n+1)
    d=[0]*(n+1)
    bcost[1]=0
    print("\nBackward Approach")
    print("bcost[1] = 0")
    for j in range(2,n+1):
        for r in range(1,j):
            if G[r][j]!=INF and bcost[r]!=INF and bcost[r]+G[r][j]<bcost[j]:
                bcost[j]=bcost[r]+G[r][j]
                d[j]=r
        print(f"bcost[{j}] =",bcost[j] if bcost[j]!=INF else "INF","d["+str(j)+"] =",d[j] if d[j]!=0 else "_")
    if bcost[n]==INF:
        print("No path exists.")
        return INF
    p[1]=1
    p[k]=n
    for j in range(k-1,1,-1):
        p[j]=d[p[j+1]]
    print("Minimum Cost =",bcost[n])
    print("Path =", " -> ".join(map(str,p[1:k+1])))
    return bcost[n]
def main():
    try:
        n=int(input("Enter number of vertices: "))
        k=int(input("Enter number of stages: "))
        if n<2 or k<2 or k>n:
            raise ValueError("Invalid number of vertices or stages.")
        G=[[INF]*(n+1) for _ in range(n+1)]
        print("Enter cost matrix (use INF for no edge):")
        for i in range(1,n+1):
            row=[None]+input().split()
            if len(row)!=n+1:
                raise ValueError("Each row must contain exactly n values.")
            for j in range(1,n+1):
                G[i][j]=INF if row[j].upper()=="INF" else int(row[j])
        p=[0]*(k+1)
        q=[0]*(k+1)
        f=FGraph(G,k,n,p)
        b=BGraph(G,k,n,q)
        if f!=INF and b!=INF and f!=b:
            print("Warning: The two approaches produced different costs. Check the matrix and stage ordering.")
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()