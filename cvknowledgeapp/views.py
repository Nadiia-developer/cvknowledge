from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import CreateRegistrationForm
from .models import Registration, TheoreticalKnowledge


def registration(request):
    if (request.method == 'POST'):
        form = CreateRegistrationForm(request.POST)
        if (form.is_valid()):
            person_name = form.cleaned_data['name']
            person = Registration.objects.create(name=person_name)
            person.save()
            return HttpResponse('Person was created with name ' + person_name)
    form = CreateRegistrationForm
    return render(request, 'registration.html', {'form':form})

def theoretical_knowledge(request):
    qn = TheoreticalKnowledge.objects.all().values()
    template = loader.get_template('theoretical_knowledge.html')
    context = {
        'qn': qn,
    }
    return HttpResponse(template.render(context, request))
