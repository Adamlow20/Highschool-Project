"""
I made this game during January of 2022 to further understand I was learning from CodeAcademy.com's python course

"""

import random

boardspot = [[" - |", " - |", " -"], ["---|---|---"], [" - |", " - |", " -"], ["---|---|---"], [" - |", " - |", " -"]]
winner = "none"
user = "!"
bot = "?"
grow = 0
gcol = 0
ro =0
turn = 0
r1= 0
hcom = False

def uinput(grow, gcol):
 gr = grow
 gc = gcol
 spot = True
 while spot:
     row = True
     col = True
     while row:
        gr = int(input("Enter Which Row: "))
    
        if gr == 1 or gr == 2 or gr == 3:
           row= False 
        
        
    
     while col:
         gc = int(input("Enter Which Colum: "))
         if gc == 1 or gc == 2 or gc == 3 :
             col = False

     
     if gr== 1:
         gr = gr-1
 
     if gr ==3:
         gr = gr+1
     gc = gc - 1
     if "-" in boardspot[gr][gc]:
      boardspot[gr][gc] = boardspot[gr][gc].replace("-", user)
      spot = False
      break
 

def printBoard(boardspot):
    print (boardspot[0][0]+ boardspot[0][1]+ boardspot[0][2])
    print (boardspot[1][0])
    print (boardspot[2][0]+ boardspot[2][1]+ boardspot[2][2])
    print (boardspot[3][0])
    print (boardspot[4][0]+ boardspot[4][1]+ boardspot[4][2])
    
def across(boardspot):
    r = 0
    while r <= 4:
        if (boardspot[r][0])[1] ==(boardspot[r][1])[1] == boardspot[r][2][1] != "-":
            winner = (boardspot[r][0])[1]
            print (winner + " has won")
            return True
            
        r+=2 
    return False

def vert(boardspot):
    c = 0
    while c < 3:
        if (c==0):
            if (boardspot[0][c])[1] ==(boardspot[2][c])[1] == (boardspot[4][c])[1] != "-":
                winner = (boardspot[0][c])[1]
                print (winner + " has won")
                return True
                
        elif(c==1):
            if (boardspot[0][c])[1] ==(boardspot[2][c])[1] == (boardspot[4][c])[1] != "-":
                winner = (boardspot[0][c])[0]
                print (winner + " has won")
                return True
                
        elif(c==2):
            if (boardspot[0][c][1]) ==(boardspot[2][c][1]) == (boardspot[4][c][1]) != "-":
                winner = (boardspot[0][c])
                print (winner + " has won")
                return True
        c +=1
                
    return False

def diag(boardspot):
    if (boardspot[0][0])[1] == (boardspot[2][1])[1] == boardspot[4][2][1] != "-":
        winner = (boardspot[0][0])[1]
        print (winner + " has won")
        return True
    elif (boardspot[4][0])[1] == (boardspot[2][1])[1] == boardspot[0][2][1] != "-":
        winner = (boardspot[4][0])[1]
        print (winner + " has won")
        return True 
    return False

def WorL(boardspot):
    if diag(boardspot) == True or across(boardspot) == True or vert(boardspot) == True:
        return False

    return True

def bfull(boardspot):
   r = 0
   while r <= 4:
        if (boardspot[r][0])[1] == "-" or (boardspot[r][1])[1] == "-" or boardspot[r][2][1] == "-":
            return True
        r+=2 
   return False

#True if spot Open False if spot filled gonna need to add loop if spot full
def easy(boardspot):
 row = 0
 spot = True
 while spot == True:
    col = random.randint(0,2)
    row = random.randint(0,5)
    # if(col % 2 !=0):
    #     col -=1
    if(row %2 !=0):
         row -=1
    print("Bot attempting at Row "+str(row)+" Col: "+str(col))
    print((boardspot[row][col])[1])
    if (boardspot[row][col])[1] == "-":
        boardspot[row][col] = (boardspot[row][col]).replace("-",bot)
        spot = False
    
#users in row
def uinr(boardspot, ro):
    numin = 0
    if user in boardspot[ro][0]:
        numin += 1
    if user in boardspot[ro][1]:
        numin += 1
    if user in boardspot[ro][2]:
        numin +=1
    return numin

#users in col
def uinc(boardspot, co):
    numin = 0
    if user in boardspot[0][co]:
        numin += 1
    if user in boardspot[2][co]:
        numin += 1
    if user in boardspot[4][co]:
        numin +=1
    return numin
#users in diagonal
def uind(boardspot, d):
    numin =0
    if d ==0:
        if user in boardspot[0][0]:
            numin += 1
        if user in boardspot[2][1]:
            numin += 1
        if user in boardspot[4][2]:
            numin += 1
    if d == 1:
        if user in boardspot[4][0]:
            numin += 1
        if user in boardspot[2][1]:
            numin += 1
        if user in boardspot[0][2]:
            numin += 1
    return numin
#bot in row
def binr(boardspot, ro):
    numin = 0
    if bot in boardspot[ro][0]:
        numin += 1
    if bot in boardspot[ro][1]:
        numin += 1
    if bot in boardspot[ro][2]:
        numin +=1
    return numin
#bot in col
def binc(boardspot, co):
    numin = 0
    if bot in boardspot[0][co]:
        numin += 1
    if bot in boardspot[2][co]:
        numin += 1
    if bot in boardspot[4][co]:
        numin +=1
    return numin
#bot in diag
def bind(boardspot, d):
    numin =0
    if d ==0:
        if bot in boardspot[0][0]:
            numin += 1
        if bot in boardspot[2][1]:
            numin += 1
        if bot in boardspot[4][2]:
            numin += 1
    if d == 1:
        if bot in boardspot[4][0]:
            numin += 1
        if bot in boardspot[2][1]:
            numin += 1
        if bot in boardspot[0][2]:
            numin += 1
    return numin
#row full
def rfull(boardspot, ro):
   if boardspot[ro][0][1] == "-" or (boardspot[ro][1])[1] == "-" or boardspot[ro][1] == "-":
       return True
   else:
       return False
#col full
def cfull(boardspot, co):
    if co == 0:
        if boardspot[0][co][1] == "-" or boardspot[2][co][1] == "-" or boardspot[4][co][1] == "-":
            return True
        else:
            return False
    elif co == 1:
        if boardspot[0][co][1] == "-" or boardspot[2][co][1] == "-" or boardspot[4][co][1] == "-":
            return True
        else:
            return False
    elif co ==2:
        if boardspot[0][co][1] == "-" or boardspot[2][co][1] == "-" or boardspot[4][co][1] == "-":
            return True
        else:
            return False
#diag full
def dfull(boardspot,d):
    if d == 0:
     if boardspot[0][0][1] == "-" or boardspot [2][1][1] == "-" or boardspot[4][2][1] == "-":
         return True
     else: 
         return False
    if d == 1:
     if boardspot[4][0][1] == "-" or boardspot [2][1][1] == "-" or boardspot[0][2][1] == "-":
         return True
     else: 
         return False
#place row
def placer(boardspot, ro):
    if ro == 0:
        if "-" in (boardspot[0][0]):
           boardspot[0][0] = boardspot[0][0].replace("-", bot)
        elif "-" in (boardspot[0][1]):
           (boardspot[0][1]) = boardspot[0][1].replace("-", bot)
        elif "-" in boardspot[0][2]:
           boardspot[0][2] = boardspot[0][2].replace("-", bot)
    elif ro == 2:
        if "-" in (boardspot[2][0]):
            boardspot[2][0] = boardspot[2][0].replace("-", bot)
        elif "-" in (boardspot[2][1]):
            boardspot[2][1] = boardspot[2][1].replace("-", bot)
        elif "-" in (boardspot[2][2]):
            boardspot[2][2] == boardspot[2][2].replace("-", bot)
    elif ro == 4:
        if  "-" in (boardspot[4][0]):
           boardspot[4][0] = boardspot[4][0].replace("-", bot)
        elif "-" in (boardspot[4][1]):
           boardspot[4][1] = boardspot[4][1].replace("-", bot)
        elif "-" in (boardspot[4][2]):
           boardspot[4][2] = boardspot[4][2].replace("-", bot)

#place col
def placec(boardspot, co):
    if co == 0:
       if "-" in boardspot[0][0]:
           boardspot[0][0] = boardspot[0][0].replace("-", bot)
       elif "-" in boardspot[2][0]:
           boardspot[2][0] = boardspot[2][0].replace("-", bot)
       elif "-" in boardspot[4][0]:
           boardspot[4][0] = boardspot[4][0].replace("-", bot)
    elif co == 1:
       if "-" in boardspot[0][1]:
           boardspot[0][1] = boardspot[0][1].replace("-", bot)
       elif "-" in boardspot[2][1]:
           boardspot[2][1] = boardspot[2][1].replace("-", bot)
       elif "-" in boardspot[4][1]:
           boardspot[4][1] = boardspot[4][1].replace("-", bot)
    elif co == 2:
       if "-" in boardspot[0][2]:
           boardspot[0][2] = boardspot[0][2].replace("-", bot)
       elif "-" in boardspot[2][2]:
           boardspot[2][2] = boardspot[2][2].replace("-", bot)
       elif "-" in boardspot[4][2]:
           boardspot[4][2] = boardspot[4][2].replace("-", bot)
#place diag
def placed(boardspot, d):
    if d == 0:
        if "-" in boardspot[0][0]:
            boardspot[0][0] = boardspot[0][0].replace("-", bot)
        elif "-" in boardspot[2][1]:
            boardspot[2][1] = boardspot[2][1].replace("-", bot)
        elif "-" in boardspot[4][2]:
            boardspot[4][2] = boardspot[4][2].replace("-", bot)

    elif d == 1:
        if "-" in boardspot[4][0]:
            boardspot[4][0] = boardspot[4][0].replace("-", bot)
        elif "-" in boardspot[2][1]:
            boardspot[2][1] = boardspot[2][1].replace("-", bot)
        elif "-" in boardspot[4][2]:
            boardspot[0][2] = boardspot[0][2].replace("-", bot)


#plays defense  
def medium(boardspot):
    hardd(boardspot)

#hard defense, makes move to defend if player has chance to win
def hardd(boardspot):
    r1 = uinr(boardspot, 0)
    r2 = uinr(boardspot, 2)
    r3 = uinr(boardspot, 4)
    c1 = uinc(boardspot, 0)
    c2 = uinc(boardspot, 1)
    c3 = uinc(boardspot, 2)
    d1 =uind(boardspot, 0)
    d2 =uind(boardspot, 1)
   
    if r1 ==2 and rfull(boardspot,0):
        placer(boardspot, 0)
        return True
    elif r2==2 and rfull(boardspot,2):
        placer(boardspot, 2)
        return True
    elif r3==2 and rfull(boardspot,4):
        placer(boardspot, 4)
        return True
    elif c1==2 and cfull(boardspot, 0):
        placec(boardspot, 0)
        return True
    elif c2==2 and cfull(boardspot, 1):
        placec(boardspot, 1)
        return True
    elif c3==2 and cfull(boardspot, 2):
        placec(boardspot, 2)
        return True
    elif d1==2 and dfull(boardspot, 0):
        placed(boardspot, 0)
        return True
    elif d2==2 and dfull(boardspot, 1):
        placed(boardspot, 1)
        return True
    else:
        easy(boardspot)
    
def hwin(boardspot):
    r1 = binr(boardspot, 0)
    r2 = binr(boardspot, 2)
    r3 = binr(boardspot, 4)
    c1 = binc(boardspot, 0)
    c2 = binc(boardspot, 1)
    c3 = binc(boardspot, 2)
    d1 =bind(boardspot, 0)
    d2 =bind(boardspot, 1)
    if r1 ==2 and rfull(boardspot,0):
        placer(boardspot, 0)
    elif r2==2 and rfull(boardspot,2):
        placer(boardspot, 2)
    elif r3==2 and rfull(boardspot,4):
        placer(boardspot, 4)
    elif c1==2 and cfull(boardspot, 0):
        placec(boardspot, 0)
    elif c2==2 and cfull(boardspot, 1):
        placec(boardspot, 1)
    elif c3==2 and cfull(boardspot, 2):
        placec(boardspot, 2)
    elif d1==2 and dfull(boardspot, 0):
        placed(boardspot, 0)
    elif d2==2 and dfull(boardspot, 1):
        placed(boardspot, 1)
    else:
        hardd(boardspot)

def ucorner(boardspot):
    tl = False
    tr = False
    bl = False
    br = False
    if user in boardspot[0][0]:
        # print(boardspot[0][0])
        # print(user)
        tl = True
    elif user in boardspot[0][2]:
        tr = True
    elif user in boardspot[4][0]:
        bl = True
    elif user in boardspot[4][2]:
        br = True
    if (tr or tl or bl or br )and ( "-" in boardspot[2][1]):
        boardspot[2][1] = boardspot[2][1].replace("-", bot)
    else:
        hwin(boardspot)
    
def hard(boardspot, t):
    if t == 1:
        ucorner(boardspot)
    else:
        hwin(boardspot)
    


#player first game against easy bot
def pfirst(boardspot, dif):
    printBoard(boardspot)
    if(dif ==1):
        print("You are now playing the Easy Bot")
        while (bfull(boardspot) == True):
            print()
            uinput(gcol, grow)
            printBoard(boardspot)
            if(WorL(boardspot) == False and bfull(boardspot) == True):
                break
            print()
            easy(boardspot)
            printBoard(boardspot)
            if(WorL(boardspot) == False and bfull(boardspot) == True):
                break
    if(dif ==2):
       print("You are now playing the Medium bot")
       printBoard(boardspot)
       while (bfull(boardspot) == True):
        print()
        uinput(gcol, grow)
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
        print()
        
        medium(boardspot)
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
    else: 
        print("You are now playing the Hard bot")
        printBoard(boardspot)
        t=1
        while (bfull(boardspot) == True):
            print()
            uinput(gcol, grow)
            t+=1
            printBoard(boardspot)
            if(WorL(boardspot) == False and bfull(boardspot) == True):
                break
            print()
            hard(boardspot,t)
            t+=1
            printBoard(boardspot)
            if(WorL(boardspot) == False and bfull(boardspot) == True):
                break
        
def bfirst(boardspot, dif):
    if(dif ==1):
       print("You are now playing the easy bot")
       printBoard(boardspot)
       while (bfull(boardspot) == True):
        print()
        easy(boardspot)
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
        print()
        
        uinput(gcol, grow)
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
    if(dif ==2):
       print("You are now playing the Medium bot")
       printBoard(boardspot)
       while (bfull(boardspot) == True):
        print()
        medium(boardspot)
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
        print()
        
        uinput(gcol, grow)
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
    
    else:
       print("You are now playing the Hard bot")
       printBoard(boardspot)
       t=1
       while (bfull(boardspot) == True and bfull(boardspot) == True):
        print()
        hard(boardspot, t)
        t+=1
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
        print()
        
        uinput(gcol, grow)
        t+=1
        printBoard(boardspot)
        if(WorL(boardspot) == False and bfull(boardspot) == True):
            break
    


    
def main(): 

    inp =0

    inp =input("Enter 1 to go first, 0 to go second: ")
    inp = int(inp)
    dif = int(input("Enter difficulty 1 for Easy, 2 for Medium, 3 for Hard: "))

    if inp ==1:
        pfirst(boardspot, dif)


    else:

        bfirst(boardspot, dif)
    


if __name__ == "__main__":
    main()
