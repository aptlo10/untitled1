class Enemy:
    life=3

    def attack(self):
        print('ouche')
        self.life-=1
    def checklife(self):
        if self.life<=0:
            print('a am dead')
        else:
            print(str(self.life)+"life left")

enemy1=Enemy()
enemy2=Enemy()

enemy1.attack()
enemy1.attack()

enemy1.checklife()
enemy2.checklife()



"""

while True:
    try:
        number=int(input("what is your age \n"))
        print(1/number)
        break
    except ValueError:
        print("erorr in insertion ")
    except  ZeroDivisionError:
        print("dont divided by zero")
    except:
        break
    finally:
        print("loop compltee ")

import tuna
import random


tuna.fish()

x= random.randrange(1,100)
print(x)

"""