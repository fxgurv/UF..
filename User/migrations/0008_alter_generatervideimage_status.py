# Generated by Django 4.2.7 on 2023-11-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_generatervideimage_status_generatervideimage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatervideimage',
            name='status',
            field=models.CharField(choices=[('inactive', 'inactive'), ('active', 'active')], max_length=100),
        ),
    ]
