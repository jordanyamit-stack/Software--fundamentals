#TRABAJO DE CLASE DIA SABADO
import os 
from random import randint
vidas=3
dado1=0
dado2=0
contador=0
def numeros():

  dado1=randint(1,6)
  dado2=randint(1,6)
  return dado1,dado2

while True:
  llave=input('presione cualquier tecla para lanzar los dados')
  lanzamiento=numeros()
  print(f'dado 1 : {lanzamiento[0]}')
  print(f'dado 2 : {lanzamiento[1]}')
  print(f'tus vidas son ',vidas)
  contador=contador+1
  
  if (lanzamiento[0] + lanzamiento[1])%2==0:
   vidas+=1
   contador=contador+1
   print('tus tiros',contador)
  else:
    vidas-=1  
    contador=contador+1
    print('tus tiros',contador)
  if lanzamiento[0]==6 and lanzamiento[1]==6:
    
    print('you win')
    contador=contador+1
    os.system('pause')
    break
    print(contador)

  if vidas==0:
   print("game over")
   print('tus tiros',contador)
   break