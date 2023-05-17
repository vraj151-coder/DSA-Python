# def count_set_bits(num):
#     count=0
#     while(num>0):
#         num&=(num-1)
#         count+=1
#     return count

# def forRangeCount(num):
#     total_count=0
#     for i in range(1,num+1):
#         total_count+=count_set_bits(i)
#     return total_count

print(forRangeCount(17))