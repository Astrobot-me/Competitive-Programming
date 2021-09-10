#Write a program that accepts a number, n, and outputs the same.
list = []

while True:
    
    i = input("Integer or q:")
    if i == "q":
        break
    elif int(i)>105:
        print("out of Range")
    else:
        list.append(int(i))

for z in range(0,len(list)):
    print(list[z],end="")    