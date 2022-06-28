from django.shortcuts import render
from .forms import BiodataForm
from .models import BiodataModel
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

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
            return render(request, 'index.html', {"list": list})
    return render(request,'create_profile.html',context)
def index(request):
    context = {}
    context['form'] = BiodataForm()
    list = BiodataModel.objects.all()
    return render(request, 'index.html', {"list": list})
def edit(request,id):
    obj = get_object_or_404(BiodataModel, pk=id)
    context = {}
    form = BiodataForm(instance=obj)
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            BiodataModel.objects.filter(pk=id).update(name=form.cleaned_data['name'],contact=form.cleaned_data['contact'],email=form.cleaned_data['email'],place_of_birth=form.cleaned_data['place_of_birth'],sub_place=form.cleaned_data['sub_place'],dob=form.cleaned_data['dob'])
            return home(request)
    context['form'] = form
    return render(request, "edit_form.html", context)
def delete(request,id):
    context = {}
    obj = get_object_or_404(BiodataModel, id=id)
    obj.delete()
    context['form'] = BiodataForm()
    list = BiodataModel.objects.all()
    return render(request, 'index.html', {"list": list})
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