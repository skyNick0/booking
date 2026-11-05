from django import forms

from .models import Booking, Room


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user", "email", "check_in", "check_out", "number_of_guests"]
        widgets = {
            "check_in": forms.DateInput(
                attrs={"type": "date"},
            ),
            "check_out": forms.DateInput(
                attrs={"type": "date"},
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
            "number_of_guests": forms.NumberInput(attrs={"min": 1}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError(
                "Check-out date must be after the check-in date."
            )
        return cleaned_data

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["room_number", "room_type", "price_per_night"]
        widgets = {
            "room_number": forms.TextInput(attrs={"placeholder": "Enter room number"}),
            "room_type": forms.TextInput(attrs={"placeholder": "Enter room type"}),
            "price_per_night": forms.NumberInput(attrs={"min": 0}),
        }
    