from django.db import migrations, models


def delete_legacy_bookings(apps, schema_editor):
    Booking = apps.get_model("app", "Booking")
    Booking.objects.using(schema_editor.connection.alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(delete_legacy_bookings),
        migrations.RemoveField(
            model_name="booking",
            name="booking_date",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="booking_time",
        ),
        migrations.AddField(
            model_name="booking",
            name="check_in",
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name="booking",
            name="check_out",
            field=models.DateField(),
        ),
    ]
