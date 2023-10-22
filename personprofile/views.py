from django.shortcuts import render
from .models import Person
from .PersonForm import PersonForm
from django.db.models import Q

from django.http import HttpResponse

def front_page(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'search_people':
            return HttpResponse('Searching People')
        elif action == 'create_user':
            return HttpResponse('Creating User')
        elif action == 'view':
            return HttpResponse('Viewing Data')
    
    return render(request, 'base.html')


def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            person = Person(name=name, email=email)
            person.save()

            return render(request, 'index.html', {'form': form, 'persons': persons})

    form = PersonForm()
    persons = Person.objects.all()
    
    return render(request, 'index.html', {'form': form, 'persons': persons})


def list_people(request):

    param = request.POST.get('param', '')
    if param:
        profiles = Person.objects.filter(Q(name__icontains=param) | Q(email__icontains=param))
    else:
        profiles = Person.objects.all()
    
    # Return the results as a JSON response
    return render(request, 'list_people.html', {'results': profiles})
