def Find(i,parent):
    while parent[i]>=0:
        i=parent[i]
    return i
def Union(i,j,parent):
    parent[i]=j
def Adjust(A,i,n):
    j=2*i
    item=A[i]
    while j<=n:
        if j<n and A[j][0]>A[j+1][0]:
            j+=1
        if item[0]<=A[j][0]:
            break
        A[j//2]=A[j]
        j*=2
    A[j//2]=item
def Heapify(A,n):
    for i in range(n//2,0,-1):
        Adjust(A,i,n)
def DelMin(A,n,x):
    if n==0:
        return False
    x[1],x[2]=A[1][1],A[1][2]
    A[1]=A[n]
    if n>1:
        Adjust(A,1,n-1)
    return True
def Kruskal(E,cost,n,t):
    A=[None]+[[cost[E[i][0]][E[i][1]],E[i][0],E[i][1]] for i in range(1,len(E))]
    m=len(A)-1
    Heapify(A,m)
    parent=[0]*(n+1)
    for i in range(1,n+1):
        parent[i]=-1
    i=mincost=0
    x=[0,0,0]
    while i<n-1 and m:
        DelMin(A,m,x)
        m-=1
        u,v=x[1],x[2]
        j,k=Find(u,parent),Find(v,parent)
        if j!=k:
            i+=1
            t[i][1],t[i][2]=u,v
            mincost+=cost[u][v]
            Union(j,k,parent)
            print("\nStep",i)
            print("t =",end=" ")
            for q in range(1,i+1):
                print(f"({t[q][1]},{t[q][2]})",end=" ")
            print()
            print("minCost =",mincost)
    if i!=n-1:
        print("\nNo spanning tree")
    return mincost
def main():
    try:
        n=int(input("Enter number of vertices: "))
        e=int(input("Enter number of edges: "))
        if n<2 or e<n-1:
            raise ValueError("Invalid number of vertices or edges.")
        cost=[[0]*(n+1) for _ in range(n+1)]
        E=[None]
        print("Enter u v cost:")
        for _ in range(e):
            u,v,c=map(int,input().split())
            if not 1<=u<=n or not 1<=v<=n or u==v or c<=0:
                raise ValueError("Invalid edge.")
            E.append((u,v))
            cost[u][v]=cost[v][u]=c
        t=[[0,0,0] for _ in range(n)]
        mincost=Kruskal(E,cost,n,t)
        if mincost:
            print("\nMinimum Cost =",mincost)
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()