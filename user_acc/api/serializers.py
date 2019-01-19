from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

	
class UserDislpaySerializer(serializers.ModelSerializer):
	follower_count = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = [
		'username',
		'first_name',
		'last_name',
		'follower_count'

		]

	def get_follwer_count(self, obj):
		
		return 0
