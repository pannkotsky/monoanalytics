# Generated by Django 4.2.16 on 2024-09-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("statement", "0003_merchantcategory_description_ua_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="statementitem",
            name="tags",
            field=models.ManyToManyField(
                related_name="statement_items", to="statement.tag"
            ),
        ),
    ]
