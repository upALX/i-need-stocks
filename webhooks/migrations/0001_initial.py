# Generated by Django 5.0.2 on 2024-02-26 23:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('webhook_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('stock_ticker_code', models.CharField(max_length=7)),
                ('webhook_url', models.CharField(max_length=700)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
