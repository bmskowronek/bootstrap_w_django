# Generated by Django 5.0.4 on 2024-05-27 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chromosome",
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
            ],
        ),
        migrations.CreateModel(
            name="Species",
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
                ("name", models.CharField(max_length=70, unique=True)),
                ("image_file", models.ImageField(upload_to="uploads/")),
            ],
        ),
        migrations.CreateModel(
            name="SNP",
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
                ("position", models.IntegerField()),
                (
                    "ref_allele",
                    models.CharField(
                        blank=True,
                        choices=[("A", "A"), ("T", "T"), ("C", "C"), ("G", "G")],
                        max_length=2,
                    ),
                ),
                (
                    "alt_allele",
                    models.CharField(
                        blank=True,
                        choices=[("A", "A"), ("T", "T"), ("C", "C"), ("G", "G")],
                        max_length=2,
                    ),
                ),
                ("maf", models.FloatField()),
                ("annotations", models.CharField(blank=True, max_length=10)),
                (
                    "chromosome",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="snp_site_app.chromosome",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="chromosome",
            name="species",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="snp_site_app.species"
            ),
        ),
    ]
