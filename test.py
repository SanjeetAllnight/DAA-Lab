
def KMPFailureFunction(P):
    m=len(P)
    f=[0]*m
    i=1
    j=0
    while i<m:
        if P[j]==P[i]:
            f[i]=j+1
            i+=1
            j+=1
        elif j>0:
            j=f[j-1]
        else:
            f[i]=0
            i+=1
    return f

def KMPMatch(T,P):
    n=len(T)
    m=len(P)
    f=KMPFailureFunction(P)
    i=0
    j=0
    while i<n:
        if P[j]==T[i]:
            if j==m-1:
                return i-m+1
            i+=1
            j+=1
        elif j>0:
            j=f[j-1]
        else:
            i+=1
    return "There is no substring of T matching P."

def main():
    P=input("Enter pattern: ")
    T=input("Enter text: ")
    f=KMPFailureFunction(P)
    print("Failure Function:",f)
    result=KMPMatch(T,P)
    print("Result:",result)

if __name__=="__main__":
    main()



def LastFunction(P):
    last={}
    for i in range(len(P)):
        last[P[i]]=i
    return last

def BMMatch(T,P):
    n=len(T)
    m=len(P)
    last=LastFunction(P)
    i=m-1
    j=m-1
    while i<n:
        if P[j]==T[i]:
            if j==0:
                return i
            else:
                i-=1
                j-=1
        else:
            i=i+m-min(j,1+last.get(T[i],-1))
            j=m-1
    return "There is no substring of T matching P."

def main():
    P=input("Enter pattern: ")
    T=input("Enter text: ")
    print("Last Function:",LastFunction(P))
    print("Result:",BMMatch(T,P))

if __name__=="__main__":
    main()

