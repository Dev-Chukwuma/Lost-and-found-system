from django.shortcuts import render, redirect
from .forms import LostItemForm, FoundItemForm
from .models import LostItem, FoundItem
# Create your views here.
def home(request):
    return render(request, 'home.html')

def sucess(request):
    return render(request, 'sucess.html')

def sucess2(request):
    return render(request, 'sucess2.html')

def report_lost(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucess')
    else:
        form = LostItemForm()

    return render(request, 'report_lost.html', {'form': form})


def report_found(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucess2')
    else:
        form = FoundItemForm()

    return render(request, 'report_found.html', {'form': form})

def lost_items(request):
    items = LostItem.objects.all()
    return render(request, 'lost_items.html', {'items': items})

def found_items(request):
    items = FoundItem.objects.all()
    return render(request, 'found_items.html', {'items': items})


def post(request, pk):
    return render(request, 'post.html', {'pk' : pk})
