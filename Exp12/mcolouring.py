n=5
m=3
G=[
[0,0,0,0,0,0],
[0,0,1,1,1,0],
[0,1,0,1,1,1],
[0,1,1,0,0,0],
[0,1,1,0,0,0],
[0,0,1,0,0,0]
]
x=[0]*(n+1)
count=0
def NextValue(k):
    while True:
        x[k]=(x[k]+1)%(m+1)
        if x[k]==0:return
        for j in range(1,n+1):
            if G[k][j]!=0 and x[k]==x[j]:break
        if j==n:return
def mColoring(k):
    global count
    while True:
        NextValue(k)
        if x[k]==0:return
        if k==n:
            print(x[1:n+1])
            count+=1
        else:mColoring(k+1)
def main():
    try:
        print("Possible color assignments:")
        mColoring(1)
        print("Total solutions:",count)
    except RecursionError:
        print("Recursion limit exceeded")
if __name__=="__main__":main()