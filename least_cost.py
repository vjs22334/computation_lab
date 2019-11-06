intmax=1000

def check(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] < intmax:
                return 0
    return 1
   

mat = [[1, 9, 13, 36, 51], [24, 12, 16, 20, 1], [14, 33, 1, 23, 26]]
res = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

req = [100, 60, 50, 50, 40]
cap = [50, 100, 150]

cost = 0
cnt=1
sumreq=sum(req)
sumcap=sum(cap)
while sumreq!=0 and sumcap!=0:
    mn=1000
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]<mn:
                mn=mat[i][j]
                p=i
                q=j
           
    if (cap[p] <= req[q]):

        res[p][q] = cap[p]
        cost += res[p][q] * mat[p][q]

        if (cap[p] == req[q]):

            cap[p] = 0
            req[q] = 0
           
            for k in range(len(mat[0])):
                mat[p][k]=mat[p][k]+intmax;
            for x in range(len(mat)):
                mat[x][q]=mat[x][q]+intmax;

        else:
            req[q] -= cap[p]
            cap[p] = 0
            for k in range(len(mat[0])):
                mat[p][k]=mat[p][k]+intmax;
    else:

        res[p][q] = req[q]
        cost += res[p][q] * mat[p][q]

        cap[p] -= req[q]
        req[q] = 0
        for x in range(len(mat)):
                mat[x][q]=mat[x][q]+intmax;
    ch=check(mat)
    sumreq=sum(req)
    sumcap=sum(cap)

print(res)
print("Total cost : " + str(cost))