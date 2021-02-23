import random


### Class difinition & cast (temp: now it is mixed)
class MoveClass:
    # In battle info
    inBattleMovedCount = 0
    canMoveInThisTurn = True

    # Preset infomation, Move master.
    def __init__(self, name, isActiveMove:bool,
     chainElementRed:int,chainElementBlue:int,chainElementYellow:int,chainElementGreen:int,
     chainReference, moveValue:int, moveElement, toTarget, whatTrigger,
     invocationRate:float, canTriggerMultipleInOneTurn:bool, numberOfPossibleMoves:int,
     buffOffenceRedStack:int, buffOffenceBlueStack:int, buffOffenceYellowStack:int, buffOffenceGreenStack:int,
     buffDefenceRedStack:int, buffDefenceBlueStack:int, buffDefenceYellowStack:int, buffDefenceGreenStack:int,
     buffAccuracyStack:int, buffEvasionStack:int, buffSpeedStack:int
     ):
        self.name = name # Name of move
        self.isActiveMove = isActiveMove    # true:"active" or false:"passive"
        self.chainElementRed = chainElementRed
        self.chainElementBlue = chainElementBlue
        self.chainElementYellow = chainElementYellow
        self.chainElementGreen = chainElementGreen
        self.chainReference = chainReference # whitch move type trigger this move in reaction
        self.moveValue = moveValue # 0: non offence nor heal move. >= +1: heal toTarget. <= -1: attack toTarget.
        self.moveElement = moveElement # Red, Blue, Yellow, Green
        self.toTarget = toTarget # "self" or "opponent"  note: now only limited 1 vs 1.
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


# Cast MoveClass
ActiveRedMidAttack = MoveClass("攻撃", True,0,0,0,0,"none", -3, "Red", "opponent", "none",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )

PassibeRedReAttack = MoveClass("反撃", False,1,0,0,0,"self", -5, "Red", "opponent", "any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )


class CharacterClass:
    isAlly = False
    chainCount = 0

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
        self.activeSlots = activeSlots # Temp; it should be arry.
        self.passiveSlots = passiveSlots # Temp; it should be arry.

        self.currentMove = activeSlots # temp; it is ugly.

# Cast CharacterClass
Ally1 = CharacterClass("ピグ", True, 20, 1, 0, 0, 0, ActiveRedMidAttack, PassibeRedReAttack)
Enemy1 = CharacterClass("エルダー", False, 24, 0, 0, 0, 0, ActiveRedMidAttack, PassibeRedReAttack)

character_list = [Ally1, Enemy1]

### Environment value difinition
separatorLineText = "***************** \n"
current_turn = 1


### Battle routine
while True:
    print(separatorLineText + "■ターン: " + str(current_turn))
    ##[1] Display Combat infomation
    for character in character_list:
        print(character.name + " Hp: " + str(character.currentHp) + "/ " + str(character.maxHp))
    print("")

    ##[2] Move Order calculation
    #actionOrderCharacter_list = sorted(character_list, key=lambda CharacterClass: CharacterClass.speed, reverse=True)
    actionOrderCharacter_list = character_list.copy() # temp, it should be ordered by move-speed.


    ##[3]Move per character
    #for character in actionOrderCharacter_list:
    while len(actionOrderCharacter_list) > 0:
        character = actionOrderCharacter_list.pop(0)
        #print("actionOrder length: " + str(len(actionOrderCharacter_list))
        #+ " character_list length: " + str(len(character_list)))
        # Target
        if(character.currentMove.toTarget == "opponent"):
            for target_raw in character_list:
                if target_raw.isAlly != character.isAlly:
                    target = target_raw
        elif(character.currentMove.toTarget == "self"):
            target = character

        #[3-1] buff move


        #[3-2] deal move
        # deal means, damage or heal to Target

        # target resist calculation
        targetResistValue = 0
        if (character.currentMove.moveElement == "Red"):
            targetResistValue = target.resistRed
        if (character.currentMove.moveElement == "Blue"):
            targetResistValue = target.resistBlue
        if (character.currentMove.moveElement == "Yellow"):
            targetResistValue = target.resistYellow
        if (character.currentMove.moveElement == "Green"):
            targetResistValue = target.resistGreen


        dealValue = int(character.currentMove.moveValue + targetResistValue) #*random.uniform(0.0 + character.accuracy,1.0))
        target.currentHp += dealValue
        print("  "*character.chainCount + "["+character.currentMove.name + "] " + character.name + " -> " + target.name + " " + str(dealValue) + "d" )

        #[XX] Result evaluation
        if target.currentHp <= 0:
            print(" "*character.chainCount + target.name + " 撃破")
            break


        #[3-1] Chain Move evaluation
        # Priority: (1)opponent reaction -> (2)self reaction
        if(target.passiveSlots.canMoveInThisTurn and target.passiveSlots.isActiveMove == False):

            if(target.passiveSlots.invocationRate >= random.uniform(0.0, 1.0) ):
                #if (target.passiveSlots.canTriggerMultipleInOneTurn == False):
                target.passiveSlots.canMoveInThisTurn == False
                target.chainCount = character.chainCount + 1
                target.currentMove = target.passiveSlots # It is ugly.
                actionOrderCharacter_list.append(target)

        # Chain can trigger only once in the loop. Unlike Guild Story 2.

        # Refresh
        character.chainCount = 0
        character.currentMove = character.activeSlots

    #[XX] Result evaluation
    if Enemy1.currentHp <= 0:
        print(separatorLineText + "勝利")
        break
    if Ally1.currentHp <= 0:
        print(separatorLineText + "敗北")
        break
    if current_turn >= 10:
        print(separatorLineText + "時間切れ")
        break


    ##[6] Clean up, reset for the next turn.
    current_turn += 1
    for character in character_list:
        character.chainCount = 0
        character.passiveSlots.canMoveInThisTurn = True  # It is ugly.
        character.currentMove = character.activeSlots

def battleStruct(actor, target):
    print("in battle Struct")
    #return (actor, target)
