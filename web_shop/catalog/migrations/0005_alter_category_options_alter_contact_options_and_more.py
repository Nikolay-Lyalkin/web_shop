# Generated by Django 5.1.1 on 2024-10-21 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_contact"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "категория", "verbose_name_plural": "категории"},
        ),
        migrations.AlterModelOptions(
            name="contact",
            options={"verbose_name": "контакт", "verbose_name_plural": "контакты"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["category"], "verbose_name": "продукт", "verbose_name_plural": "продукты"},
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="photos/")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="catalog.product",
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "изображение",
                "verbose_name_plural": "изображения",
                "db_table": "images",
            },
        ),
    ]
