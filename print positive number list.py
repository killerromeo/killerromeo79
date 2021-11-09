list1=[12,-7,5,64,-14]
print("list=[12,-7,5,64,-14]")
positive=()
for i in list1:
  if i>0:
    positive+=(i,)
print("positive numbers in list1=",positive)

list2=[12,14,-95,3]
print("list2=[12,14,-95,3]")
positive=()
for i in list2:
  if i>0:
    positive+=(i,)
print("positive numbers in list2=",positive)
