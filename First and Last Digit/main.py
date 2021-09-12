
t = int(input("T:"))
list = []
if t > 0 and t <= 1000:
    for i in range(0,t):
        
        while t > 0:
            k = int(input("N:"))
            if (k <= 1000000) and (k > 0):
                list.append(k)
                t = t - 1
                #print(t)
            else:
                print("out of range")

                

    for i in range(0,len(list)):
        z = str(list[i])
        x = z[-1]
        y = z[0]
        print(int(x)+int(y))
        


else:
    print("out of range")