import random
import copy

# https://gist.github.com/vratiu/9780109
class bcolors:
    header = '\033[95m'
    black = '\033[30m'
    red = '\033[31m'
    blue = '\033[34m'
    purple = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    lightred = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    gray = '\033[2m'
    underline = '\033[4m'
    reverse = '\033[7m'
    ##TEST = "\033[39m"

    bg_black='\033[40m'
    bg_darkred='\033[41m'
    bg_red='\033[101m'

    bg_green='\033[42m'
    bg_orange='\033[43m'
    bg_blue='\033[44m'
    bg_purple='\033[45m'
    bg_cyan='\033[46m'
    bg_lightgrey='\033[47m'

### Class difinition & cast (temp: now it is mixed)
class MoveClass:
    # In battle info
    inBattleMovedCount = 0
    canMoveInThisTurn = True
    # isActiveMove = False
    # moveElement = ""
    # moveValue = 0
    # Preset infomation, Move master.
    def __init__(self,isNull:bool, name = "", isActiveMove:bool = False,
     chainTriggerElementRed:int = 0,chainTriggerElementBlue:int = 0,chainTriggerElementYellow:int = 0,chainTriggerElementGreen:int = 0,
     chainReference = "None", moveValue:int = 1, moveElement = "赤", toTarget ="Opponent", whatTrigger= "any",
     invocationRate:float=0.10, canTriggerMultipleInOneTurn:bool=False, numberOfPossibleMoves:int=0,
     buffOffenceRedStack:int=0, buffOffenceBlueStack:int=0, buffOffenceYellowStack:int=0, buffOffenceGreenStack:int=0,
     buffDefenceRedStack:int=0, buffDefenceBlueStack:int=0, buffDefenceYellowStack:int=0, buffDefenceGreenStack:int=0,
     buffAccuracyStack:int=0, buffEvasionStack:int=0, buffSpeedStack:int=0
     ):
        if(isNull):
            for p in range(25):
                self.geneticMutate(False, p)
            isActiveText = ""
            if(self.isActiveMove):
                isActiveText = "通"
            else:
                if(self.chainReference == "Opponent"):
                    isActiveText = "反撃"
                elif(self.chainReference == "Self"):
                    isActiveText = "再行動"
                elif(self.chainReference == "Global"):
                    isActiveText = "無作為"
                else:
                    isActiveText = self.chainReference

            self.name = isActiveText + "[" + str(self.moveValue) + str(self.moveElement) + "]"

        else:
            self.name = name # Name of move
            self.isActiveMove = isActiveMove    # true:"active" or false:"passive"
            self.chainTriggerElementRed = chainTriggerElementRed
            self.chainTriggerElementBlue = chainTriggerElementBlue
            self.chainTriggerElementYellow = chainTriggerElementYellow
            self.chainTriggerElementGreen = chainTriggerElementGreen
            self.chainReference = chainReference # whitch move type trigger this move in reaction
            self.moveValue = moveValue # 0: non offence nor heal move. >= +1: heal toTarget. <= -1: attack toTarget.
            self.moveElement = moveElement # 赤, 青, 黄, 緑
            self.toTarget = toTarget # "Self" or "Opponent"  note: now only limited 1 vs 1.
            self.whatTrigger = whatTrigger #
            self.invocationRate = invocationRate  # 0.0 ~ 1.0
            self.canTriggerMultipleInOneTurn = canTriggerMultipleInOneTurn  # boolean
            self.numberOfPossibleMoves = numberOfPossibleMoves
            self.buffOffenceRedStack = buffOffenceRedStack
            self.buffOffenceBlueStack = buffOffenceBlueStack
            self.buffOffenceYellowStack = buffOffenceYellowStack
            self.buffOffenceGreenStack = buffOffenceGreenStack
            self.buffDefenceRedStack = buffDefenceRedStack
            self.buffDefenceBlueStack = buffDefenceBlueStack
            self.buffDefenceYellowStack = buffDefenceYellowStack
            self.buffDefenceGreenStack = buffDefenceGreenStack
            self.buffAccuracyStack = buffAccuracyStack
            self.buffEvasionStack = buffEvasionStack
            self.buffSpeedStack = buffSpeedStack



    def geneticMutate(self,isRandom:bool, explicitPosition:int = 0):
        position = explicitPosition
        if(isRandom):
            position = random.randint(1, 24)

        if (position == 1):
            try:
                if (self.isActiveMove):
                    self.isActiveMove = False
                else:
                    self.isActiveMove = True
            except AttributeError as error:
                self.isActiveMove = False
        elif (position == 2):
            try:
                r = random.randint(0,10)
                if(r >= 9):
                    self.chainTriggerElementRed += 1
                elif(r <= 2):
                    self.chainTriggerElementRed -= 1
                else:
                    self.chainTriggerElementRed += 0

            except AttributeError as error:
                self.chainTriggerElementRed = 0
        elif(position == 3):
            try:
                r = random.randint(0,10)
                if(r >= 9):
                    self.chainTriggerElementBlue += 1
                elif(r <= 2):
                    self.chainTriggerElementBlue -= 1
                else:
                    self.chainTriggerElementBlue += 0
            except AttributeError as error:
                self.chainTriggerElementBlue = 0
        elif(position == 4):
            try:
                r = random.randint(0,10)
                if(r >= 9):
                    self.chainTriggerElementYellow += 1
                elif(r <= 2):
                    self.chainTriggerElementYellow -= 1
                else:
                    self.chainTriggerElementYellow += 0

            except AttributeError as error:
                self.chainTriggerElementYellow = 0
        elif(position == 5):
            try:
                r = random.randint(0,10)
                if(r >= 9):
                    self.chainTriggerElementGreen += 1
                elif(r <= 2):
                    self.chainTriggerElementGreen -= 1
                else:
                    self.chainTriggerElementGreen += 0

            except AttributeError as error:
                self.chainTriggerElementGreen = 0

        elif(position == 6):
            r = random.randint(0,2)
            if(r == 0):
                self.chainReference = "Self"
            elif(r == 1):
                self.chainReference = "Opponent"
            elif(r == 2):
                self.chainReference = "Global"
            # elif(r == 3):
            #     self.chainReference = "Self"
        elif(position == 7):
            try:
                if(random.randint(0,1) ==1):
                    self.moveValue += 1
                else:
                    self.moveValue -= 1
            except AttributeError as error:
                self.moveValue = 0

        elif(position == 8):
            r = random.randint(0,3)
            if(r == 0):
                self.moveElement = "赤"
            elif(r == 1):
                self.moveElement = "青"
            elif(r == 2):
                self.moveElement = "黄"
            elif(r == 3):
                self.moveElement = "緑"
        elif(position == 9):
            if(random.randint(0,1) ==1):
                self.toTarget = "Self"
            else:
                self.toTarget = "Opponent"
        elif(position == 10):
            self.whatTrigger = "Any"
            # r = random.randint(0,1)
            # if(r == 0):
            #     self.whatTrigger = "None"
            # else:
            #     self.whatTrigger = "Any"
        elif(position == 11):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.invocationRate += 0.01
                else:
                    self.invocationRate -= 0.01
            except AttributeError as error:
                self.invocationRate = 0.5 #temp
        elif(position == 12):
            r = random.randint(0,1)
            if(r == 0):
                self.canTriggerMultipleInOneTurn = True
            else:
                self.canTriggerMultipleInOneTurn = False
        elif(position == 13):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.numberOfPossibleMoves += 1
                else:
                    self.numberOfPossibleMoves -= 1
            except AttributeError as error:
                self.numberOfPossibleMoves = 1
        elif(position == 14):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffOffenceRedStack += 1
                else:
                    self.buffOffenceRedStack -= 1
            except AttributeError as error:
                self.buffOffenceRedStack = 0

        elif(position == 15):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffOffenceBlueStack += 1
                else:
                    self.buffOffenceBlueStack -= 1
            except AttributeError as error:
                self.buffOffenceBlueStack = 0
        elif(position == 16):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffOffenceYellowStack += 1
                else:
                    self.buffOffenceYellowStack -= 1
            except AttributeError as error:
                self.buffOffenceYellowStack = 0
        elif(position == 17):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffOffenceGreenStack += 1
                else:
                    self.buffOffenceGreenStack -= 1
            except AttributeError as error:
                self.buffOffenceGreenStack = 0

        elif(position == 18):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffDefenceRedStack += 1
                else:
                    self.buffDefenceRedStack -= 1
            except AttributeError as error:
                self.buffDefenceRedStack = 0
        elif(position == 19):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffDefenceBlueStack += 1
                else:
                    self.buffDefenceBlueStack -= 1
            except AttributeError as error:
                self.buffDefenceBlueStack = 0
        elif(position == 20):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffDefenceYellowStack += 1
                else:
                    self.buffDefenceYellowStack -= 1
            except AttributeError as error:
                self.buffDefenceYellowStack = 0
        elif(position == 21):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffDefenceGreenStack += 1
                else:
                    self.buffDefenceGreenStack -= 1
            except AttributeError as error:
                self.buffDefenceGreenStack = 0
        elif(position == 22):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffAccuracyStack += 1
                else:
                    self.buffAccuracyStack -= 1
            except AttributeError as error:
                self.buffAccuracyStack = 1

        elif(position == 23):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffEvasionStack += 1
                else:
                    self.buffEvasionStack -= 1
            except AttributeError as error:
                self.buffEvasionStack = 0
        elif(position == 24):
            try:
                r = random.randint(0,1)
                if(r == 0):
                    self.buffSpeedStack += 1
                else:
                    self.buffSpeedStack -= 1
            except AttributeError as error:
                self.buffSpeedStack = 0

        isActiveText = ""
        try:
            if(self.isActiveMove):
                isActiveText = "通"
            else:
                isActiveText = "反"
            self.name = isActiveText + "[" + str(self.moveValue) + str(self.moveElement) + "]"
        except AttributeError as error:
            self.name = "null"


class CharacterClass:
    isAlly = False
    chainCount = 0

    resistRedStack = 0
    resistBlueStack = 0
    resistYellowStack = 0
    resistGreenStack = 0


    def __init__(self, name, isAlly:bool, hp:int,
     resistRed:int, resistBlue:int, resistYellow:int, resistGreen:int, speed:int, moves):
        self.name = name
        self.isAlly = isAlly
        self.maxHp = hp
        self.currentHp = hp
        self.resistRed = resistRed
        self.resistBlue = resistBlue
        self.resistYellow = resistYellow
        self.resistGreen = resistGreen
        # self.activeMove1 = activeMove1 # Temp
        # self.activeMove2 = activeMove2 # Temp
        # self.activeMove3 = activeMove3 # Temp
        self.moves = moves
        # self.reattacks = reattacks # Temp; it should be arry.
        # self.counters = counters # Temp; it should be arry.
        #self.currentMove = activeSlots # temp; it is ugly.
        self.speed = speed

class MoveOrderClass:
    def __init__(self, actor, currentMove, chainCount:int, isInitialMove:bool, orderSpeed:int):
        self.actor = actor
        self.currentMove = currentMove
        self.chainCount = chainCount
        self.isInitialMove = isInitialMove
        self.orderSpeed = orderSpeed

class TurnChainCountClass:
    chainRedStack = 0
    chainBlueStack = 0
    chainYellowStack = 0
    chainGreenStack = 0
