from django.shortcuts import render,HttpResponseRedirect
from.forms import employeeregistration
from.models import User

# Create your views here.
#This Function Will Add new Item and Show All Item
def add_show(request):
    if request.method == 'POST':
        fm= employeeregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = employeeregistration()
    else:
        fm = employeeregistration()
    emp = User.objects.all()
    return render(request,'crud1/addandshow.html',{'form':fm,'em':emp})

#This Function Will Delete Or Update
def update_data(request,id):
    if request.method== 'POST':
        pi= User.objects.get(pk=id)
        fm=employeeregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = employeeregistration(instance=pi)
    return render(request,'crud1/updateemployee.html' ,{'form':fm})




# This Function Will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')