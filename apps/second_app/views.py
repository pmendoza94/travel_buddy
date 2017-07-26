from django.shortcuts import render, redirect, HttpResponse
from ..first_app.models import User
from .models import Destination, Traveler
from django.contrib import messages
# Create your views here.
def travels(request):
    print '*** travels ***'
    if not request.session['user_id']:
        return redirect('/')
    context = {
        'users': User.objects.all(),
        'destinations': Destination.objects.all()
    }
    return render(request, 'second_app/index.html', context)

def add(request):
    print '*** add ***'
    if not request.session['user_id']:
        return redirect('/')
    context = {
        'destinations': Destination.objects.all()
        }
    return render(request, 'second_app/add.html', context)

def addtrip(request):
    print '*** addtrip ***'
    if not request.session['user_id']:
        return redirect('/')
    print Destination.objects.all()
    if request.method == 'POST':
        results = Destination.objects.tripVal(request.POST)
        print '************'
        if results['status'] == False:
            for error in results['errors']:
                messages.error(request, error)

        else:
            destination = Destination.objects.createDestination(request.POST)
            messages.success(request, 'Trip has been added!')
    return redirect('/add')

def destination(request):
    print '*** destinations ***'
    if not request.session['user_id']:
        return redirect('/')
    destination = Destination.objects.createDestination(request.POST)
    request.session['destination_id'] = results['destination'].id
    request.session['location'] = results['destination'].location
    print Desintation.objects.all()
    return redirect('/add')

def trip(request):
    print '*** info ***'
    if not request.session['user_id']:
        return redirect('/')
    request.session['destination_id'] = results['destination'].id
    return render(request, 'second_app/plan.html')
