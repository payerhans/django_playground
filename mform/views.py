from django.forms import modelformset_factory
from django.shortcuts import render
from mform.models import Author

# Create your views here.
def index(request):
    titel = "Das die FormApp"
    nachricht = "Überall dieselbe alte Leier. Das Layout ist fertig, der Text lässt auf sich warten."
    context = {'titel' : titel, 'nachricht' : nachricht}
    return render(request, 'index.html', context)

def form1(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            #do something
    else:
        formset = AuthorFormSet()
    context = {'formset' : formset}
    return render(request, 'form1.html', context)