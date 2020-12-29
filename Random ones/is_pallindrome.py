def pal(string):
    return string==string[::-1]

s="Python--nohtyP"
ans=pal(s)

if ans:
    print("Yes it is pallindrome. ")
else:
    print("Not pallindrome. ")