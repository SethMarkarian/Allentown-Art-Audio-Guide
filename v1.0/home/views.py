from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Exhibit

def language(request):
    if request.method == 'POST':
        request.session['language'] = request.POST.get('language', '')
        return redirect('home/')
    return render(request, 'home/language.html')

"""
HOW CONTEXT IS SETUP:

Tutorial (boolean)
    The first time that a user visits the (when the method is not POST), the tutorial infographic will be loaded

Exhibit (Exhibit model)
    Stores an exhibit object (see Exhibit model), or None

Language ('english' or 'spanish')
    Selected on the language.html page
    Stored in request.session['language'] – defaults to english
"""

def home(request):

    context = {
        'tutorial': False,
        'exhibit': None,
        'language': setLanguage(request),
    }

    #If it is the users first time visiting the page (method is not POST), tutorial should be displayed
    if(request.method != 'POST'):
        context['tutorial'] = True
        return render(request, 'home/index.html', context)

    #If the user has requested a new exhibit (by search or by clicking "More")
    else:
        #Case of clicking "More"
        if(request.POST.get('next','') == 'next'):
            exhibit = Exhibit.objects.get(lookup_number = request.session['next'])
            context['exhibit'] = exhibit
            return render(request, 'home/index.html', context)
        #Case of search
        lookupNumber = request.POST.get('lookup_num', '')
        try:
            exhibit = Exhibit.objects.get(lookup_number = lookupNumber)
            context['exhibit'] = exhibit
            if exhibit.additional_lookup_number:
                request.session['next'] = exhibit.additional_lookup_number.lookup_number
        except:
            context['exhibit'] = None
        return render(request, 'home/index.html', context)
        

#Checks to see if language has been set; defaults to english
def setLanguage(request):
    try:
        request.session['language']
    except:
        request.session['language'] = 'english'
    return request.session['language']