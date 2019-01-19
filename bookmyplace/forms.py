from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
#django forme za render
#napraviti classu forme i dodati forme potrebne za import
class ContactForm(forms.Form):
    fullname =  forms.CharField(
                widget=forms.TextInput(
                attrs={
                "class":"form-control",
                "placeholder":"Full Name Please!"
                }))
    email    =  forms.EmailField(widget=forms.EmailInput(
                attrs={
                "class":"form-control",
                "placeholder":"Email@Email.com"
                }))
    #content  = forms.CharField(widget=forms.Textarea) #ako neces widgete skinuti poziv funkcije ()
    content  =  forms.CharField(widget=forms.Textarea(
                attrs={
                "class":"form-control",
                "placeholder":"Some text"
                }))
    #definisati clean_DATA :
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email need to be @gmail.com!!!")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(label="confirm password" , widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already taken, PLease choose new username")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already taken, PLease choose new username")
        return email
    def clean_password(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Passwords must match!")

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email need to be @gmail.com!!!")
    #     return email
