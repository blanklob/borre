import random
import constants

class Dice:
  def __init__(
    self,
    sides = constants.NB_DICE_SIDE
  ) -> None:
    self.sides = sides

  def roll (self) -> int:
    """
    Perform a roll, and return the value of the roll
    """
    result = random.randint(1, constants.DEFAULT_DICES_NB)
    return result


class Set:
  def __init__(
    self,
    number_of_dices = constants.NB_DICE_SIDE
  ) -> None:
    self.number_of_dices = number_of_dices
    self.dices = []
    self.occurences = [0] * self.number_of_dices

    for _ in range(self.number_of_dices):
      self.dices.append(Dice())

  def roll(self) -> list:
    """
    Perform a roll of a number of dices
    """
    for dice in self.dices:
      if type(dice) is Dice:
        result = dice.roll()
        self.occurences[result-1] += 1

    print(self.occurences)
    return self.occurences


class Game:
  def __init__(self) -> None:
    self.set = Set()
    self.score = 0

  def run(self)-> None:
    """
    Runs the bore game
    """
    self.set.roll()
    self.global_score()


  def standard_score(self) -> int:
    """
    Returns the standard game score
    """
    result = (
      self.set.occurences[constants.LIST_SCORING_DICE_VALUE[0]-1] * constants.LIST_SCORING_MULTIPLIER[0]
      + self.set.occurences[constants.LIST_SCORING_DICE_VALUE[1]-1] * constants.LIST_SCORING_MULTIPLIER[1]
    )

    return result


  def bonus_score(self) -> int:
    """
    Returns the bonus game score
    """
    score = 0
    for index, occurrence in enumerate(self.set.occurences):
      num_of_bonus = occurrence // constants.TRIGGER_OCCURRENCE_FOR_BONUS

      if num_of_bonus:
        if not index:
          bonus_multiplier = constants.BONUS_VALUE_FOR_ACE_BONUS
        else:
          bonus_multiplier = constants.BONUS_VALUE_FOR_NORMAL_BONUS

        score += num_of_bonus * bonus_multiplier * (index + 1)
        self.set.occurences[index] %= constants.TRIGGER_OCCURRENCE_FOR_BONUS

    return score


  def global_score(self) -> int:
    """
    Returns the global game score
    """
    self.score = self.standard_score() + self.bonus_score()

    return self.score
