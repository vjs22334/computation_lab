matrix=[[3,1,7,4],[2,6,5,9],[8,3,3,2]]
allocation=[[200,50,0,0],[0,250,100,0],[0,0,250,150]]

m=3
n=4
while 1:
     u=[0,-1,-1]
     v=[-1,-1,-1,-1]
     i=0
     while i<3:
          j=0
          while j<4:
               if v[j]==-1 and u[i]!=-1 and allocation[i][j]!=0:
                     v[j]=matrix[i][j]-u[i]
               if v[j]!=-1 and u[i]==-1 and allocation[i][j]!=0:
                     u[i]=matrix[i][j]-v[j]

               j=j+1
          i=i+1

     print u
     print v
     maxi=0
     x=0
     y=0

     for i in range (0,3):
          for j in range (0,4):
               if allocation[i][j]==0:
                    a=u[i]+v[j]-matrix[i][j]
                    if a>maxi:
                         maxi=a
                         x=i
                         y=j

     print x,y, maxi

     if maxi==0:
          break

     j=y+1
     while j<n:
          if allocation[x][j]!=0:
               i=x-1
               while i>=0:
                    if allocation[i][j]!=0:
                         if allocation[i][y]!=0:
                              break
                    i=i-1
               if i>=0:
                    break;
               else:
                    i=x+1
                    while i<m:
                         if allocation[i][j]!=0:
                              if allocation[i][y]!=0:
                                   break
                    i=i+1
          if i<m:
               break
          j=j+1
     if j>=n:
          j=y-1
          while j>=0:
               if allocation[x][j]!=0:
                    i=x-1
                    while i>=0:
                         if allocation[i][j]!=0:
                              if allocation[i][y]!=0:
                                break
                         i=i-1
                    if i>=0:
                         break;
                    else:
                         i=x+1
                         while i<3:
                              if allocation[i][j]!=0:
                                   if allocation[i][y]!=0:
                                        break
                              i=i+1
               if i<m:
                    break
               j=j-1

     print allocation[x][y],allocation[x][j],allocation[i][j],allocation[i][y]

     if allocation[x][j]<allocation[i][y]:
          r=allocation[x][j]
     else:
          r=allocation[i][y]


     allocation[x][y]=allocation[x][y]+r
     allocation[i][j]=allocation[i][j]+r
     allocation[x][j]=allocation[x][j]-r
     allocation[i][y]=allocation[i][y]-r

     print "Current Allocation",allocation

c=0
for i in range(0,m):
     for j in range(0,n):
          c=c+matrix[i][j]*allocation[i][j]

print "Answer=",c
