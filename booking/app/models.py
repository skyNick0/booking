from django.db import models
from django.conf import settings

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    email = models.EmailField()
    room = models.ForeignKey(
        "Room",
        on_delete=models.CASCADE,
        related_name="bookings",
        null=True,
    )

    def __str__(self):
        return f"Booking by {self.user.username} from {self.check_in} to {self.check_out}"

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)

    def is_available(self, check_in, check_out):
        return not Booking.objects.filter(
            room=self,
            check_in__lt=check_out,
            check_out__gt=check_in,
        ).exists()

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type} - ${self.price_per_night}"
