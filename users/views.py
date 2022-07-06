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

@api_view( ['GET'] )
def user(request, user_id):
	user_id = int( user_id )

	if( 0 >= user_id ):
		return JsonResponse( { 'response': 'error', 'message': 'Invalid user id.'}, status=status.HTTP_201_CREATED )

	try:
		user = Users.objects.get( Q(id=user_id) )
	except Users.DoesNotExist:
		return JsonResponse( { 'response': 'error', 'message': 'Record not found.'}, status=status.HTTP_201_CREATED )

	userDict = {
		"id": user.id,
		"name": user.title + ' ' + user.first_name + ' ' + user.last_name,
		"username": user.username,
		"phone": user.phone,
		"email": user.email,
		"city": user.city,
		"state": user.state,
		"dob": user.dob
	}	

	return JsonResponse( {"response": "success", "user": userDict }, status=status.HTTP_201_CREATED )


@api_view( ['GET','POST'] )
def users( request ):
	saved_params = {}
	params = {}

	defaults = {
		'page': 1,
		'page_size': 20,
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

	page = pageinator.page( params['page'] )

	userList = [ {
			"id": user.id,
			"name": user.title + ' ' + user.first_name + ' ' + user.last_name,
			"username": user.username,
			"phone": user.phone,
			"email": user.email,
			} for user in page.object_list ]

	return JsonResponse( {
		"response": "success", 
		"users": json.dumps( userList ), 
		"pagination": {  
			'next_page_number': page.next_page_number() if True == page.has_next() else '',
			'previous_page_number': page.previous_page_number() if True == page.has_previous() else ''
		} 
	}, status=status.HTTP_201_CREATED )

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