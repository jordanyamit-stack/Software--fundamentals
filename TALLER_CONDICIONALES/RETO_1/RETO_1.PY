
import os 
from random import randint

dado1 = randint(1, 6)
dado2 = randint(1, 6)

print(f"Dado 1: {dado1} → {'PAR' if dado1 % 2 == 0 else 'IMPAR'}")
print(f"Dado 2: {dado2} → {'PAR' if dado2 % 2 == 0 else 'IMPAR'}")

if dado1 == dado2:
    print("YOU WIN")
else:
    print("GAME OVER")