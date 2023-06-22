text = "I'm learning Python. It's interesting!"
pattern = "python"
tn = len(text)
pn = len(pattern)
flg = False
p = 0

uptext = text.upper()
uppattern = pattern.upper()
while p <= tn-pn:
    c = 0
    for i in range(pn):
        if uptext[p+i] != uppattern[i]:
            break
        c += 1
    if c == pn:
        flg = True
        break
    p += 1

print(text)
if flg == True:
    print(str(p+1)+"文字目に類似する文字列が見つかりました")
else:
    print(pattern+"は見つかりませんでした")