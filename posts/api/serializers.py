from rest_framework import serializers
from user_acc.api.serializers import UserDislpaySerializer
from posts.models import Posts

class PostModelSerializer(serializers.ModelSerializer):
	
	user = UserDislpaySerializer()

	class Meta:
		model = Posts
		fields = ['user',  'content']