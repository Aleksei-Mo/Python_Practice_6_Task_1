# Игра крестики-нолики
import datetime

stepsCounter=0
winFlag=False
turnFlag=False
userData = list(range(1,10))

def TitleLog(): # записываем в файл информацию о старте новой игры
      todayDateTime=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
      title=todayDateTime + ' New game started.' +'\n'
      with open('logFile.txt', "a") as file:
            file.write(title)
      file.close

def WinnerLog(name):#записываем инфу о результате игры
      with open('logFile.txt', "a") as file:
            if name=="DRAW":
                  file.write("The result of the game is DRAW! Try a new game!"+"\n"+"\n")
            else:
                  file.write(f"{name} is the winner of the game. Congratulation!"+"\n"+"\n")
      file.close

def GetLog(data,oper):# записываем ходы игроков
      with open('logFile.txt', "a") as file:
            file.write(f"<<< Player {oper}'s turn >>>"+"\n")
            for i in range(3):
                  file.write("(" + str(data[0+i*3]) + ' ' + str(data[1+i*3]) +' ' + str(data[2+i*3]) +")"+ "\n")
                  file.write(" -----" + "\n")
      file.close

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
                  WinnerLog(winOper)
                  return True
                  break
      return False

TitleLog()
GameField(userData)
while winFlag==False:
      if stepsCounter<9:#если израсходованы все ходы, то ничья
          if turnFlag==False:
            operand='X'
            turnFlag=True
          else:
            operand='O'
            turnFlag=False
          userData=InputData(userData,operand)
          GameField(userData)
          GetLog(userData,operand)
          winFlag=GetWinner(userData)
          print()
      else:
         print("The result of the game is DRAW! Try a new game!")
         WinnerLog("DRAW")
         winFlag=True
      stepsCounter=stepsCounter+1
GameField(userData)
print("*****Game over*****")