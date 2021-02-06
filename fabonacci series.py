print("Fabonacci series with if else")
num=int(input("enter no. of fabonacci:- "))
a,b=1,1
res=0
if num==1:
    print(num)
elif num==2:
    print(a,b)
else:
    print(a,b,end=",")
    for i in range(num-2):
        res=a+b
        a,b=b,res
        print(res,end=",")


print("Fabonacci series with function")
def fab():
    res=a+b
    a,b=b,res
    print(res,end=",")

rng=int(input())
if num>1:
    fab(num)
else:print("1,1")
