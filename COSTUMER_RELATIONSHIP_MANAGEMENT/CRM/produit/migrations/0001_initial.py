# Generated by Django 5.0.6 on 2024-06-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produit",
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
                ("designation", models.CharField(max_length=200, null=True)),
                ("prix", models.FloatField(null=True)),
                ("date_ajout", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
