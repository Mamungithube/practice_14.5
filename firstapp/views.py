from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ExampleForm
from .forms import MymodelForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            return render(request,'home.html',{'form':form})

    else:
        form = ExampleForm()
    
    return render(request,'home.html',{'form':form})


def model(request):
    if request.method == "POST":
        form = MymodelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = MymodelForm()
    
    return render(request,'model.html',{'form':form})