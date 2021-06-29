
def howSum(l,ta):
  if ta==0:return []
  if ta<0:return None
  for i in l:
    remainder=ta-i
    result=howSum(l,remainder)
    if result is not None:
      return result+[i]
  return None

  
print(howSum([7,14,23,1],15))