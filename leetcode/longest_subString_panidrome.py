s="cbbd"
t=s[::-1]
z={}
j=len(s)
for i in range(len(s)):
    for x in range(len(s)):
        if s[i]==t[x]:
            x1=s[i:j-x]
            z1=x1[::-1]
            if s[i:j-x]==z1:
                z.update({len(z1):z1})
                break
print(z.get(max(z.keys())))















for i in range(len(s)):
    # for x in range(len(s)):
    if s[i]==t[i]:
        x1=s[i:j-i]
        z1=x1[::-1]
        if s[i:j-i]==z1:
            z.update({len(z1):z1})
            break
print(z.get(max(z.keys())))