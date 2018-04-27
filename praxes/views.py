from django.shortcuts import render

# Create your views here.


def index(request):
    titel = "Das ist der Titel"
    nachricht = "Überall dieselbe alte Leier. Das Layout ist fertig, der Text lässt auf sich warten."
    context = {'titel' : titel, 'nachricht' : nachricht}
    return render(request, 'index.html', context)