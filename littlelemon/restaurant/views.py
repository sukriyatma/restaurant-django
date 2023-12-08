from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime 
import json
from .forms import *
from .models import *
import re

# Create your views here.

def empty(request):
    return redirect('/home')


def home(request):
    return render(
        request,
        'index.html',
        {
            "content" : "home"
        }
    )


def reservation(request):
    form = BookingForm()
    
    if request.method == 'POST' :

        form = BookingForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            newReservation = Booking(
                name=data["name"],
                date=data["date"],
                time=data["time"]
            )
            newReservation.save()
            return JsonResponse({
                'message' : 'success'
            })

    return render(
        request,
        'index.html',
        {
            "content" : "reservation",
            'form' : form
        }
    )

def getReservation(request):
    date = request.GET.get("date", datetime.today().date())
    
    if not re.search(r"\d{4}-\d{2}-\d{2}", date) :
        return JsonResponse({"message" : "format not match, YYYY-MM-DD"})
    
    reservation = Booking.objects.filter(date=date)
    json_serialize_reservation = serializers.serialize('json',reservation)
    json_reservation = json.loads(json_serialize_reservation) 

    return JsonResponse(json_reservation, safe=False)
