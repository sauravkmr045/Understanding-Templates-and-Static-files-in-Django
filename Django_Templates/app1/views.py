from django.shortcuts import render
from app1.models import mymodel
from app1 import forms
# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def model(request):
    data = mymodel.objects.all()
    #mydict ={'val' : data}
    #return render(request,'app1/model.html', context = mydict)
    return render(request,'app1/model.html', {'val': data})


def myform(request):
    form = forms.myform()
    if request.method == 'POST':
        form = forms.myform(request.POST)

        if form.is_valid():
            print('FIRST NAME' + "form.cleaned_data['first_name']")
            print('last NAME' + "form.cleaned_data['last_name']")
            print('EMAIL' + "form.cleaned_data['email']")
            print('TextArea' + "form.cleaned_data['comment']")


    return render(request, 'app1/form.html',{'form':form})
