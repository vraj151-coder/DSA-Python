def lcm(num1,num2):
    max_num=max(num1,num2)
    multiple=1
    while True:
        if max_num==num1:
            if (num1*multiple)%num2==0:
                return num1*multiple
        else:
            if (num2*multiple)%num1==0:
                return num2*multiple
        multiple+=1

print(lcm(7,3))