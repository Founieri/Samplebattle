import random
import copy


### Class difinition & cast (temp: now it is mixed)
class MoveClass:
    # In battle info
    inBattleMovedCount = 0
    canMoveInThisTurn = True

    # Preset infomation, Move master.
    def __init__(self, name, isActiveMove:bool,
     chainTriggerElementRed:int,chainTriggerElementBlue:int,chainTriggerElementYellow:int,chainTriggerElementGreen:int,
     chainReference, moveValue:int, moveElement, toTarget, whatTrigger,
     invocationRate:float, canTriggerMultipleInOneTurn:bool, numberOfPossibleMoves:int,
     buffOffenceRedStack:int, buffOffenceBlueStack:int, buffOffenceYellowStack:int, buffOffenceGreenStack:int,
     buffDefenceRedStack:int, buffDefenceBlueStack:int, buffDefenceYellowStack:int, buffDefenceGreenStack:int,
     buffAccuracyStack:int, buffEvasionStack:int, buffSpeedStack:int
     ):
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


# Cast MoveClass
Pig_ActiveMove1 = MoveClass("攻撃中", True,0,0,0,0,"None", -3, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Pig_ActiveMove2 = MoveClass("回復", True,0,0,0,0,"None", +3, "緑", "Self", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Pig_ActiveMove3 = MoveClass("攻撃大", True,0,0,0,0,"None", -5, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Pig_PassiveRedCounterAttack = MoveClass("反撃", False,1,0,0,0,"Opponent", -5, "赤", "Opponent", "Any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Pig_PassiveRedReAttack = MoveClass("再攻撃", False,1,0,0,0,"Self", -2, "赤", "Opponent", "Any",
0.3, True, 20, 0,0,0,0,0,0,0,0,0,0,0 )

Elder_ActiveMove1 = MoveClass("攻撃中", True,0,0,0,0,"None", -3, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_ActiveMove2 = MoveClass("防御", True,0,0,0,0,"none", 0, "黄", "Self", "None",
1.0, False, 20, 0,0,0,0,3,0,0,0,0,0,0 )
Elder_ActiveMove3 = MoveClass("攻撃大", True,0,0,0,0,"none", -5, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_PassiveRedCounterAttack = MoveClass("反撃", False,1,0,0,0,"Opponent", -5, "赤", "Opponent", "Any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_PassiveRedReAttack = MoveClass("再攻撃", False,1,0,0,0,"Self", -2, "赤", "Opponent", "Any",
0.3, True, 20, 0,0,0,0,0,0,0,0,0,0,0 )

class CharacterClass:
    isAlly = False
    chainCount = 0

    resistRedStack = 0


    def __init__(self, name, isAlly:bool, hp:int,
     resistRed:int, resistBlue:int, resistYellow:int, resistGreen:int,
     activeMove1,activeMove2,activeMove3, passiveReAttack, passiveCounterAttack):
        self.name = name
        self.isAlly = isAlly
        self.maxHp = hp
        self.currentHp = hp
        self.resistRed = resistRed
        self.resistBlue = resistBlue
        self.resistYellow = resistYellow
        self.resistGreen = resistGreen
        self.activeMove1 = activeMove1 # Temp
        self.activeMove2 = activeMove2 # Temp
        self.activeMove3 = activeMove3 # Temp
        self.passiveReAttack = passiveReAttack # Temp; it should be arry.
        self.passiveCounterAttack = passiveCounterAttack # Temp; it should be arry.
        #self.currentMove = activeSlots # temp; it is ugly.

# Cast CharacterClass
Ally1 = CharacterClass("ピグ", True, 20, 1, 0, 0, 0, Pig_ActiveMove1,Pig_ActiveMove2,Pig_ActiveMove3,
 Pig_PassiveRedReAttack, Pig_PassiveRedCounterAttack)
Enemy1 = CharacterClass("エルダー", False, 30, 0, 0, 0, 0, Elder_ActiveMove1, Elder_ActiveMove2, Elder_ActiveMove3,
 Elder_PassiveRedReAttack, Elder_PassiveRedCounterAttack)

class MoveOrderClass:
    def __init__(self, actor, currentMove, chainCount:int, isInitialMove:bool):
        self.actor = actor
        self.currentMove = currentMove
        self.chainCount = chainCount
        self.isInitialMove = isInitialMove

class TurnChainCountClass:
    chainRedStack = 0
    chainBlueStack = 0
    chainYellowStack = 0
    chainGreenStack = 0


character_list = [Ally1, Enemy1]

### Environment value difinition
separatorLineText = "***************** \n"

### Battle routine
battleCount = 0
winCount = 0
drawCount = 0

while (battleCount < 1):
    # setup, clean
    current_turn = 1
    for character in character_list:
        character.currentHp = character.maxHp
        character.resistRedStack = 0


    while True:
        print(separatorLineText + "■ターン: " + str(current_turn))
        ##[1] Display Combat infomation
        for character in character_list:
            print(character.name + " Hp: " + str(character.currentHp) + "/ " + str(character.maxHp))
        print("")

        ## Clear up chain element in Turn phase
        for character in character_list:
            character.passiveCounterAttack.canMoveInThisTurn = True
            character.passiveReAttack.canMoveInThisTurn = True

        ##[2] Move Order calculation
        #actionOrderCharacter_list = sorted(character_list, key=lambda CharacterClass: CharacterClass.speed, reverse=True)
        actionOrderList = []

        # temp move1
        for character in character_list:
            action = MoveOrderClass(character, character.activeMove1, 0, True)
            actionOrderList.append(action)

        # temp move2
        for character in character_list:
            action = MoveOrderClass(character, character.activeMove2, 0, True)
            actionOrderList.append(action)

        # temp move3
        for character in character_list:
            action = MoveOrderClass(character, character.activeMove3, 0, True)
            actionOrderList.append(action)

        ##[3]Move per character
        #for character in actionOrderCharacter_list:
        turnChainCount = TurnChainCountClass()

        while len(actionOrderList) > 0:
            actorOrder = actionOrderList.pop(0)
            for c in character_list:
                if(c.name == actorOrder.actor.name):
                    actorCharacter = c
            # Target
            if(actorOrder.currentMove.toTarget == "Opponent"):
                for target_raw in character_list:
                    if target_raw.isAlly != actorCharacter.isAlly:
                        target = target_raw
            elif(actorOrder.currentMove.toTarget == "Self"):
                target = actorCharacter

            # Clear up statistic infomation
            if(actorOrder.isInitialMove == True):
                turnChainCount.chainRedStack = 0
                turnChainCount.chainBlueStack = 0
                turnChainCount.chainYellowStack = 0
                turnChainCount.chainGreenStack = 0

            #[3-1] buff move
            buffText = ""
            if (actorOrder.currentMove.buffDefenceRedStack != 0):
                if(actorOrder.currentMove.toTarget == "Opponent"):
                    target.resistRedStack += actorOrder.currentMove.buffDefenceRedStack
                    buffText = "耐久弱化: " +  str(actorOrder.currentMove.buffDefenceRedStack)
                elif(actorOrder.currentMove.toTarget == "Self"):
                    actorCharacter.resistRedStack += actorOrder.currentMove.buffDefenceRedStack
                    buffText = "耐久強化: +" + str(actorOrder.currentMove.buffDefenceRedStack)

            #[3-2] deal move
            # deal means, damage or heal to Target



            # Offence
            if (actorOrder.currentMove.moveValue < 0):
                # target resist calculation
                targetResistValue = 0
                targetResistStack = 0
                if (actorOrder.currentMove.moveElement == "赤"):
                    targetResistValue = target.resistRed + target.resistRedStack
                    targetResistStack = target.resistRedStack
                    if(target.resistRedStack > 0):
                        target.resistRedStack -= 1
                    elif(target.resistRedStack < 0):
                        target.resistRedStack += 1
                if (actorOrder.currentMove.moveElement == "青"):
                    targetResistValue = target.resistBlue
                if (actorOrder.currentMove.moveElement == "黄"):
                    targetResistValue = target.resistYellow
                if (actorOrder.currentMove.moveElement == "緑"):
                    targetResistValue = target.resistGreen

                # calculate dealValue
                if(actorOrder.currentMove.moveValue + targetResistValue > 0):
                    dealValue = 0
                else:
                    dealValue = int(actorOrder.currentMove.moveValue + targetResistValue)

            # not offence move, not consider resist value.
            elif(actorOrder.currentMove.moveValue >= 0):
                dealValue = int(actorOrder.currentMove.moveValue)


            target.currentHp += dealValue
            battleText = ""
            if (actorOrder.currentMove.moveValue != 0):
                if(dealValue < 0):
                    battleText += str(dealValue) + " ダメージ "
                elif(dealValue > 0):
                    battleText += str(dealValue) + " 回復 "
                else:
                    battleText += " 防がれた！ "
                if(targetResistStack != 0):
                    battleText += "耐久値(" + str(targetResistStack) + ") "

            elementText = "[" + actorOrder.currentMove.moveElement + "]"

            # for # DEBUG:
            #debugText = " (" + str(turnChainCount.chainRedStack) + "/" + str(turnChainCount.chainBlueStack)+ "/" + str(turnChainCount.chainYellowStack)+ "/" + str(turnChainCount.chainGreenStack) + ")"

            print("  "*actorOrder.chainCount + elementText + " -"+actorOrder.currentMove.name + "- " + actorOrder.actor.name
            + " -> " + target.name + "  " + battleText + buffText  )

            #[XX] Result evaluation
            if target.currentHp <= 0:
                print("  "*actorOrder.chainCount + target.name + " 撃破")
                break

            # add statistic infomation
            if(actorOrder.currentMove.moveElement == "赤"):
                turnChainCount.chainRedStack += 1
            if(actorOrder.currentMove.moveElement == "青"):
                turnChainCount.chainBlueStack += 1
            if(actorOrder.currentMove.moveElement == "黄"):
                turnChainCount.chainYellowStack += 1
            if(actorOrder.currentMove.moveElement == "緑"):
                turnChainCount.chainGreenStack += 1

            #[3-1] Chain Move evaluation
            while True:
                # Priority: (1)Opponent reaction -> (2)Self reaction
                # (1) Opponent reaction
                # chainReference = Opponent should work
                if(target.passiveCounterAttack.canMoveInThisTurn and target.passiveCounterAttack.isActiveMove == False
                and target.passiveCounterAttack.chainReference == "Opponent"
                and target.passiveCounterAttack.chainTriggerElementRed <= turnChainCount.chainRedStack
                and target.passiveCounterAttack.chainTriggerElementBlue <= turnChainCount.chainBlueStack
                and target.passiveCounterAttack.chainTriggerElementYellow <= turnChainCount.chainYellowStack
                and target.passiveCounterAttack.chainTriggerElementGreen <= turnChainCount.chainGreenStack
                ):
                    if(target.passiveCounterAttack.invocationRate >= random.uniform(0.0, 1.0) ):
                        if(target.passiveCounterAttack.canTriggerMultipleInOneTurn == False):
                            target.passiveCounterAttack.canMoveInThisTurn = False
                        reaction = MoveOrderClass(target, target.passiveCounterAttack, actorOrder.chainCount +1, False)
                        actionOrderList.insert(0,reaction)
                        # print("反撃　発動: " + reaction.actor.name + " chainCount:" + str(reaction.chainCount))
                        break

                # (2)Self reaction
                # chainReference = Self should work
                if(actorCharacter.passiveReAttack.canMoveInThisTurn and actorCharacter.passiveReAttack.isActiveMove == False
                and actorCharacter.passiveReAttack.chainReference == "Self"
                and target.passiveCounterAttack.chainTriggerElementRed <= turnChainCount.chainRedStack
                and target.passiveCounterAttack.chainTriggerElementBlue <= turnChainCount.chainBlueStack
                and target.passiveCounterAttack.chainTriggerElementYellow <= turnChainCount.chainYellowStack
                and target.passiveCounterAttack.chainTriggerElementGreen <= turnChainCount.chainGreenStack
                ):
                    if(target.passiveReAttack.canTriggerMultipleInOneTurn == False):
                        target.passiveReAttack.canMoveInThisTurn = False
                    if(actorCharacter.passiveReAttack.invocationRate >= random.uniform(0.0, 1.0) ):
                        reaction = MoveOrderClass(actorCharacter, actorCharacter.passiveReAttack, actorOrder.chainCount + 1, False)
                        actionOrderList.insert(0, reaction)
                        # print("再攻撃 発動" + reaction.actor.name + " chainCount:" + str(reaction.chainCount))
                        break
                # Chain can trigger only once in the loop. Unlike Guild Story 2.
                break

        #[XX] Result evaluation
        if Enemy1.currentHp <= 0:
            print(separatorLineText + "勝利")
            winCount +=1
            break
        if Ally1.currentHp <= 0:
            print(separatorLineText + "敗北")
            break
        if current_turn >= 10:
            print(separatorLineText + "時間切れ")
            break


        ##[6] Clean up, reset for the next turn.
        current_turn += 1
        # for character in character_list:
            # character.resistRedStack = 0

    battleCount += 1

print("勝率: " + str(winCount) + "/" + str(battleCount) + " 引分: " + str(drawCount))
