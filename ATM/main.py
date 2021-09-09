in_ammount = 120

i = int(input("Enter the Amount for Withdrawl:"))


print(f"Amount Left ${in_ammount - ((i//5)*5+0.5)}")