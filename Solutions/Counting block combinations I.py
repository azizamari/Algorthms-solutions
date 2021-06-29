# project euler 114
# not completely sure this is correct
def tiling(n,canRed=True,memo={}):
  if n==0:return 1
  if n<0:return 0
  if n in memo:return memo[n]
  memo[n]=tiling(n-1,True,memo)
  if canRed:
    for i in range(3,n+1):
      memo[n]+=tiling(n-i,False,memo)
  return memo[n]