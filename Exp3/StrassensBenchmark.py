import time
import random
import numpy as np
from tabulate import tabulate
def strassens(A,B,n):
    if n==2:
        p=(A[1,1]+A[2,2])*(B[1,1]+B[2,2])
        q=(A[2,1]+A[2,2])*B[1,1]
        r=A[1,1]*(B[1,2]-B[2,2])
        s=A[2,2]*(B[2,1]-B[1,1])
        t=(A[1,1]+A[1,2])*B[2,2]
        u=(A[2,1]-A[1,1])*(B[1,1]+B[1,2])
        v=(A[1,2]-A[2,2])*(B[2,1]+B[2,2])
        c11,c12=p+s-t+v,r+t
        c21,c22=q+s,p+r-q+u
        return np.array([[c11,c12],[c21,c22]])
    m=n//2
    A11=A[:m+1,:m+1]
    A12=A[:m+1,m:n+1]
    A21=A[m:n+1,:m+1]
    A22=A[m:n+1,m:n+1]
    B11=B[:m+1,:m+1]
    B12=B[:m+1,m:n+1]
    B21=B[m:n+1,:m+1]
    B22=B[m:n+1,m:n+1]
    p=strassens(A11+A22,B11+B22,m)
    q=strassens(A21+A22,B11,m)
    r=strassens(A11,B12-B22,m)
    s=strassens(A22,B21-B11,m)
    t=strassens(A11+A12,B22,m)
    u=strassens(A21-A11,B11+B12,m)
    v=strassens(A12-A22,B21+B22,m)
    C11=p+s-t+v
    C12=r+t
    C21=q+s
    C22=p+r-q+u
    return np.vstack((np.hstack((C11,C12)),np.hstack((C21,C22))))
def normal(A,B,n):
    C=np.zeros((n+1,n+1),dtype=int)
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                C[i,j]+=A[i,k]*B[k,j]
    return C
def benchmark(n):
    A=np.zeros((n+1,n+1),dtype=int)
    B=np.zeros((n+1,n+1),dtype=int)
    A[1:,1:]=np.random.randint(0,100,(n,n))
    B[1:,1:]=np.random.randint(0,100,(n,n))
    st=time.perf_counter()
    normal(A,B,n)
    en=time.perf_counter()
    normal_time=en-st
    st=time.perf_counter()
    strassens(A,B,n)
    en=time.perf_counter()
    strassen_time=en-st
    return normal_time,strassen_time
if __name__=="__main__":
    sizes=[32,64,128,256,512]
    rows=[]
    for n in sizes:
        normal_time,strassen_time=benchmark(n)
        rows.append([n,f"{normal_time:.6f}",f"{strassen_time:.6f}"])
    print(tabulate(rows,headers=["Size","Normal Multiplication","Strassens Multiplication"],tablefmt="grid"))