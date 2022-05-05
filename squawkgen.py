import random
input("Press enter for a squawk. ")
genSquawks=[]
emergency=[7500,7600,7700]
sequence="01234567"
while True:
    squawk="".join(random.choices(sequence, k = 4))
    if squawk in genSquawks or squawk in emergency:
        continue
    else:
        genSquawks.append(squawk)
        input(squawk)
