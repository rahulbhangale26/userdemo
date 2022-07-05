from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from pull_users_api.models import Users
from django.core import serializers
from datetime import datetime
from django.db.models import Q
import json
from django.core.paginator import Paginator
from collections import ChainMap  
# Create your views here.

@api_view( ['GET','POST'] )
def users( request ):
	saved_params = {}
	params = {}

	defaults = {
		'page': 1,
		'page_size': 100,
		'name': '',
		'id': '',
		'gender': ''
	}

	if request.session.has_key('params'):
		saved_params = request.session['params']
	
	if request.data:
		params = request.data
		saved_params = params
		request.session['params'] = params

	params = { **defaults, **saved_params, **params}
	
	q_objects = Q()
	if( params['id'] ):
		q_objects &= Q(id=params['id'])

	if( params['name'] ):
		q_objects &= ( Q( first_name__startswith=params['name'] ) | Q( last_name__startswith=params['name'] ) )

	if( params['gender'] ):
		q_objects &= Q( gender=getGenderId(params['gender'] ) )

	users = Users.objects.filter( q_objects )

	if( 1 > len( users ) ):
		return JsonResponse( { 'response': 'error', 'message': 'No records found.'}, status=status.HTTP_201_CREATED )		

	pageinator = Paginator( users, params['page_size'] )

	if( params['page'] not in pageinator.page_range ):
		return JsonResponse( { 'response': 'error', 'message': 'Invalid page number.'}, status=status.HTTP_201_CREATED )

	return JsonResponse( {"users": json.dumps( objectsToUserList( pageinator.page( params['page'] ).object_list ) ) }, status=status.HTTP_201_CREATED )

def objectsToUserList( users ):
	return [ {
			"id": user.id,
			"name": user.title + ' ' + user.first_name + ' ' + user.last_name,
			"gender": getGenderName( user.gender ),
			"username": user.username,
			"phone": user.phone,
			"email": user.email,
			"city": user.city,
			"state": user.state,
			"postcode": user.postcode,
			"dob": datetime.strftime( user.dob, '%Y-%m-%d' )
	} for user in users ]

def getGenderName( genderId ):
	if( 1 == genderId ):
		return 'male'
	elif( 2 == genderId ):
		return 'female' 

def getGenderId( gender ):
	if( 'male' == gender.lower() ):
		return 1
	elif( 'female' == gender.lower() ):
		return 2