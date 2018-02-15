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



"""

import tuna
import random


tuna.fish()

x= random.randrange(1,100)
print(x)

"""