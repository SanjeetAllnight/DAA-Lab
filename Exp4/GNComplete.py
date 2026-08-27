def knapsack(m,order):
    x=[0.0]*(n+1)
    u=m
    for i in order:
        if w[i]<=u:
            x[i]=1.0
            u-=w[i]
        else:
            x[i]=u/w[i]
            break
    return x
def main():
    global n,p,w
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
        order=list(range(1,n+1))
        fractional=knapsack(m,order)
        least_weight=knapsack(m,sorted(order,key=lambda i:w[i]))
        max_profit=knapsack(m,sorted(order,key=lambda i:p[i],reverse=True))
        ratio=knapsack(m,sorted(order,key=lambda i:p[i]/w[i],reverse=True))
        for name,x in [("Fractional",fractional),("Least Weight",least_weight),("Maximum Profit",max_profit),("Ratio",ratio)]:
            profit=sum(p[i]*x[i] for i in range(1,n+1))
            print("\n"+name)
            print("x =",[round(x[i],2) for i in range(1,n+1)])
            print("Maximum profit =",profit)
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()