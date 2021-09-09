n = int(input("Enter n:"))
k = int(input("Enter k:"))

inp_list = []

for i in range(1,n+1):
    z = int(input(f"enter the {i}th number:"))
    inp_list.append(z)


true_turns = 0

#print(inp_list)


for i in range(0,n):
    if inp_list[i]%k == 0:
        true_turns += 1

print(true_turns)
