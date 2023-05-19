def generate_subsets(str, curr="", i=0):
    if i == len(str):
        print("'", end="")
        print(curr, end="")
        print("'")
        return

    generate_subsets(str, curr, i+1)
    generate_subsets(str, curr+str[i], i+1)


generate_subsets("abc")
