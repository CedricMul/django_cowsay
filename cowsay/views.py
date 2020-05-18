from django.shortcuts import render
from .forms import CowUserForm
from .models import CowUser

def index(request):
    if request.method == 'POST':
        form = CowUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowUser.objects.create(
                say = data['say']
            )
            recentPost = data['say']
            return render(
                request,
                'index.html',
                {'form': form, 'recentPost': recentPost}
                )
    form = CowUserForm()
    return render(request, 'index.html', {'form': form})

def historyPage(request):
    cows = CowUser.objects.all()
    return render(request, 'history.html', {'cows': cows})
