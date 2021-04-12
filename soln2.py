def maxEvenDig(dig):
    dig=sorted(dig,reverse=True)
    minEvenDig=-1
    for i in range(len(dig)-1,-1,-1):
        if int(dig[i])%2==0:
            minEvenDig=dig[i]
            dig.pop(i)
            dig.append(minEvenDig)
            return ''.join(dig)
    return -1
if __name__=="__main__":
    str1=input()
    dig=""
    for i in str1:
        if i.isdigit():
            dig+=i
    res=maxEvenDig(dig)
    print(res)