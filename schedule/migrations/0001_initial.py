# Generated by Django 5.0.1 on 2024-02-02 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("collaborator_user", "0001_initial"),
        ("salon", "0001_initial"),
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.IntegerField(
                        choices=[
                            (1, "Domingo"),
                            (2, "Segunda"),
                            (3, "Terça"),
                            (4, "Quarta"),
                            (5, "Quinta"),
                            (6, "Sexta"),
                            (7, "Sábado"),
                        ]
                    ),
                ),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "collaborator_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule",
                        to="collaborator_user.collaboratoruser",
                    ),
                ),
                (
                    "salon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule",
                        to="salon.salon",
                    ),
                ),
                (
                    "service",
                    models.ManyToManyField(
                        related_name="schedule", to="service.service"
                    ),
                ),
            ],
            options={
                "verbose_name": "Agendamento",
                "verbose_name_plural": "Agendamentos",
                "ordering": ["day", "start"],
                "indexes": [
                    models.Index(
                        fields=["day", "start"], name="schedule_sc_day_3f1c8a_idx"
                    ),
                    models.Index(
                        fields=["collaborator_user"],
                        name="schedule_sc_collabo_11657b_idx",
                    ),
                ],
            },
        ),
    ]
