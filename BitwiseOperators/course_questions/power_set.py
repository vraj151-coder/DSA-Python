def power_set(str):
    for i in range(pow(2,len(str))):
        idx=0
        print("'",end="")
        while i:
            if i&1==1:
                print(str[idx],end="")
            idx+=1
            i>>=1
        print("'",end="")
        print()


power_set("abc")