def prime(n):
  x=0
  for i in range(2,n//2+1):
    if n%2==0:
      x=1
      break
  if x==0:
    print(n,end=",")
li=[55,98,56,87,13,78,11,20,7,19,9]    
for num in li:
  prime(num)
