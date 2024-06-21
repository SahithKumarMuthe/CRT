user_name='Chandana_pingili'
password='Nani@8324'
print(" Enter Username : ")
u=input()
if u==user_name:
    p=input("Enter Password : ")
    if p!=password:
        print("invalid password .. 2 more chances left")
        p=input("Enter Password : ")
        if p!=password:
            print("invalid password .. 1 more chances left")
            p=input("Enter Password : ")
            if p!=password:
                print("invalid paasword your account has been blocked")
            else:
                print("Login successfull ..")  
                print("Welcome!!!!")
        else:
            print("Login successfull ..")  
            print("Welcome!!!!")
    else:
        print("Login successfull ..")  
        print("Welcome!!!!")
else:
    print("Invalid username.") 

    

        
