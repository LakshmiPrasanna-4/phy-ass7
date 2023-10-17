# Write a program to print the given number is a prime number or not

n=int(input('Enter a value:'))
i=1
c=0
while(i<=n):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print('Given number is a Prime number')
else:
    print('Given number is not a Prime number')

