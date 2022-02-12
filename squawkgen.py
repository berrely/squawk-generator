import random
input("Press enter for a squawk. ")
genSquawks=[]
sequence="01234567"
while True:
    squawk="".join(random.choices(sequence, k = 4))
    if squawk in genSquawks:
        continue
    else:
        genSquawks.append(squawk)
        input(squawk)
