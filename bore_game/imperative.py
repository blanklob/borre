import random
import parametres as params


def roll_dice_set(how_many_dice):
    params.THROW_DICE_COUNTER = 0
    # Nombre de faces
    dice_value_list = [0] * params.NB_DICE_SIDE

    for n in range(how_many_dice):
        dice_value = random.randint(1, params.NB_DICE_SIDE)
        dice_value_list[dice_value - 1] += 1

        # Valeur de des
        print(dice_value)

    print("----------------------------------")
    print(dice_value_list)
    print("----------------------------------")

    # return dice_value_list
    return analyse_bonus_score(dice_value_list)


def analyse_bonus_score(dice_value_list):
    bonus_score = 0

    for index, dice_value in enumerate(dice_value_list):

        nb_of_bonus = dice_value // params.TRIGGER_OCCURRENCE_FOR_BONUS  # 3

        if nb_of_bonus > 0:
            if index == 0:
                bonus_mulitplier = params.BONUS_VALUE_FOR_ACE_BONUS
            else:
                bonus_mulitplier = params.BONUS_VALUE_FOR_NORMAL_BONUS

            #  Example 3 fois 3 => bonus_score = 1 * 100 * ( 2 + 1 )
            bonus_score += nb_of_bonus * bonus_mulitplier * (index + 1)

            dice_value_list[index] %= params.TRIGGER_OCCURRENCE_FOR_BONUS

    return analyse_standard_score(dice_value_list, bonus_score)


def analyse_standard_score(dice_value_list, bonus_score):
    standard_score = 0
    for scoring_value, scoring_multiplier in zip(
        params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER
    ):
        standard_score += dice_value_list[scoring_value - 1] * scoring_multiplier
        dice_value_list[scoring_value - 1] = 0

    return analyse_score(dice_value_list, standard_score, bonus_score)


def analyse_score(dice_value_list, standard_score, bonus_score):
    party_score = standard_score + bonus_score
    params.STACK_BONUS += party_score

    calculus = 0

    for n in dice_value_list:
        if n == 0:
            continue

        if party_score > 0:
            params.THROW_DICE_COUNTER += n

        calculus += n

    if calculus == 0 and party_score > 0:
        params.THROW_DICE_COUNTER += 6
    elif party_score == 0:
        print("Perdu sale chien")

    if params.THROW_DICE_COUNTER > 0:
        test = input("Voulez-vous relancez ?")
        if test == "yes":
            roll_dice_set(params.THROW_DICE_COUNTER)
        else:
            print("Votre score pour ce tour est de " + str(params.STACK_BONUS))


roll_dice_set(params.THROW_DICE_COUNTER)
