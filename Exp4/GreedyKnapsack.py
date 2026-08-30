from fractions import Fraction
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
        fractional=[str(Fraction(1,i+1)) for i in range(1,n+1)]
        least_weight=knapsack(m,sorted(order,key=lambda i:w[i]))
        max_profit=knapsack(m,sorted(order,key=lambda i:p[i],reverse=True))
        ratio=knapsack(m,sorted(order,key=lambda i:p[i]/w[i],reverse=True))
        for name,x in [("Fractional",fractional),("Least Weight",least_weight),("Maximum Profit",max_profit),("Ratio",ratio)]:
            if name=="Fractional":
                weight=sum(w[i]*float(Fraction(1,i+1)) for i in range(1,n+1))
                profit=sum(p[i]*float(Fraction(1,i+1)) for i in range(1,n+1))
            else:
                weight=sum(w[i]*x[i] for i in range(1,n+1))
                profit=sum(p[i]*x[i] for i in range(1,n+1))
                x=[round(x[i],2) for i in range(1,n+1)]
            print("\nStrategy:",name)
            print("Solution vector:",x)
            print("Total weight:",round(weight,2))
            print("Total profit:",round(profit,2))
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()