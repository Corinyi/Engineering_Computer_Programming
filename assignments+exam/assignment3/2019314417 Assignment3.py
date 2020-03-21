import random 
import copy


def Print_list(stock_list):
    if len(stock_list)>0 and len(stock_list[0])==4:
        col = ['Type', 'Company', 'Price', 'Amounts']
        row_format ="{:>5}"+"{:>14}" * (len(col)-1)
        print(row_format.format(*col))
        print('-'*6, end='+')
        for p in range(len(col)-1):
            print('-'*14, end='+')
        print()
        for row in stock_list:
           print(row_format.format(*row))
    elif len(stock_list)>0 and len(stock_list[0])==5:
        col = ['Type', 'Company', 'Current price', 'Amounts', 'Payment price']
        col_num = [5,11,15,9,16]
        row_format ="{:>5}{:>12}{:>16}{:>10}{:>16}"
        print(row_format.format(*col))
        for num in col_num:
            print('-'*(num), end='+')
        print()
        for row in stock_list:
           print(row_format.format(*row))
    

def Buy_stock(market_stock, my_stock):
    # ========= YOUR CODE ========= #
    for x in range(len(my_stock)):
        del my_stock[x][5]
    while True:
        my_stock_tmp=[]
        stock_kind = int(input("Which stock do you want? ")) - 1
        stock_quantity = int(input("How many will you get? "))
        stock_keep = input("Will you continue to buy stock? (y/n) ")


        my_stock_tmp = market_stock[stock_kind][:3]
        my_stock_tmp.insert(3, stock_quantity)
        my_stock_tmp.insert(4,market_stock[stock_kind][2])
        my_stock.append(my_stock_tmp)

            
        market_stock[stock_kind][3]=(int(market_stock[stock_kind][3]) - stock_quantity)
        if stock_keep == 'n':
            break
        else:
            continue

    

    # ============================= #
    return market_stock, my_stock


def Update_my_stock(init_stock, my_stock):
    my_new_stock = copy.deepcopy(my_stock)
    # ========= YOUR CODE ========= #
    i=0
    j=0
    my_stock_new_money=[]
    for i in range(len(my_stock)):
        while True:
            if my_stock[i][0] == init_stock[j][0]:
                my_stock_new_money.append(init_stock[j][2])
                j=0
                break
            else:
                j+=1
    for x in range(len(my_stock)):
        my_new_stock[x][2]=my_stock_new_money[x]
    
    
    # ============================= #
    return my_new_stock


def Calculate_profit(my_stock):
    my_stock_profit = copy.deepcopy(my_stock)
    total_profit = 0
    # ========= YOUR CODE ========= #
    my_stock_profit=[]
    total_profit_tmp=[]
    for x in range(len(my_stock)):
        profit_tmp=(int(my_stock[x][2])-int(my_stock[x][4]))*int(my_stock[x][3])
        my_stock_profit.append(my_stock[x])
        my_stock_profit[x].append(profit_tmp)
    for x in range(len(my_stock)):
        total_profit_tmp.append(my_stock_profit[x][5])
    total_profit=sum(total_profit_tmp)  
 
    
        
    
    # ============================= #
    col = ['Type', 'Company', 'Current price', 'Amounts', 'Payment price', 'Profit']
    col_num = [5,11,15,9,15,10]
    row_format ="{:>5}{:>12}{:>16}{:>10}{:>16}{:>10}"
    print(row_format.format(*col))
    for num in col_num:
        print('-'*(num), end='+')
    print()
    for row in my_stock_profit:
        print(row_format.format(*row))
    return total_profit

 
def Sell_stock(market_stock, my_stock):
    # ========= YOUR CODE ========= #
    for x in range(len(market_stock)):
        market_stock[x][3]=50
    my_stock=[]    

            
    
    # ============================= #
    return market_stock, my_stock



market_stock = [[1, 'Bitcoin', 2000, 50],
                [2, 'Ddeok-lock', 100, 50],
                [3, 'Ddeok-sang', 9000, 50],
                [4, 'Samsung', 10000, 50],
                [5, 'Apple', 10000, 50],
                [6, 'LG', 8000, 50],
                [7, 'Mall-bbang', 5800, 50]]

my_stock = []

# 1. Input your object, maximum profit and minimum loss
max_profit = int(input('Your maximum profit? '))
min_loss = int(input('Your minimum loss? '))

while True:
    # 2. Print stock list and buy stocks
    print('\n\n=================================================== ')
    print('       SKKU Financial Investment Program ')
    print('=================================================== ')
    Print_list(market_stock)
    market_stock, my_stock = Buy_stock(market_stock, my_stock)

    print('\n\n=========================================================== ')
    print('      Thanks for your purchase! ')
    print('      Now your purchase list ')
    print('=========================================================== ')
    Print_list(my_stock)

    print('\n\n=================================================== ')
    print('      And rest of stocks in market ')
    print('=================================================== ')
    Print_list(market_stock)


    # 3. Change the stock price in market
    for i in range(len(market_stock)):
        market_stock[i][2]= random.randrange(1000,15000)

    print('\n\n=================================================== ')
    print('      After changing the price of stocks in market ')
    print('=================================================== ')
    Print_list(market_stock)


    # 4. Update my stock price
    my_stock = Update_my_stock(market_stock, my_stock)   

    print('\n\n=========================================================== ')
    print('      After update the price of my stock list ')
    print('=========================================================== ')
    Print_list(my_stock)


    # 5. Calculate profits
    print('\n\n=================================================== ')
    print('      Profits ')
    print('=================================================== ')
    total_profit = Calculate_profit(my_stock)
    print('\n    [Total profit]', total_profit,'Won')

    # 6. Compare profit with your initial profit boundary
    if total_profit > max_profit or total_profit < min_loss:
        market_stock, my_stock = Sell_stock(market_stock, my_stock)

        print('\n\n==================================================== ')
        print('      Now your purchase list ')
        print('==================================================== ')
        if my_stock == []:
            print('Empty.')
        else:
            Print_list(my_stock)

        print('\n\n=================================================== ')
        print('      And rest of stocks in market ')
        print('=================================================== ')
        Print_list(market_stock)
        
        break

