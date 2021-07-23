from django.shortcuts import redirect, render
import requests
import json
from requests.models import HTTPBasicAuth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    context = {}
    return render(request, 'zapp/index.html', context)

def notfound(request, exception):
    return render(request,'zapp/index.html')

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    else:

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.warning(request, 'Username or password is incorrect')
                

        context = {}
        return render(request, 'zapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    else:

        form = CreateUser()


        if request.method == "POST":
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created for ' + form.cleaned_data.get('first_name') + '! Please log in.')


                return redirect('login')

        context = {
            'form' : form
        }
        return render(request, 'zapp/signup.html', context)

def terms(request):
    context = {}
    return render(request, 'zapp/data-table.html', context)

def error(request):
    context = {}
    return render(request, 'zapp/error.html', context)

@login_required(login_url='login')
def dashboard(request):

    url = "https://lsapi.seomoz.com/v2/top_pages"
    # url = "https://lsapi.seomoz.com/v2/usage_data"

    


    domain_name = request.GET.get('url', 'sdfaslfds')

    


    try:


    

        # domains = [ 

        # "google.com"

        # ]

        sent_json = {
            "target": domain_name,
            "limit": 20,
             
        }

        access_id = "mozscape-87fe8b4e16"
        secret_key = "b228c3aada85da29df1e840fa49abe47"

        
        r = requests.post(url, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}, json=sent_json, auth=HTTPBasicAuth(access_id,secret_key))


        json_result = r.json()

        print(json_result)

        domain_authority = json_result['results'][0]['domain_authority']
        page_authority = json_result['results'][0]['page_authority']
        spam_score = json_result['results'][0]['spam_score']
        inbound_links = json_result['results'][0]['external_pages_to_root_domain'] 
        key_values = json_result['results']

        context = {
        'domain_det' : json_result,
        'da' : domain_authority,
        'pa': page_authority,
        'spam' : spam_score, 
        'inbound' : inbound_links,
        'key_values' : key_values,
        
        }


        # title = []
        # url_x = []

        # for li in key_values:
        #     title.append(li['title'])
        #     url_x.append(li['page'])
        #     # print(li['title'])

        # print(title)

        # print(key_values)

        # print(domain_authority)
        


    
    except:
        print('hello world')
        context = {}

        # domain_authority = json_result['results']
        # print(domain_authority)

        # domain_authority = json_result['results']
        # page_authority = json_result['results']
        # spam_score = json_result['results']
        # inbound_links = json_result['results']
        # key_values = json_result['results']

        # return error(request)

    
    # print(json_result['results'][0]['domain_authority'])
    # print(domain_name)

    

    # print(json_result['results'][0]['domain_authority'])

    

    
    return render(request, 'zapp/dashboard.html', context)

# def signup(request):
#     context = {}
#     return render(request, 'zapp/signup.html', context)

# def signup(request):
#     context = {}
#     return render(request, 'zapp/signup.html', context)
