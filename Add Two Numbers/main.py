#
t = int(input("T:"))
list = []
for i in range(0,t):
    k = input("A B :")
    
    list.append(k)

print(list)
for z in range(0,len(list)):
    q = str(list[z])
    m = q.split(" ")
    print(int(m[0])+int(m[1]))
   