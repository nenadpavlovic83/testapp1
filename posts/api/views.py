from django.db.models import Q

from .serializers import PostModelSerializer
from rest_framework import generics
from posts.models import Posts

class PostListAPIView(generics.ListAPIView):
	serializer_class = PostModelSerializer

	def get_queryset(self, *args, **kwargs):
		qs = Posts.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)


				)
		return qs

