from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
#create your views here.
def User_list(request):
    users = User.objects.all()
    return render(request,"listinpage.html", {'users':users})
def AddUser(request):
    mydict={}
    form = UserForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form'] = form
    return render(request,'add.html',mydict)




