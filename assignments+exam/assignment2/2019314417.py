print("""
===============================
== Welcome! This is Cafe NU! ==
===============================""")

cou = 0
print("\n===============================")
print("Hello~. You have", cou, "coupons.")
while True:
    dr = int(input("How many drinks do you want? "))
    if dr == 0:
        print("Good bye~")
        break
    elif dr < 0:
        print("Wrong Input!")
        continue
    else:
        fdr = 0
        if cou >= 10:
            print("\n<<< 10 Coupons -> 1 Free drink >>>")
            while True:
                fdr = int(input("How many free drinks do you want? "))
                if  ((cou >= 10) and (fdr >= 0)) and (10*fdr <= cou) == True :
                    print("Okay. You use", 10*fdr, "coupons. Then you get", fdr, "free drkink(s)")
                    cou = cou-10*fdr
                    break
                if (fdr >0) and (10*fdr > cou):
                    print("You dont have enough coupons!")
                    continue
                if fdr < 0:
                    print("Wrong Input!")
                    continue
        print("You have to pay",2000*(dr-fdr), "and get", dr-fdr,"coupons! See you later~")
        cou = cou +dr -fdr
        print("===============================")
        print("\n===============================")
        print("Hello~. You have", cou, "coupons.")
            
                
                
                    
                    
            
            
