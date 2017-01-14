from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from entity.refree import Refree
from player.entity.player import Player
import os
from pprint import pprint
import json
@api_view(['GET'])    
def register(request):
	# Refree().start()
	try:	
		Refree.initialize()
		players_info = []
		player_list = []
		BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		
		try:
			players_info = json.loads(open(BASE_DIR+'/static/players_info.json').read())
		except :
			print("Wrong file or file path")
			return render(request, "report.html", {'data':{'status':False}})		
		
		pprint(players_info)
		
		for i in players_info:
			if 'id' in i and 'length' in i and 'length' in i and 'length' >0 :
				player_list.append(Player(i['id'],i['name'],i['length']))
		if len(players_info)!=8:
			return render(request, "report.html", {'data':{'status':False}})		
		try:
			Refree().match(player_list)
		except Exception,e:
			print e.message
			return render(request, "report.html", {'data':{'status':False}})				
		#  looging
		data = Refree.logging()
		# print data["third_round"]
		
		

		return render(request, "report.html", {'data':data})
	except:	
		return render(request, "report.html", {'data':{'status':False}})		