
t = int(input("T:"))
list = []
if t > 0 and t <= 100:
    for i in range(0,t):
        
        while t > 0:
            k = int(input("N:"))
            if (k <= 100) and (k > 0):
                list.append(k)
                t = t - 1
                #print(t)
            else:
                print("out of range")

                

    for i in range(0,len(list)):
        p = 1
        x = int(list[i]) + 1
        for z in range(1,x):
            p = p*z
        print(p)

else:
    print("out of range")