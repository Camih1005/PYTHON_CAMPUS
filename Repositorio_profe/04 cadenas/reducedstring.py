def superReducedString(s):
    news = ""
    slen = len(s)
    reduced = True
    while slen > 0 and reduced:
        i = 0
        reduced = False
        while i < slen:
            if i < slen-1 and s[i] == s[i+1]:
                i += 1
                reduced = True
            else:
                news += s[i]
                
            i += 1
            
        s = news
        slen = len(s)
        news = ""
    
    if s != "":
        return s
    else:
        return "Empty String"
    

# str = "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
# rta= "tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
# str = "oolaa"
# rta = "l"

str = "baab"
rta = "Empty String"

print(str)
print(superReducedString(str))
print(rta)