from django import forms

from .models import Posts

class PostsModelForm(forms.ModelForm):
	# content = forms.CharField(label='',
	# 						widget=forms.Textarea(attrs={'placeholder':'Message to Post', 'class':'form-control'})

	# 						)
	class Meta:
		model = Posts
		fields = [
		"content"


		]

	# def clean_content(self, *args, **kwargs):
	# 	content = self.cleaned_data.get("content")
	# 	if content == 'abc':
	# 		raise forms.ValidationError("contenti nvalid")
	# 	return content
