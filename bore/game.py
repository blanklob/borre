import random
import constants


def roll_dice_set(how_many_dice):
    constants.THROW_DICE_COUNTER = 0
    dice_value_list = [0] * constants.NB_DICE_SIDE
    for n in range(how_many_dice):
        dice_value = random.randint(1, constants.NB_DICE_SIDE)
        dice_value_list[dice_value - 1] += 1
        print(dice_value)
    print("----")
    print(dice_value_list)
    print("----")
    return analyse_bonus_score(dice_value_list)

def analyse_bonus_score(dice_value_list):
    bonus_score = 0
    for index, dice_value in enumerate(dice_value_list):
        nb_of_bonus = dice_value // constants.TRIGGER_OCCURRENCE_FOR_BONUS
        if nb_of_bonus > 0:
            if index == 0:
                bonus_mulitplier = constants.BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_mulitplier = constants.BONUS_VALUE_FOR_NORMAL_BONUS

            bonus_score += nb_of_bonus * bonus_mulitplier * (index + 1)
            dice_value_list[index] %= constants.TRIGGER_OCCURRENCE_FOR_BONUS
    return analyse_standard_score(dice_value_list, bonus_score)

def analyse_standard_score(dice_value_list, bonus_score):
    standard_score = 0
    for scoring_value, scoring_multiplier in zip(constants.LIST_SCORING_DICE_VALUE, constants.LIST_SCORING_MULTIPLIER):
        standard_score += dice_value_list[scoring_value - 1] * scoring_multiplier
        dice_value_list[scoring_value - 1] = 0
    return analyse_score(dice_value_list, standard_score, bonus_score)

def analyse_score(dice_value_list, standard_score, bonus_score):
    constants.STACK_BONUS += (bonus_score + standard_score)
    calculus_dickus = 0
    print(constants.STACK_BONUS)
    print("----")
    print(dice_value_list)
    print("----")
    print("----------------------------------")

    for n in dice_value_list:
        if n != 0 and (bonus_score + standard_score) > 0:
            constants.THROW_DICE_COUNTER += n
        calculus_dickus += n

    if calculus_dickus == 0 and (bonus_score + standard_score) > 0:
        constants.THROW_DICE_COUNTER += 6
        print("test")
    elif bonus_score + standard_score == 0:
        print("perdu sale chien")

    if constants.THROW_DICE_COUNTER > 0:
        test = input("voulez vous rellancez ?")
        if test == "yes":
            roll_dice_set(constants.THROW_DICE_COUNTER)
        else:
            print("votre score pour ce tour est de " + str(constants.STACK_BONUS))


roll_dice_set(constants.THROW_DICE_COUNTER)
