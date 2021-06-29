def canSum(l,ta,memo={}):
  if ta==0:return True
  if ta<0:return False
  for i in l:
    x=ta-i
    if not x in memo:memo[x]=canSum(l,x,memo) 
    r=memo[x]
    if r:
      return True
  return False

  
print(canSum([7,14,23,6],15))