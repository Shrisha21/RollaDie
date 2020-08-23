import random
min=1
max=6

while True:
    print("Wanna roll a die? (type Y for yes and N for No)")
    val=str(input())
    if(val=='Y' or val=='y'):
        print(random.randint(min,max))
        val='N'