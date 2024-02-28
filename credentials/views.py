from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect
from .models import Register
from . forms import TableForm,Branch

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        conformpassword = request.POST['password2']
        if password == conformpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('credentials:register')
            elif User.objects.filter(password=password).exists():
                messages.info(request,'password already exists')
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();

                print('user created')
                return redirect('credentials:login')

        else:
            messages.info(request, 'user not created')
            return redirect('credentials:register')
        return redirect('/')
    return render(request, 'regist.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print('loggined')
        if user is not None:
            auth.login(request, user)
            return redirect('credentials:inform')
        else:
            messages.info(request, "invalid login")
            print('invalid login')
            return redirect('credentials:login')
    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def inform(request):

    return render(request, 'informpage.html')


def personal_details_form(request):
    form = TableForm()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('credentials:details_form')
    return render(request, 'detailsform.html', {'form': form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branch = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'dropdown.html', {'branches': branch})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)