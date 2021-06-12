from .Plant import Plant
from ..Position import Position
from ..Action import Action
from ..ActionEnum import ActionEnum


class Toadstool(Plant):

	def __init__(self, toadstool=None, position=None, world=None):
		super(Toadstool, self).__init__(toadstool, position, world)

	def clone(self):
		return Toadstool(self, None, None)

	def initParams(self):
		self.power = 0
		self.initiative = 0
		self.liveLength = 10
		self.powerToReproduce = 5
		self.sign = 'T'

	def consequences(self, atackingOrganism):
		result = []

		if self.power > atackingOrganism.power:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		else:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		return result
