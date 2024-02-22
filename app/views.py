from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def dummy(request):
    return render(request,'dummy.html')


def insert_pg(request):
    EFPO=pgform()
    d={'EFPO':EFPO}

    if request.method=='POST':
        DFPO=pgform(request.POST)
        if DFPO.is_valid():
            DFPO.save()
            return HttpResponse('pg inserted successfully')
    return render(request,'insert_pg.html',d)


def display_pg(request):
    QLPO=Pgs.objects.all()
    d1={'QLPO':QLPO}
    return render(request,'display_pg.html',d1)

def view_details(request):
    return render(request,'view_details.html')