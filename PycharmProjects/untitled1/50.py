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

"""
 def details(self,name,age):
       self.n=name
       self.a=age
       print("the name is {} and the age is {}".format(name,age))

    def __init__(self):
        print("heloo world")
s1=student()

s1.details("hema",20)


s1=student

num1=int(input("enter number 1 "))
num2=int(input("enter number 2 "))

try:
    num3=num1/num2
    print(num3)
except:
    print("you cant didvide nummer my zero")


bo=open('c:/text/b.txt','w')
bo.write('this is the file i want to use it ')

bo.close()
bo=open('c:/text/b.txt','r')
bo.read()

bo.close()
bo=open('c:/text/b.txt','r')
bo.read()




for a in range(1,11):
    print('\n')
    input()
    for b in range(1,11):
        print(a,"x",b,"=",a*b)

import  time


password="ali"

for i in range(3):
    time.sleep(2)
    pwd=input("enter the password \n")
    j=2
    if (pwd==password):
        print("welocome")
        break
    else:
        print("wrong pass word, chances left",j-i)
        continue
else:

    print("try agian")

for a in range(1,11):
    print('\n')
    time.sleep(2)
    for b in range(1,11):
        print(a,"x",b,"=",a*b)

print("image one")
time.sleep(3)
print("image 2")
time.sleep(3)
print("image 3")
time.sleep(3)
import  my_model

my_model.addition(10,30)
my_model.sub(10,30)
my_model.times(10,20)
my_model.addition(30,40)


def addition(n1,n2):
    n3=n1 * n2
    print(n3)




addition(10,20)


def example():
    print(10)

example()

def name():
    n=input("enter the name")
    print(n)
name()

password="ali"

for i in range(3):
    pwd=input("enter the password \n")
    j=2
    if (pwd==password):
        print("welocome")
        break
    else:
        print("wrong pass word, chances left",j-i)
        continue
print("try agian")




name=input('enter your name \n')
age= int(input('enter your age \n'))

print("the name of the persone is ",name)

"""
