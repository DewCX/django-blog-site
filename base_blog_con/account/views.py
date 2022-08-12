from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for {username} Log in now !')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context={
        'form':form
    }

    return render(request, "account/register.html",context)

@login_required
def profile(request):
    return render(request, 'account/profile.html')
