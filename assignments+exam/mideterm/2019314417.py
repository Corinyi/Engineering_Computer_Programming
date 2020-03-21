print("""
=========================
====2019314417 이윤서====
=========================
""")

user=[3,2,1,4]
com=[2,4,6,8]
while True:
    print("\nUser cards: " ,user)
    print("Com cards: ",com)

    print("1. discard a card")
    print("2. receive a card")
    print("3. confirm win/loss(upgraded)")
    dec=int(input("select menu: "))

    if dec ==1:
        cho1=int(input("Which card number to disacrd? "))
        if cho1 not in user:
            print("*It does not exist*")
            continue
        else:
            user.remove(cho1)

    elif dec ==2:
        if len(user) ==4:
            print("*Your hand is already full*")
            continue
        else:
            cho2=int(input("New Card information? "))
            if cho2 in user:
                print("*you already have the card*")
                continue
            else:
                user.append(cho2)
                continue

    else:
        user1=[]
        user1.append(user[0])
        user1.append(user[1])
        user1.append(user[2])
        user1.append(user[3])
        com1=[]
        com1.append(com[0])
        com1.append(com[1])
        com1.append(com[2])
        com1.append(com[3])

        user.sort()
        user.reverse()
        com.sort()
        com.reverse()


        if user[0]>com[0]:
            print("*User won*")
        elif user[0]<com[0]:
            print("*User lost*")
        else:
            if user[1]>com[1]:
                print("*User won*")
            elif user[1]<com[1]:
                print("*User lost*")
            else:
                if user[2]>com[2]:
                    print("*User won*")
                elif user[2]<com[2]:
                    print("*User lost*")
                else:
                    if user[3]>com[3]:
                        print("*User won*")
                    elif user[3]<com[3]:
                        print("*User lost*")
                    else:
                        print("*It is a draw*")
        user=user1
        com=com1
  
        ex=str(input("Do you want to play agian (y/n)? "))
        if ex == "n":
            print("good bye~~")
            break
        elif ex== 'y':
            continue

