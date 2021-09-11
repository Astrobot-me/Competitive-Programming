
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
        sum = 0
        z = str(list[i])
        for q in range(0,len(z)):

            sum = sum + int(z[q])
        print(sum)


else:
    print("out of range")