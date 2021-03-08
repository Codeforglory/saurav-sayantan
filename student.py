
class Student:
   
   
    def __init__(self,name,Id,percentage,skills):
        self.name = name
        self.Id = Id
        self.percentage = percentage
        self.skills = skills
       
    def get_name(self):
        return self.name
   
    def get_Id(self):
        return self.Id
    def get_percentage(self):
        return self.percentage
    def get_skills(self):
        return self.skills
