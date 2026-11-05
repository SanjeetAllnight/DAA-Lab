from tabulate import tabulate
from fractions import Fraction
from textwrap import wrap
x=[]
wp=[]
def greedy(m,n):
    for i in range(1,n+1):
        x[i]=0.0
    u=m
    for i in range(1,n+1):
        if(wp[i][0]>u):
            break
        x[i]=1.0
        u-=wp[i][0]
    if(i<=n):
        x[i]=u/wp[i][0]
def printing():
    profit,wt=0,0
    for i in range(1,len(wp)):
        profit+=x[i]*wp[i][1]
        wt+=x[i]*wp[i][0]
    return wt,profit
def original_x():
    ans=[0]*(n+1)
    for i in range(1,n+1):
        ans[wp[i][2]]=x[i]
    return ans[1:]
def fraction_x(arr):
    return [str(Fraction(v).limit_denominator()) for v in arr]
if __name__ == "__main__":
    n = int(input("Enter number of items (n): "))
    m = float(input("Enter knapsack capacity (m): "))
    weights = list(map(float, input(f"Enter {n} weights : ").split()))
    profits = list(map(float, input(f"Enter {n} profits : ").split()))
    if len(weights) != n or len(profits) != n:
        print("Error: number of weights/profits must equal n.")
        exit(1)
    wp = [[0, 0, 0]] + [[weights[i], profits[i], i + 1] for i in range(n)]
    x=[0]*(n+1)
    result=[]
    for i in range(1,n+1):
        x[i]=1/(i+1)
    wt,profit=printing()
    result.append(["Fractions",wt,profit,fraction_x(x[1:])])
    wp=[[0,0,0]]+sorted(wp[1:],key=lambda w:w[0])
    greedy(m,n)
    wt,profit=printing()
    result.append(["Min Weight",wt,profit,fraction_x(original_x())])
    wp=[[0,0,0]]+sorted(wp[1:],key=lambda w:w[1],reverse=True)
    greedy(m,n)
    wt,profit=printing()
    result.append(["Max Profit",wt,profit,fraction_x(original_x())])
    wp=[[0,0,0]]+sorted(wp[1:],key=lambda w:w[1]/w[0],reverse=True)
    greedy(m,n)
    wt,profit=printing()
    result.append(["Profit/Weight",wt,profit,fraction_x(original_x())])
    for row in result:
        row[3]="\n".join(wrap(str(row[3])))
    print(tabulate(
        result,headers=["Method","Total Weight","Total Profit",
                        "Solution Vector"],
        tablefmt="grid")
    )