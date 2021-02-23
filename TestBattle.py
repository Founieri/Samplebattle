import random
import copy


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
Pig_ActiveRedMidAttack = MoveClass("攻撃", True,0,0,0,0,"none", -3, "Red", "opponent", "none",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Pig_PassiveRedCounterAttack = MoveClass("反撃", False,1,0,0,0,"Opponent", -5, "Red", "opponent", "any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Pig_PassiveRedReAttack = MoveClass("再攻撃", False,1,0,0,0,"Self", -2, "Red", "opponent", "any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )

Elder_ActiveRedMidAttack = MoveClass("攻撃", True,0,0,0,0,"none", -3, "Red", "opponent", "none",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_PassiveRedCounterAttack = MoveClass("反撃", False,1,0,0,0,"Opponent", -5, "Red", "opponent", "any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_PassiveRedReAttack = MoveClass("再攻撃", False,1,0,0,0,"Self", -2, "Red", "opponent", "any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )

class CharacterClass:
    isAlly = False
    chainCount = 0

    def __init__(self, name, isAlly:bool, hp:int,
     resistRed:int, resistBlue:int, resistYellow:int, resistGreen:int,
     activeMove, passiveReAttack, passiveCounterAttack):
        self.name = name
        self.isAlly = isAlly
        self.maxHp = hp
        self.currentHp = hp
        self.resistRed = resistRed
        self.resistBlue = resistBlue
        self.resistYellow = resistYellow
        self.resistGreen = resistGreen
        self.activeMove = activeMove # Temp; it should be arry.
        self.passiveReAttack = passiveReAttack # Temp; it should be arry.
        self.passiveCounterAttack = passiveCounterAttack # Temp; it should be arry.
        #self.currentMove = activeSlots # temp; it is ugly.

# Cast CharacterClass
Ally1 = CharacterClass("ピグ", True, 20, 1, 0, 0, 0, Pig_ActiveRedMidAttack, Pig_PassiveRedReAttack, Pig_PassiveRedCounterAttack)
Enemy1 = CharacterClass("エルダー", False, 24, 0, 0, 0, 0, Elder_ActiveRedMidAttack, Elder_PassiveRedReAttack, Elder_PassiveRedCounterAttack)

class MoveOrderClass:
    def __init__(self, actor, currentMove, chainCount:int):
        self.actor = actor
        self.currentMove = currentMove
        self.chainCount = chainCount


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
    actionOrderList = []
    for character in character_list:
        action = MoveOrderClass(character, character.activeMove, 0)
        actionOrderList.append(action)

    ##[3]Move per character
    #for character in actionOrderCharacter_list:
    while len(actionOrderList) > 0:
        actorOrder = actionOrderList.pop(0)
        for c in character_list:
            if(c.name == actorOrder.actor.name):
                actorCharacter = c
        # Target
        if(actorOrder.currentMove.toTarget == "opponent"):
            for target_raw in character_list:
                if target_raw.isAlly != actorCharacter.isAlly:
                    target = target_raw
        elif(actorOrder.currentMove.toTarget == "self"):
            target = actorCharacter

        #[3-1] buff move


        #[3-2] deal move
        # deal means, damage or heal to Target

        # target resist calculation
        targetResistValue = 0
        if (actorOrder.currentMove.moveElement == "Red"):
            targetResistValue = target.resistRed
        if (actorOrder.currentMove.moveElement == "Blue"):
            targetResistValue = target.resistBlue
        if (actorOrder.currentMove.moveElement == "Yellow"):
            targetResistValue = target.resistYellow
        if (actorOrder.currentMove.moveElement == "Green"):
            targetResistValue = target.resistGreen


        dealValue = int(actorOrder.currentMove.moveValue + targetResistValue) #*random.uniform(0.0 + character.accuracy,1.0))
        target.currentHp += dealValue
        print("  "*actorOrder.chainCount + "["+actorOrder.currentMove.name + "] " + actorOrder.actor.name + " -> " + target.name + " " + str(dealValue) + "d" )

        #[XX] Result evaluation
        if target.currentHp <= 0:
            print("  "*actorOrder.chainCount + target.name + " 撃破")
            break

        #[3-1] Chain Move evaluation
        while True:
            # Priority: (1)Opponent reaction -> (2)Self reaction
            # (1) Opponent reaction
            # chainReference = Opponent should work
            if(target.passiveCounterAttack.canMoveInThisTurn and target.passiveCounterAttack.isActiveMove == False
            and target.passiveCounterAttack.chainReference == "Opponent"):

                if(target.passiveCounterAttack.invocationRate >= random.uniform(0.0, 1.0) ):
                    reaction = MoveOrderClass(target, target.passiveCounterAttack, actorOrder.chainCount +1)
                    actionOrderList.insert(0,reaction)
                    # print("反撃　発動: " + reaction.actor.name + " chainCount:" + str(reaction.chainCount))
                    break

            # (2)Self reaction
            # chainReference = Self should work
            if(actorCharacter.passiveReAttack.canMoveInThisTurn and actorCharacter.passiveReAttack.isActiveMove == False
            and actorCharacter.passiveReAttack.chainReference == "Self"):

                if(actorCharacter.passiveReAttack.invocationRate >= random.uniform(0.0, 1.0) ):
                    reaction = MoveOrderClass(actorCharacter, actorCharacter.passiveReAttack, actorOrder.chainCount + 1)
                    actionOrderList.insert(0, reaction)
                    # print("再攻撃 発動" + reaction.actor.name + " chainCount:" + str(reaction.chainCount))
                    break
            # Chain can trigger only once in the loop. Unlike Guild Story 2.
            break

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

def battleStruct(actor, target):
    print("in battle Struct")
    #return (actor, target)
