# Generated by Django 3.2 on 2025-05-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20250507_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Client Name'),
        ),
    ]
