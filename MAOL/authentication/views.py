from django.shortcuts import render

from .forms import SignupForm, LoginForm


def register(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


# def login(request):
    

#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#     else:
#         form = LoginForm()

#     context = {'form': form}

#     return render(request, 'login.html', context)
