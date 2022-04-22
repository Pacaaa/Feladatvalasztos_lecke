from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from APP.models import Feladat




def belepes(request):



    if 'belep' in request.POST:
        username = request.POST['felhasznalonev']
        password = request.POST['jelszo']
        user = authenticate(request, username=username, password=password)

        if user is not None:
           
            login(request, user)   
                    
            return redirect("valasztas/")

        else:
            print("rossz")

    
    return render(request,"bejelentkezes.html")



def valasztas(request):
    context={
        'feladatok':Feladat.objects.all()
    }

    return render(request,"menu.html",context)


def jelentkezes(request,valami):
    context={
        'feladatok':Feladat.objects.all()
    }

    return render(request,"menu.html",context)
