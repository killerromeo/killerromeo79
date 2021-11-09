fibbnoic series
n=int(input("Enter the number:"))
a=-1
b=1
for i in range(0,n):
  c=a+b
  print(c)
  a=b
  b=c

