# Generated by Django 5.0.1 on 2024-02-02 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("booking", "0001_initial"),
        ("clientuser", "0001_initial"),
        ("collaborator_user", "0001_initial"),
        ("salon", "0001_initial"),
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="booking",
                to="clientuser.clientuser",
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="collaborator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="booking",
                to="collaborator_user.collaboratoruser",
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="salon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="booking",
                to="salon.salon",
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="service",
            field=models.ManyToManyField(to="service.service"),
        ),
        migrations.AlterUniqueTogether(
            name="booking",
            unique_together={("salon", "date")},
        ),
    ]
