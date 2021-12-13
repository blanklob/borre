import random
import constants

class Dice:
  def __init__(self) -> None:
    self.sides = constants.NB_DICE_SIDE

  def roll (self) -> int:
    """
    Perform a roll, and return the value of th roll.
    """
    result = random.randint(1, constants.DEFAULT_DICES_NB)
    return result


class Set:
  def __init__(self, number_of_dices = constants.NB_DICE_SIDE) -> None:
    self.number_of_dices = number_of_dices
    self.dices = []
    self.occurences = [0] * self.number_of_dices

    for _ in range(0, self.number_of_dices):
      self.dices.append(Dice())
      self.occurences

  def roll(self):
    """
    Perform a roll of a number of dices.
    """
    for dice in self.dices:
      if type(dice) is Dice:
        dice.roll()

class Game:
  def __init__(self) -> None:
    self.set = Set()

  def run(self)-> None:
    self.set.roll()
