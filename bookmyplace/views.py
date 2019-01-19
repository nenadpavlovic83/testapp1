from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import * #ContactForm , LoginForm # importuje custom formu iz forms.py

# View za renderovanje  stranica / sta vide korisnici :
#  centext za tagovanje na HTML page-u - {{ context }} renderuje text-kontext
#  koji je zadat za odredjenu stranicu
#  gde se taguje u HTML kao Dzinza TAG
#
#
def home_page(request):
    #print(request.session.get("first_name", "Unknown"))
    context = {"title" : "home",
                "content" : "cao svima!!!"}
    if request.user.is_authenticated():
        context['premium_content'] = "Weclome USER !!!"

    return render(request, 'home_page.html', context)
#     return HttpResponse("TEst")
#

def about_page(request):
    context = {"title" : "about" }
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None) # ubacivanje custom Forma iz forms.py i dodati u context
    context = {
                "title" : "contact",
                "content" : "Welcome to content page!",
                "form" : contact_form , #ubacivanje custom formi iz forms.py

               }
    if contact_form.is_valid():  #definisati cleaned_data u forms.py
        print(contact_form.cleaned_data)


    # sve ovo ideu ContactForm(request.POST or None)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname')) #get component from POST  (ako se koriste FORMS.PY mora da se stavi definisan iz FORMS.PY)
    #     print(request.POST.get('email')) #get component from POST
    #     print(request.POST.get('content')) #get component from POST
    return render(request, 'contact/view.html', context)


# def home_page(request):
#     return HttpResponse("TEst")


# standardni reusable login custom made by Nenad
# forma uzima POST or None, context sta da renderuej
# context=LoginForm da ocisti login posle submit
def login_page(request):
    form = LoginForm(request.POST or None )
    context = {"form" : form}
    print("user is logged in")
    #print(request.user.is_authenticated()) #samo za TS servera da moze da se verifikuje da li je autentifikovan na HTTPu
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        #if TS is needed uncomment bellow :
        print("--------TS--------")
        print(user)
        print(form.cleaned_data)
        print("--------Check if user is looged out without errors------")

        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            #context['form']=LoginForm()#da ocisti login
            return redirect("/")


        else:
            # Return an 'invalid login' error message.
            print("Error")
    # if form.is_valid():
    #     print(form.cleaned_data)
    return render(request, "auth/login.html", context)
#    return render(request, "PUTANJA/TEMPALTE.HTMML", {CONTEXT})

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None )
    context = {"form" : form}

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context )

#
