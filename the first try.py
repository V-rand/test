import numpy as np
def dis_abs(x,y):
    return abs(x-y)
def estimate_twf(A,B,dis_fun=dis_abs):

    N_A=len(A)
    N_B=len(B)

    D=np.zeros([N_A,N_B])
    D[0,0]=dis_fun(A[0],B[0])

    for i in range(1,N_A):
        D[i,0]=D[i-1,0]+dis_fun(A[i],B[0])

    for j in range(1,N_B):
        D[0,j]=D[0,j-1]+dis_fun(A[0],B[j])

    for i in range(1,N_A):
        for j in range(1,N_B):
            D[i,j]=dis_fun(A[i],B[j])+min(D[i-1,j],D[i,j-1],D[i-1,j-1])
    i=N_A-1
    j=N_B-1
    count=0
    d=np.zeros(max(N_A,N_B)*3)
    path=[]
    while True:
        if i>0 and j>0:
            path.append((i,j))
            m=min(D[i-1,j],D[i,j-1],D[i-1,j-1])
            if m==D[i-1,j-1]:
                d[count]=D[i,j]-D[i-1,j-1]
                i=i-1
                j=j-1
                count=count+1

            elif m==D[i,j-1]:
                d[count] = D[i, j] - D[i, j - 1]
                j=j-1
                count=count+1

            elif m==D[i-1,j]:
                d[count] = D[i, j] - D[i-1, j]
                i=i-1
                count=count+1

        elif i==0 and j==0:
            path.append((i, j))
            d[count] = D[i, j]
            count = count + 1
            break


        elif i==0:
            path.append((i, j))
            d[count] = D[i, j] - D[i, j - 1]
            j = j - 1
            count = count + 1

        elif j == 0:
            path.append((i, j))
            d[count] = D[i, j] - D[i - 1, j]
            i = i - 1
            count = count + 1
    mean =np.sum(d)/count
    return mean,path[::-1],D[::-1]

a=np.array([1,3,4,9,8,2,1,5,7,3])
b=np.array([1,6,2,3,0,9,4,1,6,3])
a=a[:,np.newaxis]
b=b[:,np.newaxis]
dis,path,D=estimate_twf(a,b,dis_fun=dis_abs)

print(dis)
print(path)
print(D)
