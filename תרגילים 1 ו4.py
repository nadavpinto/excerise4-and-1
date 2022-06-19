#ecxercise4
#1,a

sum=0
d=0
def function1(tree,num):
  d=function1(tree.right,num)+function1(tree.left,num)
  if type(tree.data)==chr:
    num = chr(num)
  else:
    num = int(num)
  if tree.data==num:
    sum=sum+1
  if tree.left!=None and tree.right==None:
    return function1(tree.left,num)
  if tree.right!=None and tree.left!=None:
    return function1(tree.right,num)
  if tree.right!=None and tree.right!=None: 
    sum=sum+d
  return sum
  
#1,b
def function2(tree,num):
  for x in num:
    if function1(tree,x)>0:
      continue
    else:
      return false
  return true

#exercise1
#1
try:
  print(int(input("number "),16))
except ValueError:
  print("invaild hex number")
  
#2
str1=input("string ")
sum=0
str2="a"
arr=["a","b","c","d","e","f","A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"]
for x in range(0,len(str1)):
  if str1[x] in arr:
    str2=str2+str1[x]
  else:
    sum=sum+int(str2,16)
    str2=""
if len(str2) != 0:
  sum=sum+int(str2,16)
print(sum)
 
#3
def func():
  num = int(input("type num "))
  sum=0
  num1=1
  sum+=num
  try:
    while 1>0:
      num = int(input("type num "))
      num1=num1+1
      sum=sum+num
  except ValueError:
    return float(sum/num1)
