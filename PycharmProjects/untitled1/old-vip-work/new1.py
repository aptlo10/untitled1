fil=open('sample.txt','w')
fil.write('welcome hell world \n')
fil.write('pooooooooooooooo \n')
fil.close()

g=open('sample.txt','r')
text=g.read()
print(text)