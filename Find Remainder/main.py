# Write a program to find the remainder when an integer A is divided by an integer B.

t = int(input("T:"))
list = []
if t <= 1000 and t > 0:

    while t > 0:
       k = input("A B:")
       l = k.split(" ")
       if (int(l[0]) > 0 and int(l[0]) < 100000) and (int(l[1]) > 0 and int(l[1]) < 100000):
           list.append(k)
           t = t-1
       else:
           print("out of range")

        
    
    for i in range(0,len(list)):
        m = str(list[i])
        a = m.split(" ")
        print(int(a[0])%int(a[1]))


else:
    print("out of range")

   


