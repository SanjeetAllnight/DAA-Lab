INF=999
def Prim(E,cost,n,t):
    k,l=E[1]
    for x in range(1,len(E)):
        edge=E[x]
        if cost[edge[1]][edge[2]]<cost[k][l]:
            k,l=edge[1],edge[2]
    mincost=cost[k][l]
    t[1][1]=k
    t[1][2]=l
    near=[0]*(n+1)
    for i in range(1,n+1):
        if cost[i][l]<cost[i][k]:
            near[i]=l
        else:
            near[i]=k
    near[k]=0
    near[l]=0
    print_step(1,k,l,mincost,cost[k][l],near,t,n)
    for i in range(2,n):
        j=0
        for k in range(1,n+1):
            if near[k]!=0 and (j==0 or cost[k][near[k]]<cost[j][near[j]]):
                j=k
        if j==0:
            raise ValueError("Graph is disconnected.")
        t[i][1]=j
        t[i][2]=near[j]
        mincost=mincost+cost[j][near[j]]
        edge_cost=cost[j][near[j]]
        near[j]=0
        for k in range(1,n+1):
            if near[k]!=0 and cost[k][near[k]]>cost[k][j]:
                near[k]=j
        print_step(i,j,t[i][2],mincost,edge_cost,near,t,n)
    return mincost
def print_step(i,j,k,mincost,c,near,t,n):
    print("\nStep",i)
    print("Added Edge =",f"({j},{k})")
    print("MST Edges =",end=" ")
    for x in range(1,i+1):
        print(f"({t[x][1]},{t[x][2]})",end=" ")
    print()
    print("i =",j,"j =",k)
    print("minCost =",mincost)
    print(f"Cost[{j},{k}] =",c if c!=INF else "INF")
    print("near[] =",["_" if near[x]==0 else near[x] for x in range(1,n+1)])
def main():
    try:
        n=int(input("Enter number of vertices: "))
        if n<2:
            raise ValueError("Number of vertices must be at least 2.")
        cost=[[0]*(n+1) for _ in range(n+1)]
        print("Enter cost matrix:")
        for i in range(1,n+1):
            row=[None]+input().split()
            if len(row)!=n+1:
                raise ValueError("Each row must contain exactly n values.")
            for j in range(1,n+1):
                if row[j].upper()=="INF":
                    cost[i][j]=INF
                else:
                    cost[i][j]=int(row[j])
                if i==j and cost[i][j]!=INF:
                    raise ValueError("Diagonal elements must be INF.")
                if i!=j and cost[i][j]!=INF and cost[i][j]<=0:
                    raise ValueError("Edge costs must be positive.")
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if cost[i][j]!=cost[j][i]:
                    raise ValueError("Cost matrix must be symmetric.")
        E=[None]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if cost[i][j]!=INF:
                    E.append((i,j))
        if len(E)==1:
            raise ValueError("Graph must contain at least one edge.")
        t=[[0,0,0] for _ in range(n)]
        mincost=Prim(E,cost,n,t)
        print("\nMinimum Cost =",mincost)
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()