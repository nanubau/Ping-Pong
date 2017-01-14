from random import randint
import json
import random
from player.entity.player import Player
import os
class Refree(object):
	game_round = 0 # quater finals semifinals and finals
	data = [] # data to be returned
	Champion = None
	@staticmethod
	def initialize():
		Refree.Champion = None
		Refree.data = []
		Refree.game_round = 0
		
	def match(self,player_list):
		if len(player_list) > 1:
			players_info = player_list
			random_oponents = []
			Champion = ''
			# creating random oponents
			
			while len(players_info) !=0:
				player1 = random.choice(players_info)
				player1.score=0
				players_info.remove(player1)
				player2 = random.choice(players_info)
				player2.score=0
				players_info.remove(player2)
				
				player1.set_game_id(player1.name + '  vs  '+player2.name)		
				player2.set_game_id(player1.name + '  vs  '+player2.name)	
				
				print player1.name + '	vs	'+player2.name	
				
				random_oponents.append([player1,player2])	
			
			another_round = []
			# actual game begins
			while len(random_oponents) != 0:
				try:
					Refree().game(random_oponents[0])
				except:
					Refree.data = ["error"]
					return Refree.data
				if Refree.game_round == 0:
					print "gameround 	",Refree.game_round
				elif Refree.game_round == 1:
					print "gameround 	",Refree.game_round
				elif Refree.game_round == 2:
					print "gameround 	",Refree.game_round
				if random_oponents[0][0].status == 'WINNER':
					another_round.append(random_oponents[0][0])
					
					Refree.data.append({"game_id":random_oponents[0][1].game_id,"WINNER" : random_oponents[0][0].name,"WINNER_SCORE" : random_oponents[0][0].score, "LOSER" : random_oponents[0][1].name ,"LOSER_SCORE" : random_oponents[0][1].score ,"game_round":Refree.game_round})
					
				
				elif random_oponents[0][1].status == 'WINNER':
					another_round.append(random_oponents[0][1])
					Refree.data.append({"game_id":random_oponents[0][1].game_id,"WINNER" : random_oponents[0][1].name,"WINNER_SCORE" : random_oponents[0][1].score, "LOSER" : random_oponents[0][0].name ,"LOSER_SCORE" : random_oponents[0][0].score,"game_round":Refree.game_round})
					
				random_oponents.remove(random_oponents[0])
				
			
			Refree.game_round += 1
			Refree().match(another_round)

		else:
			print 'final WINNER 	',player_list[0].name
			Refree.Champion = player_list[0].name
			
			return Refree.Champion

	def game(self,opponents):
		player1 = opponents[0]
		player2 = opponents[1]
		
		attacker_value = player1.attack()
		[defense_list,flag] = player2.defense()
		if flag == 0:
			raise "error" 	
		if player1.score < 5 and player2.score < 5:
			if attacker_value in defense_list:
				player2.set_score()
				Refree().game([player2,player1])					
			
			else :
				player1.set_score()
				Refree().game([player1,player2])	
		else :
			if player1.score == 5: 
				player1.status = 'WINNER'
				player2.status = 'LOSER'
			elif player2.score == 5 :
				player1.status = 'LOSER'
				player2.status = 'WINNER'
			return player1,player2

	@staticmethod
	def logging():
		champion = Refree.Champion
		record = Refree.data
		firt_round = []
		second_round = []
		third_round = []
		status = False
		print Refree.data
		for i in Refree.data:
			if i["game_round"] == 0:
				firt_round.append(i)
			elif i["game_round"] == 1:
				second_round.append(i)			
			elif i["game_round"] == 2:
				third_round.append(i)
			status = True							
		data = {'first_round':firt_round,'second_round':second_round,'third_round':third_round,'champion':champion,'status':status}
		return data
	
