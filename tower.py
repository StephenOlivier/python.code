###########################################
# Tower Array class
###########################################

class TowerArray(object):
	def __init__(self):
		self.towerList = []

###########################################
# Shot class
###########################################

class Shot(object):
    def __init__(self, tower, enemy, board, cellDim):
        self.tower = tower
        self.enemy = enemy
        self.board = board
        self.cellDim = cellDim
        self.color = "yellow"  # Color of the shot
        self.speed = tower.shotSpeed  # Speed of the shot
        self.location = self.calculateInitialLocation()
        self.center = self.calculateCenter()

    def calculateInitialLocation(self):
        # Start the shot at the tower's center
        tower_center = self.tower.center
        startx = tower_center[0]
        starty = tower_center[1]
        return [startx, starty, startx + self.cellDim / 4, starty + self.cellDim / 4]

    def calculateCenter(self):
        centerX = (self.location[2] - self.location[0]) / 2.0 + self.location[0]
        centerY = (self.location[3] - self.location[1]) / 2.0 + self.location[1]
        return [centerX, centerY]

    def moveShot(self):
        # Move the shot towards the enemy
        enemy_center = self.enemy.center
        directionX = enemy_center[0] - self.center[0]
        directionY = enemy_center[1] - self.center[1]

        # Normalize the direction vector
        distance = (directionX**2 + directionY**2) ** 0.5
        if distance > 0:
            directionX /= distance
            directionY /= distance

        # Update the location of the shot
        self.location[0] += directionX * self.speed
        self.location[1] += directionY * self.speed
        self.location[2] += directionX * self.speed
        self.location[3] += directionY * self.speed
        self.center = self.calculateCenter()

    def isOffScreen(self):
        # Check if the shot is off the screen
        return (self.location[0] < 0 or
                self.location[1] < 0 or
                self.location[2] > len(self.board[0]) * self.cellDim or  # Adjusted to get the correct width
                self.location[3] > len(self.board) * self.cellDim)  # Adjusted to get the correct height




###########################################
# Tower class
###########################################

class Tower(object):
	def __init__(self, row, col, board, cellDim):
		self.row = row
		self.col = col
		self.board = board
		self.cellDim = cellDim
		self.location = self.calculateLocation(
		self.row, self.col, cellDim)
		self.shotOnScreen = False
		self.radius = 80
		self.center = self.calculateCenter(self.location) 
		self.shots = []
		self.color = "black"
		self.shotSpeed = 15
		self.shotDamage = 0
		self.slowDown = False

	def __repr__(self):
		return "Tower(%r, %r, %r)" % (self.row, self.col, self.color)

	def calculateLocation(self, row, col, cellDim):	
		startx = col*cellDim
		starty = row*cellDim
		endx = startx + cellDim
		endy = starty + cellDim
		return [startx, starty, endx, endy]

	def calculateCenter(self, location): 
		centerX = (location[2] - location[0])/2.0 + location[0] 
		centerY = (location[3] - location[1])/2.0 + location[1]
		return [centerX, centerY]

	def fireShot(self, enemy):
		self.shotOnScreen = True
		shot = Shot(self, enemy, self.board, self.cellDim)
		self.shots.append(shot)   
			

###########################################
# Orange Tower class
###########################################

class OrangeTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(OrangeTower, self).__init__(row, col, board, cellDim)
		self.color = "orange"
		self.cost = 3
		self.shotDamage = 1
	
		
###########################################
# Red Tower class
###########################################

class RedTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(RedTower, self).__init__(row, col, board, cellDim)
		self.color = "red"
		self.cost = 10
		self.shotDamage = 2


###########################################
# Green Tower class
###########################################

class GreenTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(GreenTower, self).__init__(row, col, board, cellDim)
		self.color = "green"
		self.cost = 15
		self.shotSpeed = 25
		self.radius = 90
		self.shotDamage = 3


###########################################
# Purple Tower class
###########################################

class PurpleTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(PurpleTower, self).__init__(row, col, board, cellDim)
		self.color = "#8C489F"
		self.radius = 65 
		self.slowDown = True
		self.cost = 15
		self.shotDamage = 1.5
		self.shotSpeed = 10


