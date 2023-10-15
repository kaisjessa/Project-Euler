import re

def re_contain(a, b):
    return re.search(a,b) is not None

with open("p079_keylog.txt", 'r') as f:
    subs = []
    for l in f.readlines():
        subs.append(l.strip())
#print(subs)
subs = [f"[{sub[0]}].*[{sub[1]}].*[{sub[2]}]" for sub in subs]

s = 1
found = False
while(not found):
    foundnow = True
    t = "73"+str(s)
    for sub in subs:
        if(not re_contain(sub, t)):
            foundnow = False
            s += 1
            break
    found = foundnow
print(t)