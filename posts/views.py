from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, DetailView, UpdateView, ListView, CreateView
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import PostsModelForm
from .models import Posts

# Create your views here.

class PostCreateView(FormUserNeededMixin, CreateView):
	#queryset = Posts.object.all()
	form_class = PostsModelForm
	template_name = 'posts/create_view.html'
	#success_url = '/posts/' 
	login_url = 'login'
	# def form_valid(self, form):
	# 	if self.request.user.is_authenticated:

	# 		form.instance.user = self.request.user
	# 		return super(PostCreateView, self).form_valid(form)
	# 	else:
	# 		form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in'])
	# 		return self.form_invalid(form)

class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Posts.objects.all()
	form_class = PostsModelForm
	#success_url = '/posts'
	template_name = 'posts/update_view.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
	#queryset = Posts.objects.all()
	model = Posts
	template_name = "posts/delete_confirm.html"
	success_url = reverse_lazy('posts:list')


class PostDetailView(DetailView):

	queryset = Posts.objects.all()


class PostListView(ListView):

	def get_queryset(self, *args, **kwargs):
		qs = Posts.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)


				)
		return qs


	
	def get_context_data(self, *args, **kwargs):
		context = super(PostListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = PostsModelForm()
		context['create_url'] = reverse_lazy('posts:create')
		return context

# def post_detail_view(request, id=1):
# 	obj = Posts.objects.get(id=id)
# 	print(obj)
# 	context = {
# 		"object" : obj

# 	}
# 	return render(request, 'posts/detail_view.html', context)


def post_list_view(request):
	queryset = Posts.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.content)
	context = {
		"object_list" : queryset
	}
	return render(request, 'posts/list_view.html', context)

