import random
import os

again = ""

class InvalidLogic(ValueError):
  def __init__(self, value):
    self.value = value
  
def msgError(msg = "Erro de valor! Digite de novo."):
    print(msg)


def numberRange():
  try:
    range1 = int(input("O número aleatório deve ir de:"))
    range2 = int(input("a:"))
    if range1 > range2:
      raise InvalidLogic("Erro de lógica, o número não pode ir de maior para menor! o padrão de 0 a 1 foi aplicado") from ValueError
    else:
      return range1, range2
  except InvalidLogic as il:
    print(il)
    return 0, 1

def randomNumber(nrange1, nrange2):
  try:
    numberRandom = random.randint(nrange1,nrange2)
    return numberRandom
  except ValueError:
    msgError("Valor impossível! Aceite sua derrota o computador ficou bravo aceitar que ele venceu é a única solução:")
    numberRandom = 666
    return numberRandom

def guessNumber():
  try:
    numberGuessed = int(input("Chute um número inteiro:")) 
    return numberGuessed
  except ValueError:
    msgError()
   
def computerGuess():
    range1, range2 = numberRange()
    while True:
      computerNumber = randomNumber(range1, range2)
      try:
        guessedRight = int(input(f"""Eu pensei em... {computerNumber}! está certo?
  Digite 0 se o número está certo.
  Digite 1 se o número certo é menor.
  Digite 2 se é maior.
  O número é:"""))
      except ValueError:
        msgError()
      if guessedRight == 0:
        print("Obrigado por jogar!")
        break
      elif guessedRight == 1:
        print("Vou tentar denovo!")
        range2 = computerNumber - 1
      else:
        print("Vou tentar denovo!")
        range1 = computerNumber  + 1
        
def rightOrNot(a, b):
    if a == b:
      print("Você acertou!")
      return True
    elif a <= b:
      print("Chute um número maior!")
    else:
      print("Chute um número menor!")

while True:
    
    try:
      opc = int(input(f"Quer jogar{again}?\n 2-A maquina advinha seu número\n 1-Advinhe o número\n 0-Sair\n escolho:"))
      again = " de novo"
      os.system("cls")
    except ValueError:
      msgError()
      continue

    match(opc):
      case 0:
        break
      case 1:
        range1, range2 = numberRange()
        toBeGuessed = randomNumber(range1, range2)
        while True:
          if rightOrNot(guessNumber(),toBeGuessed):
            break
      case 2:
        while True:
          computerGuess()
          break
      case _:
        print("Erro!")
        break