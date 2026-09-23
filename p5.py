
class father:
    def skill (self):
        print("Driving")

class mother :
    def skill2(self):
        print("cooking")

class child(father,mother):
    def skill3(self):
        print("gaming")

c=child()
c.skill()
c.skill2()
c.skill3()