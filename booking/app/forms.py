from django import forms

from .models import Booking, Room


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user", "email", "check_in", "check_out", "number_of_guests", "room"]
        widgets = {
            "check_in": forms.DateInput(
                attrs={"type": "date"},
            ),
            "check_out": forms.DateInput(
                attrs={"type": "date"},
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
            "number_of_guests": forms.NumberInput(attrs={"min": 1}),
            "room": forms.Select(attrs={"placeholder": "Select a room"}),
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

    def clean_room_booking_date(self):
        check_in = self.cleaned_data.get("check_in")
        check_out = self.cleaned_data.get("check_out")
        room = self.cleaned_data.get("room")

        if room and check_in and check_out:
            overlapping_bookings = Booking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in,
            )
            if overlapping_bookings.exists():
                raise forms.ValidationError(
                    "This room is already booked for the selected dates."
                )
        return self.cleaned_data

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["room_number", "room_type", "price_per_night"]
        widgets = {
            "room_number": forms.TextInput(attrs={"placeholder": "Enter room number"}),
            "room_type": forms.TextInput(attrs={"placeholder": "Enter room type"}),
            "price_per_night": forms.NumberInput(attrs={"min": 0}),
        }
    