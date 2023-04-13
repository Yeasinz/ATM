balance=250

while True:
  print("Welcome to Northern Frock")
  print("you are at the main menu")
  print("1-display balance")
  print("2- withdraw funds")
  print("3-dipost funds")
  print("9-return card")
  


  selection=input("please select a number from 1-9: ")
  if selection=="1":
    print(f"your current balance is £{balance}")
  
  elif selection == "2":
    withdrawal_list=["£10","£20","£30","£40","£50","£100","£200", "other amount"]
    index=0
    for withdrawal in withdrawal_list:
     print(index,withdrawal)
     index += 1

    withdrawal_amount=int(input("please select withdrawal amount:"))
    if withdrawal_amount== 0:
      if balance >= 10:
        balance =balance -10
      else:
        print("you have insufficient funds")
    elif withdrawal_amount== 1:
      if balance >=20:
        balance =balance -20 
      else:
        print("you have insufficient funds")
    elif withdrawal_amount== 2:
      if balance>= 30:
        balance =balance -30
      else:
        print("you have insufficient funds")
    elif withdrawal_amount== 3:
      if balance >=40:
        balance =balance -40
      else:
        print("you have insufficient funds")
    elif withdrawal_amount==4:
      if balance >= 50: 
        balance =balance -50
      else:
        print("you have insufficient funds")
    elif withdrawal_amount== 5:
      if balance >= 100:
        balance =balance -100
      else:
        print("you have insufficient funds")
    elif withdrawal_amount== 6:
      if balance >= 200:
        balance =balance -200
      else:
        print("you have insufficient funds")
    
    elif withdrawal_amount== 7:
      withdrawal_other=int(input("please enter the amount you like to withdraw in increments of £10:  "))
      if withdrawal_other % 10==0:
        if withdrawal_other  < balance and  withdrawal_amount  < balance :
           balance= balance -withdrawal_other
           print(balance)
        else: 
             print("you have insufficent balance for your withdrawal amount ")
      else:
        print("you can only withdraw in increments of £10,you will be send back to the main menu")
       
    if balance>0:
      print(f"your new balance is £{balance}")
  
  elif selection == "3":
    diposit_list=["£10","£20","£30","£40","£50","£100","£200", "other amount"]
    index=0
    for diposit in diposit_list:
      print(index,diposit)
      index += 1

    diposit_amount=int(input("please select diposit amount: "))
    if diposit_amount == 0:
        balance= balance+10
    elif diposit_amount == 1:
        balance=balance+20
    elif diposit_amount == 2:
        balance=balance+30
    elif diposit_amount == 3:
        balance=balance+40
    elif diposit_amount == 4:
        balance=balance+50
    elif diposit_amount == 5:
        balance=balance+100
    elif diposit_amount == 6:
        balance=balance+200
    elif diposit_amount == 7:
        diposit_other=int(input("please slect the amount you like to diposit in increments of £10: "))
        if diposit_other % 10 !=0:
          print("you can only diposit in increments of £10,you will be send back to the main menu")
        else:
          balance=balance+diposit_other
         
    print(f"your new balance is £{balance}")
  
  elif selection == "9":
    print("here is your card,")
    print("thank you for using Northern Frock, have a nice day!")
    break

  else:
    print("error please select the options provided in the main menu")

