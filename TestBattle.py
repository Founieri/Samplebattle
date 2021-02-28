import random
import copy
import masterClass
from operator import itemgetter, attrgetter

# Cast MoveClass
Pig_ActiveMove1 = masterClass.MoveClass(False, "攻撃中", True,0,0,0,0,"None", -3, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0)
Pig_ActiveMove2 = masterClass.MoveClass(False,"回復", True,0,0,0,0,"None", +3, "緑", "Self", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Pig_ActiveMove3 = masterClass.MoveClass(False,"攻撃大", True,0,0,0,0,"None", -5, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_RedCounter1 = masterClass.MoveClass(False,"反撃<赤>", False,1,0,0,0,"Opponent", -3, "赤", "Opponent", "Any",
# 0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_RedCounter2 = masterClass.MoveClass(False,"反撃強<赤赤>", False,2,0,0,0,"Opponent", -5, "赤", "Opponent", "Any",
# 0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_BlueCounter1 = masterClass.MoveClass(False,"防御削り<黄>", False,0,0,1,0,"Global", -1, "青", "Opponent", "Any",
# 0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
#
# Pig_Counters = [Pig_RedCounter1, Pig_RedCounter2, Pig_BlueCounter1]

# CsvMove1 = [False,'CsvMove1', False,1,0,0,0,"Self", -2, "赤", "Opponent", "Any",
# 0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 ]

# CsvMoveSets = [CsvMove1, CsvMove1]

# Pig_Reattack1 = masterClass.MoveClass(False,"武技雷迅<赤>", False,1,0,0,0,"Self", -2, "赤", "Opponent", "Any",
# 0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_Reattack2 = masterClass.MoveClass(False,"武技千烈<赤赤>", False,2,0,0,0,"Self", -2, "赤", "Opponent", "Any",
# 0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_Reattack3 = masterClass.MoveClass(False,"武技破岩<赤*3>", False,3,0,0,0,"Self", -2, "赤", "Opponent", "Any",
# 0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_Reattack4 = masterClass.MoveClass(False,"武技崩天<赤*4>", False,4,0,0,0,"Self", -2, "赤", "Opponent", "Any",
# 0.2, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_Reattack5 = masterClass.MoveClass(False,"武技天舞<赤*5>", False,5,0,0,0,"Self", -2, "赤", "Opponent", "Any",
# 0.2, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_Reattack6 = masterClass.MoveClass(False,"武技龍迅<赤*6>", False,6,0,0,0,"Self", -3, "赤", "Opponent", "Any",
# 0.2, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
# Pig_Reattack7 = masterClass.MoveClass(False,"武技虎砲<赤*7>", False,7,0,0,0,"Self", -3, "赤", "Opponent", "Any",
# 0.2, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )


# Pig_Reattacks = [Pig_Reattack1, Pig_Reattack2 ,Pig_Reattack3, Pig_Reattack4,
 # Pig_Reattack5, Pig_Reattack6, Pig_Reattack7]

Pig_Moves = []
number = 1;
for c in range(10):
    move = masterClass.MoveClass(True)
    for d in range(20):
        move.geneticMutate(True)
    # print(move.name)
    Pig_Moves.append(move)
    number += 1

Elder_ActiveMove1 = masterClass.MoveClass(False,"攻撃中", True,0,0,0,0,"None", -3, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_ActiveMove2 = masterClass.MoveClass(False,"防御", True,0,0,0,0,"none", 0, "黄", "Self", "None",
1.0, False, 20, 0,0,0,0,3,0,0,0,0,0,0 )
Elder_ActiveMove3 = masterClass.MoveClass(False,"攻撃大", True,0,0,0,0,"none", -5, "赤", "Opponent", "None",
1.0, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_RedCounter1 = masterClass.MoveClass(False,"反撃<赤>", False,1,0,0,0,"Opponent", -3, "赤", "Opponent", "Any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_GreenCounter1 = masterClass.MoveClass(False,"回復潰し<青>", False,0,0,0,1,"Global", -2, "青", "Opponent", "Any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_BlueCounter1 = masterClass.MoveClass(False,"追加介入<青黄>", False,0,1,1,0,"Opponent", -3, "青", "Opponent", "Any",
0.3, False, 20, 0,0,0,0,0,0,0,0,0,0,0 )
Elder_Reattack1 = masterClass.MoveClass(False,"再攻撃", False,1,0,0,0,"Self", -2, "赤", "Opponent", "Any",
0.3, True, 20, 0,0,0,0,0,0,0,0,0,0,0 )

Elder_Moves = [Elder_ActiveMove1, Elder_ActiveMove2, Elder_ActiveMove3,Elder_RedCounter1,
   Elder_Reattack1]

# Cast CharacterClass


### Environment value difinition
separatorLineText = masterClass.bcolors.underline +  "                 \n" + masterClass.bcolors.endc

### Battle routine
generationCount = 0
enemyHp = 10
winRateText = ""

# Save previous moves
previousMoves = Pig_Moves.copy()
previousWinRate = 0.0


while (generationCount < 30):

    for move in Pig_Moves:
        for d in range(3):
            move.geneticMutate(True)

    if (previousWinRate > 0.8):
        enemyHp += 1

    Ally1 = masterClass.CharacterClass("ピグ", True, 30, 1, 1, 1, 1, 7, Pig_Moves)
    Enemy1 = masterClass.CharacterClass("エルダー", False, enemyHp, 0, 0, 0, 0, 6, Elder_Moves)
    character_list = [Ally1, Enemy1]

    battleCount = 0
    winCount = 0
    drawCount = 0

    while (battleCount < 10):
        # setup, clean
        current_turn = 1
        for character in character_list:
            character.currentHp = character.maxHp
            character.resistRedStack = 0
            character.resistBlueStack = 0
            character.resistYellowStack = 0
            character.resistGreenStack = 0

        while True:
            print(separatorLineText + "■ターン: " + str(current_turn) + " 世代: " + str(generationCount + 1) )
            ##[1] Display Combat infomation
            for character in character_list:
                damage_color = ""
                if(character.currentHp / character.maxHp >= 0.5):
                    damage_color =""
                elif(character.currentHp / character.maxHp >= 0.2):
                    damage_color = masterClass.bcolors.yellow
                else:
                    damage_color = masterClass.bcolors.red

                bg_color = ''
                if(character.isAlly):
                    bg_color = masterClass.bcolors.bg_cyan + masterClass.bcolors.black
                else:
                    bg_color = masterClass.bcolors.bg_orange + masterClass.bcolors.black

                print(bg_color + character.name + masterClass.bcolors.endc + " Hp: " + damage_color + str(character.currentHp) + "/ " + str(character.maxHp) + masterClass.bcolors.endc)
            print("")

            ## Clear up chain element in Turn phase
            for character in character_list:
                for chain in character.moves:
                    chain.canMoveInThisTurn = True
                # for reattack in character.reattacks:
                #     reattack.canMoveInThisTurn = True

            ##[2] Move Order calculation
            #actionOrderCharacter_list = sorted(character_list, key=lambda CharacterClass: CharacterClass.speed, reverse=True)
            actionOrderList = []

            tempOrderList =[]
            for character in character_list:
                delaySpeed = 0
                for move in character.moves:
                    if (move.isActiveMove):
                        moveSpeed = character.speed - delaySpeed
                        action = masterClass.MoveOrderClass(character, move, 0, True, moveSpeed)
                        tempOrderList.append(action)
                        delaySpeed += 2
            # sorted(actionOrderList, key=lambda character: character.orderSpeed)
            actionOrderList = sorted(tempOrderList, key=attrgetter('orderSpeed'), reverse=True)


            # # temp move2
            # for character in character_list:
            #     action = masterClass.MoveOrderClass(character, character.activeMove2, 0, True)
            #     actionOrderList.append(action)
            #
            # # temp move3
            # for character in character_list:
            #     action = masterClass.MoveOrderClass(character, character.activeMove3, 0, True)
            #     actionOrderList.append(action)

            ##[3]Move per character
            #for character in actionOrderCharacter_list:
            turnChainCount = masterClass.TurnChainCountClass()

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

                # 赤
                if (actorOrder.currentMove.buffDefenceRedStack != 0):
                    if(actorOrder.currentMove.toTarget == "Opponent"):
                        target.resistRedStack += actorOrder.currentMove.buffDefenceRedStack
                        buffText += "赤耐久: " +  str(actorOrder.currentMove.buffDefenceRedStack)
                    elif(actorOrder.currentMove.toTarget == "Self"):
                        actorCharacter.resistRedStack += actorOrder.currentMove.buffDefenceRedStack
                        buffText += "赤耐久: " + str(actorOrder.currentMove.buffDefenceRedStack)

                # 青
                if (actorOrder.currentMove.buffDefenceBlueStack != 0):
                    if(actorOrder.currentMove.toTarget == "Opponent"):
                        target.resistBlueStack += actorOrder.currentMove.buffDefenceBlueStack
                        buffText += "青耐久: " +  str(actorOrder.currentMove.buffDefenceBlueStack)
                    elif(actorOrder.currentMove.toTarget == "Self"):
                        actorCharacter.resistBlueStack += actorOrder.currentMove.buffDefenceBlueStack
                        buffText += "青耐久: " + str(actorOrder.currentMove.buffDefenceBlueStack)

                # 黄
                if (actorOrder.currentMove.buffDefenceYellowStack != 0):
                    if(actorOrder.currentMove.toTarget == "Opponent"):
                        target.resistYellowStack += actorOrder.currentMove.buffDefenceYellowStack
                        buffText += "黄耐久: " +  str(actorOrder.currentMove.buffDefenceYellowStack)
                    elif(actorOrder.currentMove.toTarget == "Self"):
                        actorCharacter.resistYellowStack += actorOrder.currentMove.buffDefenceYellowStack
                        buffText += "黄耐久: " + str(actorOrder.currentMove.buffDefenceYellowStack)

                # 緑
                if (actorOrder.currentMove.buffDefenceGreenStack != 0):
                    if(actorOrder.currentMove.toTarget == "Opponent"):
                        target.resistGreenStack += actorOrder.currentMove.buffDefenceGreenStack
                        buffText += "緑耐久: " +  str(actorOrder.currentMove.buffDefenceGreenStack)
                    elif(actorOrder.currentMove.toTarget == "Self"):
                        actorCharacter.resistGreenStack += actorOrder.currentMove.buffDefenceGreenStack
                        buffText += "緑耐久: " + str(actorOrder.currentMove.buffDefenceGreenStack)



                #[3-2] deal move
                # deal means, damage or heal to Target



                # Offence
                targetResistValue = 0
                targetResistStack = 0
                if (actorOrder.currentMove.moveValue < 0):
                    # target resist calculation
                    if (actorOrder.currentMove.moveElement == "赤"):
                        targetResistValue = target.resistRed + target.resistRedStack
                        targetResistStack = target.resistRedStack
                        if(target.resistRedStack > 0):
                            target.resistRedStack -= 1
                        elif(target.resistRedStack < 0):
                            target.resistRedStack += 1
                    if (actorOrder.currentMove.moveElement == "青"):
                        targetResistValue = target.resistBlue + target.resistBlueStack
                        targetResistStack = target.resistBlueStack
                        if(target.resistBlueStack > 0):
                            target.resistBlueStack -= 1
                        elif(target.resistBlueStack < 0):
                            target.resistBlueStack += 1
                    if (actorOrder.currentMove.moveElement == "黄"):
                        targetResistValue = target.resistYellow + target.resistYellowStack
                        targetResistStack = target.resistYellowStack
                        if(target.resistYellowStack > 0):
                            target.resistYellowStack -= 1
                        elif(target.resistYellowStack < 0):
                            target.resistYellowStack += 1
                    if (actorOrder.currentMove.moveElement == "緑"):
                        targetResistValue = target.resistGreen + target.resistGreenStack
                        targetResistStack = target.resistGreenStack
                        if(target.resistGreenStack > 0):
                            target.resistGreenStack -= 1
                        elif(target.resistGreenStack < 0):
                            target.resistGreenStack += 1

                    # calculate dealValue
                    if(actorOrder.currentMove.moveValue + targetResistValue > 0):
                        dealValue = 0
                    else:
                        dealValue = int(actorOrder.currentMove.moveValue + targetResistValue)

                # not offence move, not consider resist value.
                elif(actorOrder.currentMove.moveValue >= 0):
                    dealValue = int(actorOrder.currentMove.moveValue)


                target.currentHp += dealValue

                # check over heal
                if(target.currentHp > target.maxHp):
                    target.currentHp = target.maxHp

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

                color = ""
                if(actorOrder.currentMove.moveElement == "赤"):
                    color = masterClass.bcolors.red
                elif(actorOrder.currentMove.moveElement == "青"):
                    color = masterClass.bcolors.blue
                elif(actorOrder.currentMove.moveElement == "黄"):
                    color = masterClass.bcolors.yellow
                elif(actorOrder.currentMove.moveElement == "緑"):
                    color = masterClass.bcolors.green

                elementText = "[" + color + actorOrder.currentMove.moveElement + masterClass.bcolors.endc + "]"

                # for # DEBUG:
                #debugText = " (" + str(turnChainCount.chainRedStack) + "/" + str(turnChainCount.chainBlueStack)+ "/" + str(turnChainCount.chainYellowStack)+ "/" + str(turnChainCount.chainGreenStack) + ")"

                bg_color = ''
                if(actorOrder.actor.isAlly):
                    bg_color = masterClass.bcolors.bg_cyan + masterClass.bcolors.black
                else:
                    bg_color = masterClass.bcolors.bg_orange + masterClass.bcolors.black

                print("  "*actorOrder.chainCount + elementText +" " + "-" + actorOrder.currentMove.name + "- "
                + bg_color + actorOrder.actor.name + masterClass.bcolors.endc + " -> " + target.name
                + "  " + battleText + buffText + " (速:" +str(actorOrder.orderSpeed) + ")" )

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

                if(actorOrder.chainCount <= 10):
                    while (True):
                        # Priority: (1)Opponent reaction -> (2)Global reaction -> (3)Self reaction
                        # (1) Opponent reaction
                        # chainReference = Opponent should work
                        for counter in target.moves:
                            flag = False
                            if(counter.canMoveInThisTurn and counter.isActiveMove == False
                            and counter.chainReference == "Opponent"
                            and counter.chainTriggerElementRed <= turnChainCount.chainRedStack
                            and counter.chainTriggerElementBlue <= turnChainCount.chainBlueStack
                            and counter.chainTriggerElementYellow <= turnChainCount.chainYellowStack
                            and counter.chainTriggerElementGreen <= turnChainCount.chainGreenStack
                            and counter.numberOfPossibleMoves >= counter.inBattleMovedCount
                            ):
                                if(counter.invocationRate >= random.uniform(0.0, 1.0) ):
                                    if(counter.canTriggerMultipleInOneTurn == False):
                                        counter.canMoveInThisTurn = False
                                    counter.inBattleMovedCount += 1
                                    reaction = masterClass.MoveOrderClass(target, counter, actorOrder.chainCount +1, False, actorOrder.orderSpeed)
                                    actionOrderList.insert(0,reaction)
                                    # print("反撃　発動: " + reaction.actor.name + " chainCount:" + str(reaction.chainCount))
                                    flag = True
                                    break
                        if(flag):
                            break

                        # (2) Global reaciton
                        for character in character_list:
                            flag = False
                            for counter in character.moves:
                                if(counter.canMoveInThisTurn and counter.isActiveMove == False
                                and counter.chainReference == "Global"
                                and counter.chainTriggerElementRed <= turnChainCount.chainRedStack
                                and counter.chainTriggerElementBlue <= turnChainCount.chainBlueStack
                                and counter.chainTriggerElementYellow <= turnChainCount.chainYellowStack
                                and counter.chainTriggerElementGreen <= turnChainCount.chainGreenStack
                                and counter.numberOfPossibleMoves >= counter.inBattleMovedCount
                                ):
                                    if(counter.invocationRate >= random.uniform(0.0, 1.0) ):
                                        if(counter.canTriggerMultipleInOneTurn == False):
                                            counter.canMoveInThisTurn = False
                                        counter.inBattleMovedCount += 1
                                        reaction = masterClass.MoveOrderClass(character, counter, actorOrder.chainCount +1, False, actorOrder.orderSpeed)
                                        actionOrderList.insert(0,reaction)
                                        flag = True
                                        break
                                if(flag):
                                    break
                            if(flag):
                                break

                        # (3)Self reaction
                        # chainReference = Self should work
                        for reattack in actorCharacter.moves:
                            if(reattack.canMoveInThisTurn and reattack.isActiveMove == False
                            and reattack.chainReference == "Self"
                            and reattack.chainTriggerElementRed <= turnChainCount.chainRedStack
                            and reattack.chainTriggerElementBlue <= turnChainCount.chainBlueStack
                            and reattack.chainTriggerElementYellow <= turnChainCount.chainYellowStack
                            and reattack.chainTriggerElementGreen <= turnChainCount.chainGreenStack
                            and reattack.numberOfPossibleMoves >= reattack.inBattleMovedCount
                            ):
                                if(reattack.canTriggerMultipleInOneTurn == False):
                                    reattack.canMoveInThisTurn = False
                                reattack.inBattleMovedCount += 1
                                if(reattack.invocationRate >= random.uniform(0.0, 1.0) ):
                                    reaction = masterClass.MoveOrderClass(actorCharacter, reattack, actorOrder.chainCount + 1, False, actorOrder.orderSpeed)
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
                drawCount +=1
                break


            ##[6] Clean up, reset for the next turn.
            current_turn += 1
            for character in character_list:
                for move in character.moves:
                    move.inBattleMovedCount = 0

        battleCount += 1

    currentWinRate = (winCount + (drawCount / 2) ) / battleCount

    # If winrate is below than previous one, back to previous move.
    if(currentWinRate < previousWinRate):
        Pig_Moves = previousMoves.copy()
    else:
        previousMoves = Pig_Moves.copy()
    previousWinRate = currentWinRate
    # str(winCount) + "/" + str(battleCount) + " 引分: " + str(drawCount) +

    slash = ""
    q, mod = divmod(generationCount, 10)
    if(9 == mod ):
        slash = "\n"

    winRateText += str(generationCount) + ": " +str(round(currentWinRate *100 )) + "% " + slash
    generationCount += 1
print(winRateText)
