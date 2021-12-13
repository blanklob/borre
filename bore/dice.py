import random
import constants

class Dice:
  def __init__(self) -> None:
    self.sides = constants.NB_DICE_SIDE

  def roll (self) -> int:
    """
    Perform a roll, and return the value of th roll
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

    return self.occurences


class Game:
  def __init__(self) -> None:
    self.set = Set()

  def run(self)-> None:
    """
    Runs the bore game
    """
    self.set.roll()

  def score(self) -> int:
    """
    Returns the game score
    """
    result = (
      self.set.occurences[constants.LIST_SCORING_DICE_VALUE[0]-1] * constants.LIST_SCORING_MULTIPLIER[0]
      + self.set.occurences[constants.LIST_SCORING_DICE_VALUE[0]-1] * constants.LIST_SCORING_MULTIPLIER[1]
    )
    return result
