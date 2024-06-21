from authentication import Authentication

class passWord(Authentication):

    def authenticate(self):
        uname=input("Enter username : ")
        if uname==self.username:
            attempts=3
            while attempts>0:
                attempts-=1
                pswrd=input("Enter password : ")
                if pswrd==self.access():
                    print("Login successful !!")
                else:
                    if attempts>0:
                        print(f"incorrect password {attempts} more attempts left")
                    else:
                        print("Account blocked :(")
                        break
        else:
            print("Invalid username")
    


        