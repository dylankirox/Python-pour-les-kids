import random
num = random.randint(1,100)
score = 10
while True:
    if score == 0:
        print('Perdu!!!Game Over!!!')
        break
    score = score - 1
    print('Devine un nombre compris entre 1 et 100')
    a = input()
    i = int(a)
    if i == num:
        print('Tu as trouvé')
        print('Score: %i' % (score))
        break
    elif i < num:
        print('Essaie plus haut')
        print('Nombre de coup(s) restants: %i' % (score))
    elif i > num:
        print('Essaie plus bas')
        print('Nombre de coup(s) restants: %i' % (score))
        
