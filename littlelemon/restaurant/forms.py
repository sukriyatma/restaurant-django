from typing import Any
from django import forms
from models import *


class BookingForm(forms.Form):
    class Meta():
        Model = Booking
        Field = "__all__"
        
    TIME_OPEN_RESTAURANT = (
        ('', "Select time"),
        ("10 AM", "10 AM"),
        ("11 AM", "11 AM"), 
        ("12 PM", "12 PM"),
        ("1 PM", "1 PM"),
        ("2 PM", "2 PM"),
        ("3 PM", "3 PM"),
        ("4 PM", "4 PM"),
        ("5 PM", "5 PM"),
        ("6 PM", "6 PM"),
        ("7 PM", "7 PM"),
        ("8 PM", "8 PM"),
    )

    name = forms.CharField(label="Name", max_length=255, required=True)
    date = forms.DateField(
        label="Reservation Date", 
        widget=forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}), 
        required=True
    ) 
    time = forms.ChoiceField(
        label="Reservation Time",
        choices=TIME_OPEN_RESTAURANT,
        required=True
    )