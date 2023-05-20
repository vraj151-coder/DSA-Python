def power_set(str,curr="",i=0,arr=[]):
    if i>len(str):
        return
    if i==len(str):
        arr.append(curr)
        return
    power_set(str,curr,i+1,arr)
    power_set(str,curr+str[i],i+1,arr)
    return arr

print(power_set("abc"))