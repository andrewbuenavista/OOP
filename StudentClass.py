from datetime import date

class Student:


    def __init__(self,id,name,dob,classification):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification

    def set_age(self):       

        dobyear = self.__dob
        dobyear = dobyear.split('/')

        today = date.today()
        
        self.__age =  (int(today.year) - int(dobyear[2]))

    def set_registration(self,classification):
        if (classification.lower() == 'f'):
            self.__regdate =  "4/10 - 4/12"
        elif (classification.lower() == 's'):
            self.__regdate = "4/7 - 4/9"
        elif (classification.lower() == 'jr'):
            self.__regdate = "4/4 - 4/6"
        elif (classification.lower() == "sr"):
            self.__regdate = "4/1 - 4/3"
        else:
            self.__regdate = 'invalid'
        
    def get_age(self):
        return self.__age

    def get_registration(self):
        return "Your registratoin date is: " + self.__regdate