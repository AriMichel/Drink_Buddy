from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password, Email=email)
            login(request, user)

            # redirect user to premium page
            return redirect('premium')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

