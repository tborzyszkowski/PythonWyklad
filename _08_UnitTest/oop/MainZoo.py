import os
from Zoo.World import World
from Zoo.Position import Position
from Zoo.Organisms.Grass import Grass
from Zoo.Organisms.Sheep import Sheep
from Zoo.Organisms.Dandelion import Dandelion
from Zoo.Organisms.Wolf import Wolf
from Zoo.Organisms.Toadstool import Toadstool


if __name__ == '__main__':
	pyWorld = World(8, 8)

	newOrg = Grass(position=Position(xPosition=4, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=0, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Dandelion(position=Position(xPosition=0, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Wolf(position=Position(xPosition=7, yPosition=7), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Toadstool(position=Position(xPosition=4, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)

	for _ in range(0, 10):
		input('')
		os.system('cls')
		pyWorld.makeTurn()
		print(pyWorld)
