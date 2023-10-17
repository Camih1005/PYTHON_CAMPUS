n = int(input("English newspaper: "))
setEng = set()
for i in range(n):
    setEng.add(input())

n = int(input("French newspaper: "))
setFrench = set()
for i in range(n):
    setFrench.add(input())
    
result = setEng - setFrench
print("Student only English newspapers:", len(result))