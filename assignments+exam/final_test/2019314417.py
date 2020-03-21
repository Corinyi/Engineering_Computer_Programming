filename = input("Enter a filename : ")
f = open(filename,"r")
a=0
for line in f:
    a=a+1
print("There are",a,"sales info.")
sale={}
f.close()

f = open(filename,"r")
for line in f:
    lst = line.strip()
    lst = lst.split()
    for b in range(len(lst)):
        if lst[b] in sale:
            sale[lst[b]]=sale[lst[b]] +1
        else:
            sale[lst[b]] = 1
f.close()
print("There are",len(sale.keys()),"unique items.")         
f.close()

print("""
1. Display top 10 best-sellers
2. Recommend an item
3. Disable a single item
4. Exit
""")
while True:
    menu = int(input("Select: "))
    if menu == 4:
        print(Exit)
        break
    elif menu==1:
        print("Top 10 best-seller items")


        print(sale)

