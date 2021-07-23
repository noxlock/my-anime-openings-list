from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# TODO: add custom form, then pass the form fields
# as props to vue

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    return render(request, 'login.html')
