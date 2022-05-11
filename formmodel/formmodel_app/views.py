from urllib import request
from django.shortcuts import render
from formmodel_app.forms import UserForm

# Create your views here.

def index(request):
    template  = {'insert_me':'Go to /user page for modelForm!'}
    return render(request,'app/index.html',context=template)

def user(request):
    form =  UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST )  

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Form is not valid!')

    return render(request,'app/user.html',{'form':form})