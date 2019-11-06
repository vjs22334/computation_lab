from sympy import symbols,diff,Eq,solve

x1, x2, l1, l2, s1, s2 = symbols('x1 x2 l1 l2 s1 s2', real=True)

f = (10*x1-x1**2+10*x2-x2**2) - l1*(x1+x2+s1**2-14) - l2*(-x1+x2+s2**2-6)


dfdx1 = diff(f, x1)
dfdx2 = diff(f, x2)
dfds1 = diff(f, s1)
dfds2 = diff(f, s2)
dfdl1 = diff(f, l1)
dfdl2 = diff(f, l2)


print(dfdx1)
print(dfdx2)
print(dfds1)
print(dfds2)
print(dfdl1)
print(dfdl2)

eq1 = Eq(dfdx1)
eq2 = Eq(dfdx2)
eq3 = Eq(dfdl1)
eq4 = Eq(dfdl2)
eq5 = Eq(dfds1)
eq6 = Eq(dfds2)

sol = solve((eq1,eq2,eq3,eq4,eq5,eq6),(x1,x2,l1,l2,s1,s2))
print("all solutions:")
print(sol)

ans=[]
for i in sol:
  if i[2] == 0 or i[3] == 0:
    pass
  else:
    print("final solution:")
    print(i)
    ans=i


dfdx1x1 = diff(dfdx1, x1)
dfdx1x2 = diff(dfdx1, x2)
dfdx2x2 = diff(dfdx2, x2)
dfdx2x1 = diff(dfdx2, x1)


#hessian matrix
print(" hessian matrix:")
hmatrix  = [[dfdx1x1,dfdx1x2],
            [dfdx2x1,dfdx2x2]]

print(hmatrix)

m1 = dfdx1x1

m2 = dfdx1x1*dfdx2x2 - dfdx1x2*dfdx2x1

print("principal minor:",m1)
print("det:",m2)

if m1>0 and m2>0:
  print("Local minima at ", ans[0], ans[1])
  print(ans[0]*10 - ans[0]**2+10*ans[1]-ans[1]**2)
elif m1<0 and m2>0:
  print("Local maxima at ", ans[0], ans[1])
  print(ans[0]*10 - ans[0]**2+10*ans[1]-ans[1]**2)
else:
  print("Saddle point")