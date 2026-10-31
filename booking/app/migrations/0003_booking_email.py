from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_booking_stay_dates"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="email",
            field=models.EmailField(default="", max_length=254),
            preserve_default=False,
        ),
    ]
