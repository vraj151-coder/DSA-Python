def max_and(num_list):
    max_val=0
    for i in range(len(num_list)):
        val=0
        for j in range(i+1,len(num_list)):
            val=num_list[i] & num_list[j]
            if val>=max_val:
                max_val=val
    return max_val

print(max_and([2,4,8,16]))

#O(n**2)