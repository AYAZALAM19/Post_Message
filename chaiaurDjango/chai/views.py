from django.shortcuts import render
from .models import ChaiVarity, Store
from .forms import ChaiVarityForm

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_stores_views(request):
    form = ChaiVarityForm()
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
        else:
            form = ChaiVarityForm()   
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})
