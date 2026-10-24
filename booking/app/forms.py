from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user", "booking_date", "booking_time", "number_of_guests"]
        widgets = {
            "booking_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "booking_time": forms.TimeInput(attrs={"type": "time"}),
            "number_of_guests": forms.NumberInput(attrs={"min": 1}),
        }