class student:
    def __init__(self, name):
        self.n = name
        self.attend = 0
        self.marks = []
        print("the name is {}".format(name))

    def add_markes(self, markss):
        self.marks.append(markss)

    def attendass(self):
        self.attend += 1

    def get_avg(self):
        return sum(self.marks) / len(self.marks)


s1 = student('hema')
s1.marks

s1.attendass()
s1.attend