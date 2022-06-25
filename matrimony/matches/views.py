from django.shortcuts import render
from .forms import BiodataForm
from .models import BiodataModel

# Create your views here.
def home(request):
    context = {}
    context['form'] = BiodataForm()
    list = BiodataModel.objects.all()
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return render(request,'example.html', {"list":list})
    return render(request,'biodata.html',context)
def contact(request):
    return render(request,'contact.html')
def details(request):
    return render(request,'details.html')
def Listing(request):
    return render(request,'Listing.html')
def sarchform(request):
    return render(request,'sarchform.html')
def index(request):
    return render(request,'index.html')