from django.conf import settings
import django.contrib.auth.hashers
import django.db.models.deletion
from django.db import migrations, models


def migrate_legacy_users(apps, schema_editor):
    database = schema_editor.connection.alias
    LegacyUser = apps.get_model("app", "User")
    Booking = apps.get_model("app", "Booking")
    AuthUser = apps.get_model(*settings.AUTH_USER_MODEL.split("."))

    for legacy_user in LegacyUser.objects.using(database).all():
        auth_user = AuthUser.objects.using(database).filter(
            username=legacy_user.username
        ).first()
        if auth_user is None:
            auth_user = AuthUser.objects.using(database).create(
                username=legacy_user.username,
                email=legacy_user.email,
                password=django.contrib.auth.hashers.make_password(None),
                is_active=False,
            )
        Booking.objects.using(database).filter(user_id=legacy_user.pk).update(
            django_user_id=auth_user.pk
        )


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_booking_room"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="django_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RunPython(migrate_legacy_users, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="booking",
            name="user",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="django_user",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="booking",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
