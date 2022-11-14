import random
def ordenar():
    num=[]
    for i in range(10):
        num.append(random.randint(1, 100))
    num.sort()
    print(num)
ordenar()