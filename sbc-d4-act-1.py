list = []

for i in range(5):
    numbers = (input("Enter Number:")) 
    list.append(numbers) 

print("Enter 1 pag NAA 0 pag  WALA")
bossing = int(input("Naa si Boss?"))

if bossing == 0:
    list.pop(0)
    print(list)

elif bossing == 1:    
    list.pop()
    print(list)
    for i in range(2):
        list.append(input("Enter Number:"))
        print("insert to add,",list)
else:
    print("Enter again") 
