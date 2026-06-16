"=====Expense Tracker====="
ListExpensis=[]
while True:
    print("=====Welcom to the Expense Tracker=====")
    print(" --- 1 ---  press for add expensis:>")
    print(" --- 2 ---  press for check detail about expensis( like category,-->amount,date):")
    print(" --- 3 ---  press for check total amount :>")
    print(" --- 4 ---  press for exit:>")

   

    choice=int(input("Enter your choise:"))
# ===== for add the expensise ========
    if choice==1:
        category=input("enter your category(--- like , food, clothes, makup,etc----):>")
        date=int(input("enter your date:>"))
        amount=float(input("Enter your amout of expense:>"))
        
        dict_expense={
            "Category":category,
            "Date":date,
            "Amount":amount 
            }
        ListExpensis.append(dict_expense)
        print(ListExpensis)
#  ======= for veiw all expensise======= 
    elif choice==2:
        if len(ListExpensis)==0:
            print("zero expensis:>")
        else:
            count=1
            for expenses in ListExpensis:
                print(f"expenses no.{count}--->{expenses['Date']},{expenses['Category']},{expenses['Amount']}")
                count+=1

# ======= for veiw total amount========

    elif choice==3:
        total=0
        for expenses in ListExpensis:
            total=total+expenses["Amount"]

        print( f"lo ji kar diya karche {total} rupeee")
    




    elif choice==4:
        print("Thank for coming:>")
        break

    else:
        print("Invalid choice:")
        print("Try again")
    
    
    