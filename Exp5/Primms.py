def Prim(E,cost,n,t):
    k,l=E[0]
    for edge in E:
        if cost[edge[0]][edge[1]]<cost[k][l]:
            k,l=edge
    mincost=cost[k][l]
    t[1][1]=k
    t[1][2]=l
    near=[0]*(n+1)
    for i in range(1,n+1):
        if cost[i][l]<cost[i][k]:
            near[i]=l
        else:
            near[i]=k
    near[k]=near[l]=0
    print_step(1,k,l,mincost,cost[k][l],near,n)
    for i in range(2,n):
        j=0
        for k in range(1,n+1):
            if near[k]!=0:
                if j==0 or cost[k][near[k]]<cost[j][near[j]]:
                    j=k
        t[i][1]=j
        t[i][2]=near[j]
        mincost=mincost+cost[j][near[j]]
        print_step(i,j,near[j],mincost,cost[j][near[j]],near,n)
        near[j]=0
        for k in range(1,n+1):
            if near[k]!=0 and cost[k][near[k]]>cost[k][j]:
                near[k]=j
    return mincost
def print_step(i,j,k,mincost,c,near,n):
    print("\nStep",i)
    print("i =",j,"j =",k)
    print("minCost =",mincost)
    print(f"Cost[{j},{k}] =",c)
    print("near[] =",["_" if near[x]==0 else near[x] for x in range(1,n+1)])
def main():
    try:
        n=int(input("Enter number of vertices: "))
        if n<2:
            raise ValueError("Number of vertices must be at least 2.")
        cost=[[0]*(n+1) for _ in range(n+1)]
        print("Enter cost matrix:")
        for i in range(1,n+1):
            row=input().split()
            if len(row)!=n:
                raise ValueError("Each row must contain exactly n values.")
            for j in range(1,n+1):
                if row[j-1].upper()=="INF":
                    cost[i][j]=float("inf")
                else:
                    cost[i][j]=float(row[j-1])
                if i==j and cost[i][j]!=float("inf"):
                    raise ValueError("Diagonal elements must be INF.")
                if i!=j and cost[i][j]!=float("inf") and cost[i][j]<=0:
                    raise ValueError("Edge costs must be positive.")
        E=[]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if cost[i][j]!=float("inf"):
                    E.append((i,j))
        if len(E)<n-1:
            raise ValueError("Graph does not have enough edges for a spanning tree.")
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if cost[i][j]!=cost[j][i]:
                    raise ValueError("Cost matrix must be symmetric.")
        t=[[0,0,0] for _ in range(n)]
        mincost=Prim(E,cost,n,t)
        print("\nMST Edges:")
        for i in range(1,n):
            print(f"({t[i][1]},{t[i][2]})")
        print("Minimum Cost =",mincost)
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()