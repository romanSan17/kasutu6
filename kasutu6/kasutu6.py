#6
from random import *
number=[]
N=int(input("mitu numbrit on nimekirjas? "))
for o in range(N):
    number.append(randint(1,1000))
print(number)
max_num=max(number)
print("max numbri:", max_num)
kasutu=max_num / N
print("kasutu number:", kasutu)
index_max_num = number.index(max_num)
number[index_max_num] = kasutu
print("Numbrite loend pärast muutmist:", number)