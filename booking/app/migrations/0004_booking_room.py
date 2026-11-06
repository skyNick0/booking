import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_booking_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookings",
                to="app.room",
            ),
        ),
    ]
