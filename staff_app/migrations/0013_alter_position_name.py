# Generated by Django 4.2.5 on 2023-10-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff_app", "0012_office_company_office_department_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="name",
            field=models.CharField(max_length=156, unique=True),
        ),
    ]
