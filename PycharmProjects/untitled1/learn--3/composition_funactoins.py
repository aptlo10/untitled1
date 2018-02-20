def factorial(n):
    if n==1:
        return 1
    else:
        return n *factorial(n-1)

print(factorial(5))

def sum(n):
    if n ==1:
        return 1
    else:
        return n+sum(n-1)


"""


def scope(a):
    a=a+1
    print(a)
    return a

scope(5)


def parmeter(a):
    print(a)

parmeter(10)

def def_parma(a,b=4,c=5):
    return a+b+c
result=def_parma(3)

print(result)

def fun():
    print("poo")

fun()

def returing():
    return "hooooooo"

print(returing())

def multival():
    return "this is a result",2

print(multival())
"""