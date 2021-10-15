from django.shortcuts import redirect, render

from .forms import SignupForm


def register(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/login')

    context = {'form': form}
    return render(request, 'register.html', context)
