from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user", "check_in", "check_out", "number_of_guests"]
        widgets = {
            "check_in": forms.DateInput(
                attrs={"type": "date"},
            ),
            "check_out": forms.DateInput(
                attrs={"type": "date"},
            ),
            "number_of_guests": forms.NumberInput(attrs={"min": 1}),
        }