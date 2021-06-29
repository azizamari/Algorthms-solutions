def grid(m,n,mem={}):
  if (n,m) in mem:return mem[(n,m)]
  if (m,n) in mem:return mem[(m,n)]
  if m==0 or n==0:return 0
  if m==1 or n==1:return 1
  mem[(m,n)] =grid(m-1,n,mem)+grid(m,n-1,mem)
  mem[(n,m)]=mem[(m,n)]
  return mem[(m,n)]


print(grid(2,3))
print(grid(18,18))