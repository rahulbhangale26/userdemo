from rest_framework import serializers 
from .models import Users
 
 
class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = Users
		fields = ('id',
				  'title',
				  'first_name',
				  'last_name',
                  'gender',
                  'email',
                  'username',
                  'city',
                  'state',
                  'postcode',
                  'phone',
                  'dob')