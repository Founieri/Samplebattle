import random

class MoveClass:
    # In battle info
    inBattleMovedCount = 0
    canMoveInThisTurn = True

    # Preset infomation, Move master.
    def __init__(self, name, isActiveMove:bool,
     chainElementRed:int,chainElementBlue:int,chainElementYellow:int,chainElementGreen:int,
     chainReference, moveValue:int, moveElement, toTarget, whatTrigger,
     invocationRate:float, canTriggerTwiceOneTurn:bool, numberOfPossibleMoves:int,
     buffOffenceRedStack:int, buffOffenceBlueStack:int, buffOffenceYellowStack:int, buffOffenceGreenStack:int,
     buffDefenceRedStack:int, buffDefenceBlueStack:int, buffDefenceYellowStack:int, buffDefenceGreenStack:int,
     buffAccuracyStack:int, buffEvasionStack:int, buffSpeedStack:int
     ):
        self.name = name
        self.isActiveMove = isActiveMove
        self.chainElementRed = chainElementRed
        self.chainElementBlue = chainElementBlue
        self.chainElementYellow = chainElementYellow
        self.chainElementGreen = chainElementGreen
        self.chainReference = chainReference
        self.moveValue = moveValue
        self.moveElement = moveElement
        self.toTarget = toTarget
        self.whatTrigger = whatTrigger
        self.invocationRate = invocationRate  # 0.0 ~ 1.0
        self.canTriggerTwiceOneTurn = canTriggerTwiceOneTurn  # boolean
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

ActiveRedMidAttack = MoveClass("赤中攻撃", True,0,0,0,0,"none", 3, "Red", "opponent", "none",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )

PassibeRedReAttack = MoveClass("赤再攻撃", False,1,0,0,0,"self", 3, "Red", "opponent", "any",
0.3, True, 20, 0,0,0,0,0,0,0,0,0,0,0 )


class CharacterClass:
    isAlly = False
    def __init__(self, name, isAlly:bool, hp:int,
     resistRed:int, resistBlue:int, resistYellow:int, resistGreen:int,
     activeSlots, passiveSlots):
        self.name = name
        self.isAlly = isAlly
        self.maxHp = hp
        self.currentHp = hp
        self.resistRed = resistRed
        self.resistBlue = resistBlue
        self.resistYellow = resistYellow
        self.resistGreen = resistGreen
        self.activeSlots = activeSlots
        self.passiveSlots = passiveSlots


Ally1 = CharacterClass("Pig_A", True, 20, 1, 0, 0, 0, ActiveRedMidAttack, PassibeRedReAttack)
#Enemy1 = CharacterClass("Elder_A", False, 24, 5, 7, 0.5)
Enemy1 = CharacterClass("Elder_A", False, 24, 0, 0, 0, 0, ActiveRedMidAttack, PassibeRedReAttack)
character_list = [Ally1, Enemy1]
current_turn = 1

while True:
    print("***************** \n Turn:" + str(current_turn))
    # Display Combat infomation
    for character in character_list:
        print(character.name + " Hp:" + str(character.currentHp) + "/ " + str(character.maxHp))
    print("")

    # Move
    #actionOrderCharacter_list = sorted(character_list, key=lambda CharacterClass: CharacterClass.speed, reverse=True)
    actionOrderCharacter_list = character_list # temp, it should be ordered by move-speed.
    for character in actionOrderCharacter_list:
        for target_raw in character_list:
            if target_raw.isAlly != character.isAlly:
                target = target_raw
        damage = int(character.activeSlots.moveValue - target.resistRed) #*random.uniform(0.0 + character.accuracy,1.0))
        target.currentHp -= damage
        print(character.name + " -> " + target.name + " " + str(damage) + "d" )

    # Result evaluation
    if Enemy1.currentHp <= 0:
        print("***************** \n You win.")
        break
    if Ally1.currentHp <= 0:
        print("***************** \n You lose.")
        break
    if current_turn >= 10:
        print("***************** \n Time over.")
        break
    current_turn += 1
