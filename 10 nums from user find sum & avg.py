#Write a program to read 10 numbers from the keyboard and find their sum and average.

a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(a)
sum=0
count=0
for i in(a):
    sum=sum+i
    count=count+1
    avg=sum/count
print(sum)
print(avg)
