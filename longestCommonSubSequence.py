# def subSequence(s,cur="",i=0,ans=[]):
#     if i==len(s):
#         return ans
#     for k in range(i,len(s)):
#         ans.append(cur+s[k])
#         ans=subSequence(s,cur+s[k],k+1,ans)
#     return ans

# def longestCommonSubSequence(s1,s2):
#     subseq1=subSequence(s1,"",0,[])
#     subseq2=subSequence(s2,"",0,[])
#     max_len=0
#     max_str=""
#     for subs in subseq1:
#         if subs in subseq2:
#             if len(subs)>max_len:
#                 max_len=len(subs)
#                 max_str=subs

#     print(max_len,max_str)
# longestCommonSubSequence("abcd","axbdc")

def longestSubSequencelength(s1,s2):
    dp=[]
    for i in range(len(s2)+1):
        dp.append([0]*(len(s1)+1))
    i=1
    while i<(len(s2)+1):
        j=1
        while j<(len(s1)+1):
            if s1[j-1]==s2[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
            j+=1
        i+=1
    print(dp)
    longestSubSequence(dp,s1,s2)

def longestSubSequence(dp,s1,s2):
    i=len(dp)-1
    s=""
    j=len(dp[0])-1
    while j>0:
        if dp[i][j]==max(dp[i-1][j],dp[i][j-1]):
            if dp[i-1][j]>dp[i][j-1]:
                i=i-1
            else:
                j-=1
        else:
            s+=s1[j-1]
            i-=1
            j-=1
        if dp[i][j]==0:
            break
        
    print(s[::-1])
    

longestSubSequencelength("abcd","axbd")