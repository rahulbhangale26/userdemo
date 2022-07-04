from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'PUT'])
def pull_users(request, user_counts):
	return JsonResponse({'message': 'Received user_counts: {}'.format( user_counts ) }, status=status.HTTP_201_CREATED)