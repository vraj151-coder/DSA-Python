def odd_occuring(list_num):
    appeared=""
    for num in list_num:
        count=0
        for num_compare in list_num:
            if num_compare==num:
                count+=1
        if count%2!=0 and str(num) not in appeared:
            print(num)
            appeared+=str(num)


odd_occuring([8,7,7,8,8])
            

