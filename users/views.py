from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method == "POST":
        # Process the user registration and then login.
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    else:
        # Display a blank registration form for user to handle their requests.
        form = UserCreationForm()
    context = {
        'title': 'Learning_Logs/New_User',
        'form': form
    }
    return render(request, 'registration/register.html', context)