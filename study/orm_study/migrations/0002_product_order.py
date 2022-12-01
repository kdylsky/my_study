# Generated by Django 4.1.3 on 2022-11-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orm_study", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "products",
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("number", models.IntegerField()),
                ("products", models.ManyToManyField(to="orm_study.product")),
            ],
            options={
                "db_table": "orders",
            },
        ),
    ]
