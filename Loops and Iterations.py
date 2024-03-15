####Loops and Iterations
Number = [1,2,3,4,5,6]
for num in Number :
    print (num)

## Brake statement 

Number = [1,2,3,4,5,6]
for num in Number :
    if num == 4:
        print('Found!!')
        break
    print (num)

## Continue statement 

Number = [1,2,3,4,5,6]
for num in Number :
    if num == 4:
        print('Found!!')
        continue
    print (num)

## Loop with in a Loop.

Number = [1,2,3,4,5,6]
for num in Number:
    for Letters in 'abc':
        print(num , Letters)

Name =[',Bhushan , Avan , Divyansh, purvesh'] 
for num in Name:
    for Age in [23,24,25,26,]:
        print(num, Age)

## To justify the range in loop.

Name =['Bhushan,Avan,Divyansh,purvesh' ]
for num in Name:
    for Age in [23,24,25,26,]:
        print(num, Age)

## while loops 
# 
x = 0
while x>10:
   print(x)
x+=1

## Using the brake with while loop.

x=0
while x < 10:
  if x == 5:
     break
  print(x)
  x += 1

x=0
while x<10:
  if x==5:
      break
  print(x)
  x+=1

### This could also be used to rrach some instint of number.

x=1
while x<1000:
  if x==1000:
    break
  print(x)
  x+=1

## To print the exact number to an exact instenct
x=0
while True:
    if x== 1000:
       break
    print(x)
    x+=1

Number=4
for i in (1,2,3,4):
  if i==Number:
    print('Number is found',i)
    break



for i in (1,2,3,4,5,):
    if i == 3:
     continue
    print(i)
    