INF=999999
def ShortestPath(v,cost,dist,n):
    s=[False]*(n+1)
    parent=[0]*(n+1)
    for i in range(1,n+1):
        s[i]=False
        dist[i]=cost[v][i]
        if cost[v][i]<INF:
            parent[i]=v
    s[v]=True
    dist[v]=0
    print_step(1,v,s,dist,n)
    for num in range(2,n+1):
        u=0
        for i in range(1,n+1):
            if not s[i] and (u==0 or dist[i]<dist[u]):
                u=i
        s[u]=True
        for w in range(1,n+1):
            if not s[w] and cost[u][w]<INF:
                if dist[w]>dist[u]+cost[u][w]:
                    dist[w]=dist[u]+cost[u][w]
                    parent[w]=u
        print_step(num,u,s,dist,n)
    return parent
def print_step(step,u,s,dist,n):
    print("\nStep",step,"u =",u)
    print("S:",end=" ")
    for i in range(1,n+1):
        print(f"S[{i}]={'true' if s[i] else 'false'}",end=" ")
    print()
    print("dist:",end=" ")
    for i in range(1,n+1):
        x="INF" if dist[i]>=INF else dist[i]
        print(f"dist[{i}]={x}",end=" ")
    print()
def get_path(parent,v):
    path=[]
    while v!=0:
        path.append(v)
        v=parent[v]
    return path[::-1]
def main():
    global INF
    try:
        n=int(input("Enter number of vertices: "))
        if n<=0:
            raise ValueError("Number of vertices must be greater than 0.")
        v=int(input("Enter source vertex: "))
        if v<1 or v>n:
            raise ValueError("Invalid source vertex.")
        cost=[[INF]*(n+1) for _ in range(n+1)]
        print("Enter cost matrix:")
        for i in range(1,n+1):
            row=input().split()
            if len(row)!=n:
                raise ValueError("Each row must contain exactly n values.")
            for j in range(1,n+1):
                if row[j-1].upper()=="INF":
                    cost[i][j]=INF
                else:
                    cost[i][j]=int(row[j-1])
        dist=[INF]*(n+1)
        parent=ShortestPath(v,cost,dist,n)
        print("\nSrc | Dest | Length | Path")
        print("-"*30)
        for i in range(1,n+1):
            if dist[i]>=INF:
                print(f"{v:>3} | {i:>4} | {'INF':>6} | No path")
            else:
                path=get_path(parent,i)
                print(f"{v:>3} | {i:>4} | {dist[i]:>6} | {' -> '.join(map(str,path))}")
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()
