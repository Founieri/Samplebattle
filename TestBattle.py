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
     invocationRate:float, canTriggerTwiceOneTurn:bool, numberOfPossibleMoves:int,
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


# Cast MoveClass
ActiveRedMidAttack = MoveClass("赤中攻撃", True,0,0,0,0,"none", -3, "Red", "opponent", "none",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )

PassibeRedReAttack = MoveClass("赤再攻撃", False,1,0,0,0,"self", -3, "Red", "opponent", "any",
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

# Cast CharacterClass
Ally1 = CharacterClass("Pig_A", True, 20, 1, 0, 0, 0, ActiveRedMidAttack, PassibeRedReAttack)
Enemy1 = CharacterClass("Elder_A", False, 24, 0, 0, 0, 0, ActiveRedMidAttack, PassibeRedReAttack)

character_list = [Ally1, Enemy1]

### Environment value difinition
separatorLineText = "***************** \n"
current_turn = 1


### Battle routine
while True:
    print(separatorLineText + " Turn:" + str(current_turn))
    ##[1] Display Combat infomation
    for character in character_list:
        print(character.name + " Hp:" + str(character.currentHp) + "/ " + str(character.maxHp))
    print("")

    ##[2] Move Order calculation
    #actionOrderCharacter_list = sorted(character_list, key=lambda CharacterClass: CharacterClass.speed, reverse=True)
    actionOrderCharacter_list = character_list # temp, it should be ordered by move-speed.

    ##[3] Move
    # Target
    if(character.activeSlots.toTarget == "opponent"):
        for character in actionOrderCharacter_list:
            for target_raw in character_list:
                if target_raw.isAlly != character.isAlly:
                    target = target_raw
    elif(character.activeSlots.toTarget == "self"):
        target = character

    #[3-1] buff move


    #[3-2] deal move
    # deal means, damage or heal to Target

    # target resist calculation
    targetResistValue = 0
    if (character.activeSlots.moveElement == "Red"):
        targetResistValue = target.resistRed
    if (character.activeSlots.moveElement == "Blue"):
        targetResistValue = target.resistBlue
    if (character.activeSlots.moveElement == "Yellow"):
        targetResistValue = target.resistYellow
    if (character.activeSlots.moveElement == "Green"):
        targetResistValue = target.resistGreen


    dealValue = int(character.activeSlots.moveValue - targetResistValue) #*random.uniform(0.0 + character.accuracy,1.0))
    target.currentHp += dealValue
    print(character.name + " -> " + target.name + " " + str(dealValue) + "d" )

    #[3-3] heal move

    ##[4] Chain Move evaluation
    # Priority: (1)opponent reaction -> (2)self reaction
    # Chain can trigger only once in the loop. Unlike Guild Story 2.

    #[5] Result evaluation
    if Enemy1.currentHp <= 0:
        print(separatorLineText + "You win.")
        break
    if Ally1.currentHp <= 0:
        print(separatorLineText + "You lose.")
        break
    if current_turn >= 10:
        print(separatorLineText + "Time over.")
        break

    ##[6] Clean up, reset for the next turn.
    current_turn += 1
