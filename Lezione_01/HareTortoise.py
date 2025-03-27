import random
import time

positionList = ["|"]
tortStep = 0
hareStep = 0
tortStamina = 100
hareStamina = 100
harePosition:int = 1
tortPosition:int = 1
clock = 0
bang = True
rain = 1

for i in range(1, 71): 
    positionList.insert(i, "_")
def PositionCheck(positionList:list, harePosition:int, tortPosition:int):
    if harePosition == tortPosition:
        positionList[harePosition] = "OUCH!"
        print(*positionList)
        positionList[harePosition] = "_"
    else:
        positionList[harePosition] = "H"
        positionList[tortPosition] = "T"
        print(*positionList)
        positionList[harePosition] = "_"
        positionList[tortPosition] = "_"

def tortChance(tortPosition, tortStamina) -> int:
    tortStep = random.randint(1, 10)
    match tortStep:
        case 1  | 2 | 3 | 4 | 5:
            if tortStamina>=5:
                tortPosition = tortPosition + 3
                tortStamina-5
            else:
                tortStamina = tortStamina +10
        case 6 | 7:
            if tortStamina >= 10:
                tortPosition = tortPosition - 6
                tortStamina = tortStamina -10
            else:
                tortStamina = tortStamina +10
        case 8 | 9 | 10:
            if tortStamina>3:
                tortPosition = tortPosition + 1
                tortStamina = tortStamina-3
            else:
                tortStamina = tortStamina +10
    if rain % 2 == 0:
        tortPosition = tortPosition -1
    if tortStamina>100:
            tortStamina=100
    if tortPosition<1:
        tortPosition=1
    return tortPosition, tortStamina
    
def hareChance(harePosition, hareStamina) -> int:
    hareStep = random.randint(1, 10)
    match hareStep:
        case 1 | 2:
            harePosition = harePosition+0
            hareStamina = hareStamina+10
        case 3 | 4:
            if hareStamina>=15:
                harePosition = harePosition+9
                hareStamina=hareStamina-15
        case 5:
            if hareStamina>=20:
                harePosition = harePosition-12     
                hareStamina= hareStamina-20   
        case 6 | 7 | 8:
            if hareStamina>=5:
                harePosition = harePosition+1
                hareStamina=hareStamina-5
        case 9 | 10:
            if hareStamina>=8:
                harePosition = harePosition-2
                hareStamina = hareStamina-8
    if rain % 2 == 0:
        harePosition = harePosition -2
    if harePosition<1:
        harePosition = 1
    if hareStamina>100:
        hareStamina=100
    print(hareStamina)
    return harePosition, hareStamina

print("BANG !!!!! AND THEY'RE OFF !!!!!")
while tortPosition < 70 and harePosition < 70:
    clock = clock +1
    if clock%10 == 0:
        rain += 1
    time.sleep(1)
    print(f"Time:{clock}")
    PositionCheck(positionList, harePosition, tortPosition)
    harePosition, hareStamina = hareChance(harePosition, hareStamina)
    tortPosition, tortStamina = tortChance(tortPosition, hareStamina)

if harePosition >= 70 and tortPosition >= 70:
    print("It's a tie!")
elif harePosition >= 70:
    print("HARE WINS! YUCH!!!")
else:
    print("TORTOISE WINS! VAY!!!")
