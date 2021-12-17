import random
import parametres as params

def create_player():
    PLAYER = []
    player_username = ""
    how_many_player = int(input("combien de joueur êtes vous ?"))
    print(how_many_player)
    for index in range(how_many_player):
        player_username = str(input("votre nom"))
        PLAYER.append({
            'username': player_username,
            'score': 0,
            'id': index,
        })
    return PLAYER


def roll_dice_set(how_many_dice):

    dice_value_list = [0] * params.NB_DICE_SIDE
    for n in range(how_many_dice):
        dice_value = random.randint(1, params.NB_DICE_SIDE)
        dice_value_list[dice_value - 1] += 1
        print(dice_value)

    return dice_value_list

def analyse_bonus_score(dice_value_list, player):
   print(dice_value_list)

   bonus_score = 0
   for index, dice_value in enumerate(dice_value_list):
       nb_of_bonus = dice_value // params.TRIGGER_OCCURRENCE_FOR_BONUS
       if nb_of_bonus > 0:
           if index == 0:
               bonus_mulitplier = params.BONUS_VALUE_FOR_ACE_BONUS
           else:
               bonus_mulitplier = params.BONUS_VALUE_FOR_NORMAL_BONUS

           bonus_score += nb_of_bonus * bonus_mulitplier * (index + 1)
           dice_value_list[index] %= params.TRIGGER_OCCURRENCE_FOR_BONUS

   print(bonus_score)
   player["score"] += bonus_score

   return dice_value_list


def analyse_standard_score(dice_value_list, player):
    standard_score = 0
    for scoring_value, scoring_multiplier in zip(params.LIST_SCORING_DICE_VALUE, params.LIST_SCORING_MULTIPLIER):
        standard_score += dice_value_list[scoring_value - 1] * scoring_multiplier
        dice_value_list[scoring_value - 1] = 0

    print(standard_score)
    player["score"] += standard_score
    return dice_value_list





def analyse_score(dice_value_list, old_score, player):
    old_score
    turn_is_scored = True
    total_dice_remain_calcul = 0
    params.THROW_DICE_COUNTER = 0

    if old_score == player["score"]:
        turn_is_scored = False

    for n in dice_value_list:
        if n != 0 and turn_is_scored == True:
            params.THROW_DICE_COUNTER += n
        total_dice_remain_calcul += n

    if total_dice_remain_calcul == 0 and turn_is_scored == True:
        params.THROW_DICE_COUNTER += 6
    elif turn_is_scored == False:
        params.STACK_BONUS = 0
        print("perdu sale chien")


    print("il te reste " + str(params.THROW_DICE_COUNTER) + " dés a lancer")
    if params.THROW_DICE_COUNTER > 0:
        test = input("voulez vous relancez ?")
        if test == "y":
            pass
        else:
            print("votre score pour ce tour est de " + str(params.STACK_BONUS))



def game():
    players = create_player()
    for player in players:
        old_score = player["score"]
        dice_value_list = roll_dice_set(params.THROW_DICE_COUNTER)
        dice_value_list = analyse_bonus_score(dice_value_list, player)
        dice_value_list = analyse_standard_score(dice_value_list, player)
        analyse_score(dice_value_list, old_score, player)

        # analyse_bonus_score(roll_dice_set(params.THROW_DICE_COUNTER, player), player)
        #analyse_standard_score()

    print("-----------------")
    print(players)



if __name__ == "__main__":
    game()
