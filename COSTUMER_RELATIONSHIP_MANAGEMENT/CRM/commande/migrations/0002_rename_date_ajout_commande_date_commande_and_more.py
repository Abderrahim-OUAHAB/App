# Generated by Django 5.0.6 on 2024-06-12 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commande", "0001_initial"),
        ("produit", "0004_alter_produit_quantite_stock"),
    ]

    operations = [
        migrations.RenameField(
            model_name="commande",
            old_name="date_ajout",
            new_name="date_commande",
        ),
        migrations.RemoveField(
            model_name="commande",
            name="nom",
        ),
        migrations.RemoveField(
            model_name="commande",
            name="produit",
        ),
        migrations.AddField(
            model_name="commande",
            name="montant_total",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="commande",
            name="status",
            field=models.CharField(
                choices=[
                    ("En attente", "En attente"),
                    ("Processing", "En traitement"),
                    ("Annulée", "Annulée"),
                    ("Terminée", "Terminée"),
                ],
                max_length=200,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="OrderProduct",
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
                ("quantite", models.IntegerField(null=True)),
                (
                    "commande",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="commande.commande",
                    ),
                ),
                (
                    "produit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="produit.produit",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="commande",
            name="produits",
            field=models.ManyToManyField(
                through="commande.OrderProduct", to="produit.produit"
            ),
        ),
    ]
