from django.shortcuts import render
from .models import mth_info

def search_results(request):
    location = request.GET.get('location')
    address = request.GET.get('address')
    type = request.GET.get('type')
    size = request.GET.get('size')

    results = mth_info.objects.all()
    if location:
        results = results.filter(location__icontains=location)
    if address:
        results = results.filter(address__icontains=address)
    if type:
        results = results.filter(type__icontains=type)
    if size:
        results = results.filter(size__icontains=size)

    return render(request, 'search_results.html', {'results': results})