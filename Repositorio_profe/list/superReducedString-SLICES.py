def superReducedString(s):
    while True:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i]+s[i+2:]
                break
        else:
            break
    return s if s else "Empty String"


# programa prueba
str = "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
rta= "tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
# str = "oolaa"
# rta = "l"

# str = "baab"
# rta = "Empty String"

print(str)
print(superReducedString(str))
print(rta)

# s = ""
# for i in range(len(s)):
#     print(s[i], end=", ")
#     break
# else:
#     print("Evaluo pero No entro al for")