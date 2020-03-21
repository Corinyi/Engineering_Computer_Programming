print ("Assignment1 - Dutch pay(1/n) Calculator")
tot = int(input("How much was the food? : "))
ppl = int(input("How many are you? : "))
money = int(((tot/100)//ppl)*100)
print ("Each of you will pay", money, "won")
remain = str(tot - money*ppl)
print ("Who's going to pay the rest of the money("+remain+" won)?")

