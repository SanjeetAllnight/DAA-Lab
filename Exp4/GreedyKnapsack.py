def greedyKnapsack(m,n):
    for i in range(1,n+1):
        x[i]=0.0
    u=m
    for i in range(1,n+1):
        if w[i]>u:
            break
        x[i]=1.0
        u=u-w[i]
    if i<=n:
        x[i]=u/w[i]

def main():
    global p,w,x
    try:
        n=int(input("Enter n: "))
        if n<=0:
            raise ValueError("Number of objects must be greater than 0.")
        p=[0.0]+list(map(float,input("Enter profits: ").split()))
        w=[0.0]+list(map(float,input("Enter weights: ").split()))
        if len(p)!=n+1 or len(w)!=n+1:
            raise ValueError("Number of profits and weights must match n.")
        if any(v<=0 for v in w[1:]):
            raise ValueError("Weights must be greater than 0.")
        m=float(input("Enter knapsack capacity(m): "))
        if m<0:
            raise ValueError("Knapsack capacity cannot be negative.")
        items=sorted([(p[i],w[i]) for i in range(1,n+1)],key=lambda x:x[0]/x[1],reverse=True)
        p=[0.0]+[item[0] for item in items]
        w=[0.0]+[item[1] for item in items]
        x=[0.0]*(n+1)
        greedyKnapsack(m,n)
        profit=0
        print("Solution:")
        for i in range(1,n+1):
            print(f"x[{i}] = {x[i]:.2f}")
            profit+=p[i]*x[i]
        print("Maximum profit:",profit)
    except ValueError as e:
        print("Error:",e)

if __name__=="__main__":
    main()