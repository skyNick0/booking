from django.test import TestCase
from django.contrib.auth import get_user_model

from .forms import BookingForm
from .models import Room


class BookingFormTests(TestCase):
    def setUp(self):
        self.room = Room.objects.create(
            room_number="101",
            room_type="Standard",
            price_per_night="100.00",
        )
        self.user = get_user_model().objects.create_user(
            username="guest",
            email="guest@example.com",
            password="unused",
        )

    def test_booking_form_saves_email(self):
        form = BookingForm(
            data={
                "user": self.user.pk,
                "email": "booking@example.com",
                "check_in": "2026-10-30",
                "check_out": "2026-11-02",
                "number_of_guests": 2,
                "room": self.room.pk,
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        booking = form.save()
        self.assertEqual(booking.email, "booking@example.com")
        self.assertEqual(booking.user, self.user)

    def test_booking_form_requires_email(self):
        form = BookingForm(
            data={
                "user": self.user.pk,
                "check_in": "2026-10-30",
                "check_out": "2026-11-02",
                "number_of_guests": 2,
                "room": self.room.pk,
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
