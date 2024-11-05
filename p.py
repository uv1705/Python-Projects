import random
'''
1 snake
-1 water
0 gun

'''
computer=random.choice(1,0,-1)
yourstr=input("Enter your choice: ")
dict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you=dict(yourstr)
print()