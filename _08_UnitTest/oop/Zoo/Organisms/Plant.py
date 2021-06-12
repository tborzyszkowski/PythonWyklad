from .Organism import Organism
from ..Action import Action
from ..ActionEnum import ActionEnum
import random


class Plant(Organism):

	def __init__(self, plant=None, position=None, world=None):
		super(Plant, self).__init__(plant, position, world)

	def move(self):
		result = []
		return result

	def action(self):
		result = []
		newPlant = None
		newPosition = None

		if self.ifReproduce():
			pomPositions = self.getFreeNeighboringPosition(self.position)

			if pomPositions:
				newPosition = random.choice(pomPositions)
				newPlant = self.clone()
				newPlant.initParams()
				newPlant.position = newPosition
				self.power = self.power / 2
				result.append(Action(ActionEnum.A_ADD, newPosition, 0, newPlant))
		return result

	def getFreeNeighboringPosition(self, position):
		return self.world.filterFreePositions(self.world.getNeighboringPositions(position))
