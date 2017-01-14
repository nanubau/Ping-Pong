from random import randint
import json
from pprint import pprint
import random
class Player(object):
	def __init__(self,player_id,name,length,game_id=None,score=0,status=None):
		self.name = name
		self.id = player_id
		self.length = length
		self.game_id = game_id
		self.score = score
	
	
	def set_game_id(self,game_id):
		if game_id != None and game_id !='':
			self.game_id = game_id
			
		else :
			raise "Undefined game_id", game_id
	
	def set_score(self):
		self.score += 1

	def attack(self):
		return (randint(1,10))	

	def defense(self):
		try:	
			if self.length > 0 :
				defense_list = []
				while len(defense_list) < self.length:
					defense_list.append(randint(1,10))
				return [defense_list,1]
			else :
			 	raise "Length is zero" 
		except:
			raise "error " 
				

