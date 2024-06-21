class Person:
    def __init__(self,name,age,roll_number,mail) -> None:
        self.name=name
        self.age=age
        self.roll_number=roll_number
        self.mail=mail

    def introduce(self,lang):
        print('hi my name is {0}\nam {1} years old\nmy roll number is {2} \nconnect with me via {3} my lanmguage is {4}'.format(self.name,self.age,self.roll_number,self.mail,lang))


c=Person("chandana",20,"2203A51L47","2203a51l47@sru.edu.in")
m=Person("manaswini",20,"l04","2203a51l04@sru.edu.in")
c.introduce("telugu")
m.introduce("english")