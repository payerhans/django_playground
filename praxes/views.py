from django.shortcuts import render
from .models import Name

# Create your views here.


def index(request):
    titel = "Das ist der Titel"
    nachricht = "Überall dieselbe alte Leier. Das Layout ist fertig, der Text lässt auf sich warten."
    context = {'titel' : titel, 'nachricht' : nachricht}
    return render(request, 'index.html', context)

def jquery(request):
    titel = "Jquery Sandbox"
    nachricht = "Überall dieselbe alte Leier. Das Layout ist fertig, der Text lässt auf sich warten."
    context = {'titel' : titel, 'nachricht' : nachricht}
    return render(request, 'jquery.html', context)

def namen(request):
    titel = "Namensliste"
    namensliste = Name.objects.all()

    context = {'titel' : titel, 'namensliste' : namensliste}
    return render(request, 'namen.html', context)
