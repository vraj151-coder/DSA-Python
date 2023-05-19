def palindrome_check(str, i=0):
    if i == len(str)//2:
        return True
    return (str[i] == str[len(str)-1-i]) and palindrome_check(str, i+1)


print(palindrome_check("abbcbba"))
