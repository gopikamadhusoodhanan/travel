

# Create your views here.
from django.shortcuts import render
from . models import travel,travel1

# Create your views here.
def demo(request):
    obj=travel.objects.all()
    obj2=travel1.objects.all()
    return render(request,'index.html',{'a1':obj,'a2':obj2})

