# Generated by Django 5.2 on 2025-05-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='amount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
    ]
