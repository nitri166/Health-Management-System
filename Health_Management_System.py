# 3 clients Garry , Shaun, Robert
# make 3 files to log their food
# make 3 file to log their exercise
# total 6 files
# func_log() writes in 6 files
# func_retrieve() shows whats in 6 files



# 2nd function to retrive data for any client
def getdate():
    import datetime
    return datetime.datetime.now()

def func_log():
    print("Choose your client 1- Garry, 2- Shaun, 3-Robert")
    input1 = int(input())
    if input1 == 1:
        print("Do you want to log exercise or food")
        print("Press \n 1 for exercise, 0 for food")
        var1 = int(input())
        if var1 == 1:
            print("Exercise you want to enter - ")
            Exe = input()
            with open("Garry_exer.txt", "a") as f:
                temp = getdate()
                f.write(str(temp)+" "+Exe+"\n")
               
            # showing the content of file
            with open("Garry_exer.txt","r") as x:
                print(x.read())

        elif var1 == 0:
            print("Food the client ate- ")
            Food = input()
            with open("Garry_food.txt","a") as f:
                temp = getdate()
                f.write(str(temp)+" "+Food+"\n")
            with open("Garry_food.txt","r") as x:
                print(x.read())      



    if input1 == 2:
        print("Do you want to log exercise or food")
        print("Press \n 1 for exercise, 0 for food")
        var1 = int(input())
        if var1 == 1:
            print("Exercise you want to enter - ")
            Exe = input()
            with open("Shaun_exer.txt", "a") as f:
                temp = getdate()
                f.write(str(temp)+" "+Exe+"\n")
                
            # showing the content of file
            with open("Shaun_exer.txt","r") as x:
                print(x.read()) 

        elif var1 == 0:
            print("Food the client ate- ")
            Food = input()
            with open("Shaun_food.txt","a") as f:
                temp = getdate()
                f.write(str(temp)+" "+Food+"\n")
            with open("Shaun_food.txt","r") as x:
                print(x.read())  

    if input1 == 3:
        print("Do you want to log exercise or food")
        print("Press \n 1 for exercise, 0 for food")
        var1 = int(input())
        if var1 == 1:
            print("Exercise you want to enter - ")
            Exe = input()
            with open("Robert_exer.txt", "a") as f:
                temp = getdate()
                f.write(str(temp)+" "+Exe+"\n")
                
            # showing the content of file
            with open("Robert_exer.txt","r") as x:
                print(x.read()) 

        elif var1 == 0:
            print("Food the client ate- ")
            Food = input()
            with open("Robert_food.txt","a") as f:
                temp = getdate()
                f.write(str(temp)+" "+Food+"\n")
            with open("Robert_food.txt","r") as x:
                print(x.read())                                






def func_retrieve():
    print("Choose your client 1- Garry, 2- Shaun, 3-Robert")
    input1 = int(input())
    if input1 == 1:
        print("Do you want to retrieve exercise or food")
        print("Press \n 1 for exercise, 0 for food")
        var1 = int(input())
        if var1 == 1:
            with open("Garry_exer.txt","r") as x:
                print(x.read())
        elif var1 ==0:
            with open("Garry_food.txt","r") as x:
                print(x.read())    

    elif input1 == 2:
        print("Do you want to retrieve exercise or food")
        print("Press \n 1 for exercise, 0 for food")
        var1 = int(input())
        if var1 == 1:
            with open("Shaun_exer.txt","r") as x:
                print(x.read())
        elif var1 ==0:
            with open("Shaun_food.txt","r") as x:
                print(x.read()) 

    elif input1 == 3:
        print("Do you want to retrieve exercise or food")
        print("Press \n 1 for exercise, 0 for food")
        var1 = int(input())
        if var1 == 1:
            with open("Robert_exer.txt","r") as x:
                print(x.read())
        elif var1 ==0:
            with open("Robert_food.txt","r") as x:
                print(x.read())                                        




print("Do you want to log the data or retrieve it")
initial = int(input("Press 1- lock and 0- retrieve \n"))
if initial == 1:
    func_log()
elif initial ==0:
    func_retrieve()



    