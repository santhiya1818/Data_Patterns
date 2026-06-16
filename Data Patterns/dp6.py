import math
x = int(input(""))
num = x
res = 0
while(True):
    num += 1
    if(num == 2):
        res = num
        break
    elif (num == 3):
        res = num
        break
    elif (num == 5):
        res = num
        break
    elif(num == 1):
        res+=2
        break
    elif(num % 2 != 0 and num % 3 != 0 and num % 5 != 0):
        res = num
        break
    for i in range(2,abs(int(math.sqrt(num)))):
        if num % i != 0 :
            res = num
print(res)