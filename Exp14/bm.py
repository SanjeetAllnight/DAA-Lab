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