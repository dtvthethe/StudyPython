class Car:
	def __init__(self, name, speed):
		self.name = name
		self.speed = speed

	def voice(self):
		return 'beep'


class Audi(Car):
	def __init__(self, name, speed):
		self.name = name
		self.speed = speed
		
	def voice(self):
		return 'keep'

au = Audi('RV*', 3000)
print(au.name)
print(au.speed)
print(au.voice())
