def isPalindrome(s,strt,end):
    if strt>=end:
        print(s)
        return True
    if s[strt]==s[end]:
        isPalindrome(s,strt+1,end-1)
    else:
        return False
    


#navie approach

def longestPalindromicSubstring(s):
    i=0
    max_len=0
    sub=""
    while i<len(s):
        j=i+1
        
        while j<len(s):
            print(s[i:j])
            if isPalindrome(s[i:j+1],i,j-1) is True:
                if j-i>max_len:
                    max_len=j-i
                    sub=s[i:j+1]
            j+=1
        i+=1
    print(sub,max_len)

print(longestPalindromicSubstring("Chandana"))
    

