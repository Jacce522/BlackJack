def draw(total):
    newNumber = random.randrange(1,11)
    if newNumber == 1 or newNumber == 11:        
        print("Ace drawn, use as a 1 or 11?")
        answer = int(input())
        newNumber = answer
    print(total, end=" +")
    print("", newNumber)
    return newNumber

def cpuDraw(total):
    newNumber = random.randrange(1,11)
    if total >= 11 and newNumber == 11:
        newNumber = 1
    print("Dealer:", total, end=" +")
    print("", newNumber)
    return newNumber


  
  #beginning of game
flag = 1;# bool flag 
playerNumber = 0
cpuNumber = 0




print("Let's play 21. I'll draw some cards")
cpuNumber = random.randrange(1,11)

if cpuNumber == 1:
    cpuNumber = 11
playerNumber = draw(playerNumber)
print("Your number is:", playerNumber)
print("Dealer number is:", cpuNumber)


while flag != 0:
    if playerNumber == 21:
        print("You win!")
        break
    elif playerNumber > 21:
        print("Sorry you busted and went over 21")
        break
    elif cpuNumber == 21:
        print("Dealer wins!")
        break
    elif cpuNumber > 21:
        print("Dealer busts!")
        break
    print("Hit or Stay?")
    answer = input()
   
  if answer == "hit":
        playerNumber += draw(playerNumber)
        print("Your new number is:", playerNumber)
        if cpuNumber <= 17:
            cpuNumber += cpuDraw(cpuNumber)
            print("Dealer's new number:", cpuNumber) 
        else:
            print("Dealer stays!")
        flag = 1
   elif answer == "stay":
        flag = 0
        while cpuNumber < 21:
            if cpuNumber <= 17:
                cpuNumber += cpuDraw(cpuNumber)
                print("Dealer's new number:", cpuNumber)
            else:
                print("Dealer stays!")
                break
            
