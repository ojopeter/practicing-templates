from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'name':"peter"}
    return render(request, "product/home.html", context)

def about(request):
    lists = ["laptops", "Phones", "tablets"]
    true_length = True if len(lists)>2 else False
    return render(request, 'product/about.html', {'lists':lists, 'true_length':true_length})