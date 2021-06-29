def magicCows(cows,c,d):
  if d==0:
    return len(cows)
  if d<0:
    return None
  for i in range(len(cows)):
    cow=cows[i]
    if cow*2>c:
      cows.append(cow)
    else:
      cows[i]*=2
  return magicCows(cows,c,d-1)


print(magicCows([1,2,1,2,1],2,2))