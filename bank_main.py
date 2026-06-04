import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:  
            print("no such file exist")

    except Exception as err:
        print(f"an exception occured as {err}")
       
    @staticmethod
    def __update():
        with open(Bank.database ,"w") as fs:
            json.dump(Bank.data, fs, indent=4)
            
    @classmethod
    def __accountgenrate(cls):
        num = random.choices(string.digits,k = 12,)
        random.shuffle(num)
        return "".join(num)
    
    def creatingaccount(self):
        info = {
            "name"  : input("tell your name :- "),
            "age"   : int(input("tell your age :- ")),
            "email" : input("tell your email :- "),
            "pin"   : int(input("tell your 4 number pin :- ")),
            "accountNo" : Bank.__accountgenrate(),
            "balance"   : 0
        }
        if info["age"] <18 or len(str(info["pin"])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("please note down your account number")
            
            Bank.data.append(info)
            Bank.__update()
            
    def depositmoney(self):
        accnumber = (input("tell me your account number :- "))
        pinnumber = int(input("tell me your pin number :- "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pinnumber]
        if not userdata:
            print("Sorry no data found")
            
        else:
            amount = int(input("how much you amount want to deposite :-"))
            if amount > 100000 or amount <= 0:
                print("sorry the amount is too much you can deposite bellow 100000 and above 0 ")
                
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")
                print("Current Balance:", userdata[0]['balance'])
    
    def withdrawmoney(self):
        accnumber = (input("tell me your account number :- "))
        pinnumber = int(input("tell me your pin number :- "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pinnumber]
        if not userdata:
            print("Sorry no data found")
            
        else:
            amount = int(input("how much you amount want to withdraw :-"))
            if amount > 100000 or amount <= 0:
                print("sorry the amount is too much you can withdraw bellow 100000 and above 0 ")
                
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdraw successfully")
                print("Current Balance:", userdata[0]['balance'])
                
    def checkbalance(self):
        accnumber = (input("tell me your account number :- "))
        pinnumber = int(input("tell me your pin number :- "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pinnumber]
        if not userdata:
            print("Sorry no data found")
            
        else:
            print("Current Balance:", userdata[0]['balance'])
    
    def showdetails(self):
        accnumber = (input("tell me your account number :- "))
        pinnumber = int(input("tell me your pin number :- "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pinnumber]
        if not userdata:
            print("Sorry no data found")
            
        else:
            print("your information are \n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
                
    def updatedetails(self):
        accnumber = (input("tell me your account number :- "))
        pinnumber = int(input("tell me your pin number :- "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pinnumber]
        if not userdata:
            print("Sorry no data found")
            
        else:
            print("Note:-")
            print("you cannot change your age, account number, balance")
            print("Fill the details for change or leave it empty if no change")
            
            newdata = {
                "name" : input("tell your new name or press enter to skip :- "),
                "email": input("tell your new email or press enter to skip :- "),
                "pin" : input("tell your new pin or press enter ro skip :- ")
            }
            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
                
            newdata['age'] = userdata[0]['age']
            newdata["accountNo"] = userdata[0]["accountNo"]
            newdata["balance"] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata["pin"] = int(newdata["pin"])
                
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            Bank.__update()
            print("details updated successfully")
            
    def deleteaccount(self):
        accnumber = (input("tell me your account number :- "))
        pinnumber = int(input("tell me your pin number :- "))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pinnumber]
        if not userdata:
            print("Sorry no data found")
            
        else:
            check = input("press y if you actually delete the account or press n :- ")
            if check == 'n' or check == 'N':
                print("bypassed")
            elif check == 'y' or check == 'Y':
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()
         
user = Bank()
print("press 1 for Creating an account")
print("press 2 for Deposite money in the bank")
print("press 3 for Withdraw money")
print("press 4 for Cheak Balance")
print("press 5 for Show Details")
print("press 6 for updating the Details")
print("press 7 for Deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.creatingaccount()
    
elif check == 2:
    user.depositmoney()
    
elif check == 3:
    user.withdrawmoney()
    
elif check == 4:
    user.checkbalance()
    
elif check == 5:
    user.showdetails()
    
elif check == 6:
    user.updatedetails()
    
elif check == 7:
    user.deleteaccount()