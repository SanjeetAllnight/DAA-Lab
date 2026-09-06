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
n=int(input("Enter n: "))
m=float(input("Enter capacity: "))
profits=list(map(float,input("Enter profits: ").split()))
weights=list(map(float,input("Enter weights: ").split()))
if len(profits)!=n or len(weights)!=n:
    raise ValueError("Number of profits and weights must match n.")
wp=[[0,0,0]]
for i in range(n):
    wp.append([weights[i],profits[i],i+1])
x=[0]*(n+1)
result=[]
for i in range(1,n+1):
    x[i]=1/(i+1)
wt,profit=printing()
result.append(["Initial",wt,profit,fraction_x(x[1:])])
wp=[[0,0,0]]+sorted(wp[1:],key=lambda w:w[0])
greedy(m,n)
wt,profit=printing()
result.append(["Weight",wt,profit,fraction_x(original_x())])
wp=[[0,0,0]]+sorted(wp[1:],key=lambda w:w[1],reverse=True)
greedy(m,n)
wt,profit=printing()
result.append(["Profit",wt,profit,fraction_x(original_x())])
wp=[[0,0,0]]+sorted(wp[1:],key=lambda w:w[1]/w[0],reverse=True)
greedy(m,n)
wt,profit=printing()
result.append(["Profit/Weight",wt,profit,fraction_x(original_x())])
for row in result:
    row[3]="\n".join(wrap(str(row[3])))
print(tabulate(result,headers=["Method","t wt","t profit","x"],tablefmt="grid"))