from django.shortcuts import render
from django.shortcuts import redirect

from .forms import BookingForm
from .models import Booking, Room


def home(request):
	context = {
		"room_count": Room.objects.count(),
		"booking_count": Booking.objects.count(),
		"recent_bookings": Booking.objects.select_related("user").order_by("-booking_date")[:5],
		"rooms": Room.objects.all()[:3],
	}
	return render(request, "app/home.html", context)


def room_list(request):
	return render(request, "app/room_list.html", {"rooms": Room.objects.all()})


def booking_list(request):
	bookings = Booking.objects.select_related("user").order_by("-booking_date")
	return render(request, "app/booking_list.html", {"bookings": bookings})


def booking_create(request):
	form = BookingForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("booking_list")
	return render(request, "app/booking_form.html", {"form": form})
