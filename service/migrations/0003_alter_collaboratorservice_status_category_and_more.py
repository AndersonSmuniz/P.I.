# Generated by Django 5.0.4 on 2024-04-10 01:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salon", "0001_initial"),
        ("service", "0002_service_image_alter_service_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collaboratorservice",
            name="status",
            field=models.CharField(
                choices=[(0, "Ativo"), (1, "Inativo")], default="Ativo", max_length=20
            ),
        ),
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.URLField(blank=True, null=True)),
                (
                    "salon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="salon.salon",
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
                "ordering": ["title"],
            },
        ),
        migrations.AddField(
            model_name="service",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="services",
                to="service.category",
            ),
        ),
    ]
