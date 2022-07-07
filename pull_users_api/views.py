import django
django.setup()
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from datetime import datetime
import multiprocessing
import requests
import json

# Create your views here.


@api_view(['GET', 'PUT'])
def pull_users(request, user_counts):

	batch_count = 1000
	processes = []
	response = []
	user_counts = int( user_counts )

	while( user_counts > 0 ):
		if( user_counts < 1000 ):
			batch_count = user_counts

		p = multiprocessing.Process(target=pullAndSave, args=[batch_count])
		p.start()
		processes.append( p )
		response.append( {'message': 'Added Parallel Process for user_counts: {}' .format( batch_count ) } )

		user_counts = user_counts - batch_count

	for p in processes:
		p.join()

	return JsonResponse({'response': '{}'.format( response ) }, status=status.HTTP_201_CREATED)

def pullAndSave( batch_count ):
	res = requests.get( 'https://randomuser.me/api/?results={}&nat=US' . format( batch_count ) ).json()
	saveUsers( res['results'] )
	

def saveUsers( res ):
	users = []
	for user in res:
		users.append( {
			'first_name': user['name']['first'],
			'last_name': user['name']['last'],
			'title': user['name']['title'],
			'gender': getGenderId( user['gender'] ),
			'email': user['email'],
			'username': user['login']['username'],
			'city': user['location']['city'],
			'state': user['location']['state'],
			'postcode': user['location']['postcode'],
			'phone': user['phone'],
			'dob': datetime.strftime( datetime.strptime(user['dob']['date'], '%Y-%m-%dT%H:%M:%S.%fZ'), '%Y-%m-%d' )
		} )
	serializer = UserSerializer( data=users, many=True )

	if serializer.is_valid():
		serializer.save()
		return {"status": "success", "data": serializer.data}
	else:
		return {"status": "error", "data": serializer.errors}

def getGenderId( gender ):
	if( 'male' == gender.lower() ):
		return 1
	elif( 'female' == gender.lower() ):
		return 2
