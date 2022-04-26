from operator import truediv
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
    count=Feladat.objects.filter(resztvevo=request.user).count()

    
    if count==0:
        vanmar=False
    else:
        vanmar=True
      
 
    context={
        'feladatok':Feladat.objects.all(),
        'vanmar':vanmar,
    }
   

    return render(request,"menu.html",context)


def jelentkezes(request,valami):


    if 'atjelentkezes' in request.POST or 'jelentkezes' in request.POST :
  
        Feladat.objects.filter(resztvevo=request.user).update(resztvevo="")
        Feladat.objects.filter(nev=valami).update(resztvevo=str(request.user))
    
    if 'lejelentkezes' in request.POST:
        Feladat.objects.filter(resztvevo=request.user).update(resztvevo="")



    return redirect(valasztas)
