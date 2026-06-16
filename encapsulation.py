class instagram:
    __password = "nandu@123" #privet
    __followers =500

    def change_password(self,old,new):
        if old ==self.__password:
            self.__password =new

            print ("password change succesfully")
        else:
            print("wrong passoword")

    def add_followers(self):
        self.__followers +=1
        print(f"new followers! total:{self.__followers}")

    def get_followers(self):
         print(f"followers:{self.__followers}")

    #object
acc = instagram()
acc.change_password("nandu@123","newpass@123")
acc.add_followers()
acc.get_followers()   

    #direct access nhi milega 

    # print(acc._password) #error
    # print(acc.__followers) #error


