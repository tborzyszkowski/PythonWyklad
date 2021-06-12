
class Position:

	def __init__(self, position = None, xPosition = None, yPosition = None):
		self.__x = 0
		self.__y = 0

		if position is not None:
			self.__x = position.x
			self.__y = position.y
		else:
			if xPosition is not None:
				self.__x = xPosition
			if yPosition is not None:
				self.__y = yPosition

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		self.__y = value

	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)

	def __str__(self):
		return '({0}, {1})'.format(self.x, self.y)
