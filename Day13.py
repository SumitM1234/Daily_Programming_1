def longest_palindromic_substring(s):
    check_list = []
    for i in range(0,len(s)):
        for j in range(len(s)-1,-1,-1):
            check = s[i:j+1]
            if(check==check[::-1]):
                check_list.append(check)
    if(len(check_list)==0):
        return s[0]
    else:
        return max(check_list, key =len)
s = "abc"
print(longest_palindromic_substring(s))
