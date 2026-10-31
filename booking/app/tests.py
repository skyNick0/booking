from django.test import TestCase

from .forms import BookingForm
from .models import User


class BookingFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
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
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.save().email, "booking@example.com")

    def test_booking_form_requires_email(self):
        form = BookingForm(
            data={
                "user": self.user.pk,
                "check_in": "2026-10-30",
                "check_out": "2026-11-02",
                "number_of_guests": 2,
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
