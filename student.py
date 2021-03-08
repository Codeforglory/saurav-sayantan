class Student:
    def __init__(self, name, Id, percentage = 0, skills = []):
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

    def set_name(self, name):
        self.name = name

    def set_percentage(self, perct):
        self.percentage = perct

    def set_skill(self, skillsnew):
        self.skills = skillsnew

        
class Operation (Student):
    
    def __init__(self):
        Student.__init__(self,"saurav",1)

    def changeName(self, newName):
        self.set_name(newName)

    def changeNameUserInput(self):
        newName = input("Enter your new Name")
        self.set_name(newName)

    def addSkills(self,newSkills):
        self.set_skill(newSkills)
