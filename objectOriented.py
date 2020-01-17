class Person:

    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age

    def pronouce_your_name(self):
        return self.firstname    


    def  set_first_name(self,new_name):
        self.firstname=new_name

    def set_last_name(self,new_name) :
        self.lastname=new_name 

    def set_age(self,new_age):
        self.age=new_age 


    def get_first_name(self):
        return self.firstname 


    def get_last_name(self):
        return self.lastname 

    def get_age(self):
        return self.age

    def __str__(self):
        return "Firstname: "+self.firstname+ "\n Lastname: "+self.lastname    

class Student(Person):

    def __init__(self,fname,lname,age,student_no,program):
         super().__init__(fname,lname,age) 
         self.student_number=student_no 
         self.program_of_study=program
      
    def __str__(self):
        return super().__str__() + "\n Student Number:"+ str(self.student_number)+"\n Program of Study: "+self.program_of_study


if  __name__ == "__main__":
    Pers1=Person('Akola','Mbey Denis',22)
    pers2=Student('Musah','Seidu',34,2045675,'Technical Skills')
    print(Pers1)
    print(pers2)
   


