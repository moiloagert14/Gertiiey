#Gert Moiloa 46533605
#A program asking the the  user's church and give the rules

#printing out the main event of programe
print("RULES AMONGST CHURCHES")
print()

#asking the user to enter his/her church and is he/she baptised
church=input("Enter your church name(apostol/lutheran): ")
baptised=input("Are you baptised (Y/N): ")

#using while loop and if statement to write my conditions
while baptised =="Y":
    if church =="apostol":
        print("you cannot eat a pork")
        break
    elif church =="lutheran":
        print("you can eat everything")
        break
    else:
        break

