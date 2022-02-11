import random
input("Press enter for a squawk. ")
while True:
    sequence="01234567"
    input("".join(random.choices(sequence, k = 4)))
