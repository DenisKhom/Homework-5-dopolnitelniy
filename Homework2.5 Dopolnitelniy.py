import random
key1 = range (3, 20)
i = random.choice(key1)
if i%2 == 0:
    a=int(i/2)
if i%2 !=0:
    a=int(i//2+1)
#print(i)
#print(a)
key = []
Kod=input('Ставь "+", если хочешь получить код   ')
if Kod== '+':
    for j in range (1,a):
        m = j + 1
        for n in range (m,i):

            if j!=n and i%(j+n)==0:
                key += (j,n)

    print(i,'-', *key)
else:
    print('Ну не хочешь, как хочешь')

