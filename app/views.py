from django.shortcuts import render

from django.http import *

def html_forms(request):

    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']

        print(un)
        print(pw)

        return render(request,'responce.html')

    return render(request,'html_forms.html')
