from django.contrib import admin
from .forms import PostsModelForm
# Register your models here.
from .models import Posts

#admin.site.register(Posts)

class PostsModelAdmin(admin.ModelAdmin):
	# form = PostsModelForm
	class Meta:
		model = Posts
		


admin.site.register(Posts, PostsModelAdmin)		