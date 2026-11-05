INF=999
n=10
cost=[
[0,0,0,0,0,0,0,0,0,0,0],
[0,INF,98,60,65,12,20,95,13,INF,INF],
[0,98,INF,28,92,20,61,23,64,27,62],
[0,60,28,INF,55,51,34,25,INF,73,INF],
[0,65,92,55,INF,49,54,81,43,15,59],
[0,12,20,51,49,INF,97,80,30,INF,88],
[0,20,61,34,54,97,INF,26,66,66,22],
[0,95,23,25,81,80,26,INF,36,61,55],
[0,13,64,INF,43,30,66,36,INF,87,95],
[0,INF,27,73,15,INF,66,61,87,INF,69],
[0,INF,62,INF,59,88,22,55,95,69,INF]
]
def Prim(E,cost,n,t):
    k,l=E[1]
    for x in range(1,len(E)):
        edge=E[x]
        if cost[edge[0]][edge[1]]<cost[k][l]:
            k,l=edge[0],edge[1]
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
        E=[None]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if cost[i][j]!=INF:
                    E.append((i,j))
        t=[[0,0,0] for _ in range(n)]
        mincost=Prim(E,cost,n,t)
        print("\nMinimum Cost =",mincost)
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()