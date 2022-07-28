# Игра крестики-нолики
stepsCounter=0
winFlag=False
turnFlag=False
userData = list(range(1,10))

def CheckEnteredNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def GameField(data):
      for i in range(3):
            print("(",data[0+i*3] ,' ', data[1+i*3],' ',data[2+i*3] ,")")
            print(" ----------- ")

def InputData(data,oper):
      result=input(f"You want to put {oper} to position # --> ")
      if CheckEnteredNumber(result)==True:
            result=int(result)
            if result>9 or result<1:
                print("The entered symbol should be in range [1...9]. Try again!")
                InputData(data,oper)
            elif data[result-1]=='X' or data[result-1]=='O':
                print("Choose another position, this position is already occupied.")
                InputData(data,oper)
            else:
                data[result-1]=oper
                return data
      else:
            print("The entered symbol is not number. Try again!")
            InputData(data,oper)
      return data

def GetWinner(data):
      winComb = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
      for i in winComb:
            if data[i[0]]==data[i[1]]==data[i[2]]:
                  winOper=data[i[0]]
                  data[i[0]]='*'
                  data[i[1]]='*'
                  data[i[2]]='*'
                  print(f"The WINNER is {winOper} !")
                  return True
                  break
      return False

GameField(userData)
while winFlag==False:
      if stepsCounter<9:
          if turnFlag==False:
            operand='X'
            turnFlag=True
          else:
            operand='O'
            turnFlag=False
          userData=InputData(userData,operand)
          GameField(userData)
          winFlag=GetWinner(userData)
          print()
      else:
         print(f"The result of the game is DRAW! Try a new game!")
         winFlag=True
      stepsCounter=stepsCounter+1
GameField(userData)
print("*****Game over*****")