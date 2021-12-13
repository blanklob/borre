import random
import constants


def roll_dice_set(how_many_dice):
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
    return analyse_score(standard_score, bonus_score)

def analyse_score(standard_score, bonus_score):
    print(standard_score)
    print(bonus_score)


roll_dice_set(6)
