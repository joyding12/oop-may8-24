#Oop Test for grad tracker

class Tap:
    tapmembers = 0
    progress_rate = 2
    cur_prog = 0

    __dept = "Not Declared"

    def __init__(self, first, last ,progress,__dept):
        self.first = first
        self.last = last
        self.progress = progress
        self.__dept = __dept
        #print("initialized")

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def set_dept(self, dept):
        self.__dept = dept

    def get_dept(self):
        return self.__dept
    
    def __len__(self):
        return len(self.first + self.last)
    
    def __str__(self):
        return f"{self.first} {self.last} : {self.progress}"
   

tap1 = Tap("Josh", "Peck", 0,"")
print(tap1)
print(tap1.full_name())
print(tap1.first)
tap1.set_dept("IT")
print(tap1.get_dept())
print(len(tap1))
print(str(tap1))

