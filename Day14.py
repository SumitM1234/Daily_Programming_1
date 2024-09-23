def check_unique(val,res_count):
    unique_val = set(val)
    count = len(unique_val)
    if(count==k):
        res_count.append(val)

def count_distinct(s):
    res_count = []
    for i in range(len(s)):
        for j in range(len(s)-1,-1,-1):
            check_unique(s[i:j+1],res_count)
    return len(res_count)


k = 4
p = "abc"
print(count_distinct(p))
