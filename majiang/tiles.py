class Tile:
	_type = None
	_value = None

	def get_type(self):
		return self._type

	def get_value(self):
		return self._value

	def __init__(self,type,value):
		if value < 1:
			raise Exception

		if value > 9:
			raise Exception

		self._value = value
		self._type = type

	def can_chao(self):
		return True

class Bamboo(Tile):
	def __init__(self, value):
		super().__init__("bamboo",value)

class Circle(Tile):
	def __init__(self, value):
		super().__init__("circle",value)

class Dragon(Tile):
	def __init__(self, value):
		if value < 1:
			raise Exception

		if value > 3:
			raise Exception

		self._value = value
		self._type = "dragon"

	def can_chao(self):
		return False

class Number(Tile):
	def __init__(self, value):
		super().__init__("number",value)

class Wind(Tile):
	def __init__(self, value):
		if value < 1:
			raise Exception("value too small")

		if value > 5:
			raise Exception("value too big")

		self._value = value
		self._type = "wind"

	def can_chao(self):
		return False
