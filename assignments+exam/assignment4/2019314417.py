def load_menu():
    global Menu
    Menu = []
    #========= STEP 1 ==========
    f=open("menu.txt","r")
    for line in f:
        menu = line.split()
        Menu.append(menu[0])
        print(menu[0]+" : "+menu[1]+" won")
    f.close()
    #========= STEP 1 ==========

    return Menu



def error_check(date):
    global menu_price
    #========= STEP 3 ==========
    f=open("menu.txt","r")
    menu = []
    menu_price = []
    for line in f:
        menu_name = line.split()
        menu.append(menu_name[0])
        menu_price.append(menu_name[1])
    f.close()
    f = open(name_e,"r")
    g = open(name_e_c,"w")
    h = open(sum_e_c,"w")
    h.write("No.\tMenu_NAme\tNum\tTotal\n")
    g.close()
    h.close()
    g = open(name_e_c,"a")
    h = open(sum_e_c,"a")
    for line in f:
        name_E = line.split()
        name_Ele = name_E[0]+"\t"+name_E[1]+"\t"+name_E[2]+"\t"+name_E[3]+"\n"
        if name_E[1] not in menu:
            g.write(name_Ele)
        else:
            for a in range(len(menu)):
                if name_E[1] == menu[a]:
                    name_E[3] = str(int(name_E[2])*int(menu_price[a]))
                    name_Ele = name_E[0]+"\t"+name_E[1]+"\t"+name_E[2]+"\t"+name_E[3]+"\n"
                    h.write(name_Ele)
    h.close()
    f.close()
    g.close()
       
    #========= STEP 3 ==========
    return menu_price

def calculate_total_income(date):

    #========= STEP 4 ==========
    print("\n"+"="*10+"Total Sales"+"="*10)
    f = open(sum_e_c,"r")
    list1=[0,0,0,0,0]
    for a in f:
        line = a.split()
        for h in range(len(Menu)):
            if line[1] == Menu[h]:
                list1[h]=(int(list1[h])+int(line[2]))
    for h in range(len(Menu)):
        print(Menu[h]+" : "+str(list1[h]))
    print("="*31)
    tot_sum=0
    for h in range(len(Menu)):
        tot_sum+=int(menu_price[h])*list1[h]
    print("Total Income : "+str(tot_sum)+" won.")
    
    
    #========= STEP 4 ==========


MENU = load_menu()
while True:
    # load and error check
    date = input("The date of ledger file : ")
    name_e = "ledger_"+date+".txt"
    name_e_c = "ledger_"+date+"_name_error.txt"
    sum_e_c = "ledger_"+date+"_corrected.txt"
    #in error_check make 2 more files
    #   -> _corrected.txt and _name_error.txt
    error_check(date)

    calculate_total_income(date)
    print("")


    
