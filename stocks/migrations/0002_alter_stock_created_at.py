# Generated by Django 5.0.2 on 2024-02-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
